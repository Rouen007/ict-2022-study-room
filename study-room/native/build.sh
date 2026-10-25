#!/bin/zsh
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
APP="${1:-$HOME/Desktop/ICT 2022 学习室.app}"
# Build a complete sibling bundle first. Existing installs are archived, never deleted.
[[ "$APP" = /* && "$APP" = *.app && ! -L "$APP" ]] || { echo "Expected an absolute, non-symlink .app destination" >&2; exit 2; }
PARENT="$(dirname "$APP")"
[[ -d "$PARENT" ]] || { echo "Destination parent must exist" >&2; exit 2; }
if [[ -e "$APP" ]]; then
  EXISTING_ID=$(/usr/libexec/PlistBuddy -c 'Print :CFBundleIdentifier' "$APP/Contents/Info.plist" 2>/dev/null || true)
  [[ "$EXISTING_ID" = local.rouen.ict2022study ]] || { echo "Refusing to replace another application" >&2; exit 2; }
fi
BUILD_DIR=$(mktemp -d "$PARENT/.ict-build.XXXXXX")
STAGED="$BUILD_DIR/ICT 2022 学习室.app"
CONTENTS="$STAGED/Contents"
MACOS="$CONTENTS/MacOS"
RESOURCES="$CONTENTS/Resources"
mkdir -p "$MACOS" "$RESOURCES"
cp "$ROOT/native/Info.plist" "$CONTENTS/Info.plist"
/usr/libexec/PlistBuddy -c "Add :StudyRootPath string $ROOT" "$CONTENTS/Info.plist"
/usr/libexec/PlistBuddy -c "Add :StudyDataPath string $ROOT" "$CONTENTS/Info.plist"
if [[ -f "$ROOT/native/Study.icns" ]]; then
  cp "$ROOT/native/Study.icns" "$RESOURCES/Study.icns"
else
  swift "$ROOT/native/Icon.swift" "$BUILD_DIR/Study.png"
  ICONSET="$BUILD_DIR/Study.iconset"
  mkdir -p "$ICONSET"
  for s in 16 32 128 256 512; do
    sips -z $s $s "$BUILD_DIR/Study.png" --out "$ICONSET/icon_${s}x${s}.png" >/dev/null
    s2=$((s * 2))
    sips -z $s2 $s2 "$BUILD_DIR/Study.png" --out "$ICONSET/icon_${s}x${s}@2x.png" >/dev/null
  done
  iconutil -c icns "$ICONSET" -o "$RESOURCES/Study.icns"
fi
for file in index.html style.css distill.css distill-data.js distill.js course.js library-data.js app.js version.js version.json; do
  cp "$ROOT/$file" "$RESOURCES/$file"
done
ditto "$ROOT/lesson-assets" "$RESOURCES/lesson-assets"
[[ -d "$ROOT/comparative-assets" ]] && ditto "$ROOT/comparative-assets" "$RESOURCES/comparative-assets"
xcrun swiftc -parse-as-library "$ROOT/native/NotebookStore.swift" "$ROOT/native/App.swift" -o "$MACOS/ICT2022Study" -framework Cocoa -framework WebKit
codesign --force --deep --sign - "$STAGED"
plutil -lint "$CONTENTS/Info.plist"
codesign --verify --deep --strict "$STAGED"
BACKUP=""
if [[ -e "$APP" ]]; then
  ARCHIVES="$PARENT/.ict-app-archives"
  mkdir -p "$ARCHIVES"
  BACKUP="$ARCHIVES/ICT2022-$(date +%Y%m%d-%H%M%S)-$$.app"
  mv "$APP" "$BACKUP"
fi
if ! mv "$STAGED" "$APP"; then
  [[ -n "$BACKUP" ]] && mv "$BACKUP" "$APP"
  echo "Install failed; previous application restored" >&2
  exit 1
fi
echo "Built: $APP"
[[ -z "$BACKUP" ]] || echo "Previous app archived: $BACKUP"
echo "Build workspace retained: $BUILD_DIR"
