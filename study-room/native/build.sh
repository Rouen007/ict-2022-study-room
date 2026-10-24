#!/bin/zsh
set -euo pipefail

ROOT="/Users/rouen/.gemini/antigravity/scratch/ict-2022-mentorship/study-room"
APP="/Users/rouen/Desktop/ICT 2022 学习室.app"
CONTENTS="$APP/Contents"
MACOS="$CONTENTS/MacOS"
RESOURCES="$CONTENTS/Resources"

if [[ ! -f "$ROOT/native/Study.icns" && -f "$ROOT/native/Icon.swift" ]]; then
  swift "$ROOT/native/Icon.swift" "$ROOT/native/Study.png"
  ICONSET="$ROOT/native/Study.iconset"
  rm -rf "$ICONSET"
  mkdir -p "$ICONSET"
  for s in 16 32 128 256 512; do
    sips -z $s $s "$ROOT/native/Study.png" --out "$ICONSET/icon_${s}x${s}.png" >/dev/null
    s2=$((s * 2))
    sips -z $s2 $s2 "$ROOT/native/Study.png" --out "$ICONSET/icon_${s}x${s}@2x.png" >/dev/null
  done
  iconutil -c icns "$ICONSET" -o "$ROOT/native/Study.icns"
fi

rm -rf "$APP"
mkdir -p "$MACOS" "$RESOURCES"

cp "$ROOT/native/Info.plist" "$CONTENTS/Info.plist"
if [[ -f "$ROOT/native/Study.icns" ]]; then
  cp "$ROOT/native/Study.icns" "$RESOURCES/Study.icns"
fi
cp "$ROOT/index.html" "$RESOURCES/index.html"
cp "$ROOT/style.css" "$RESOURCES/style.css"
cp "$ROOT/distill.css" "$RESOURCES/distill.css"
cp "$ROOT/distill-data.js" "$RESOURCES/distill-data.js"
cp "$ROOT/distill.js" "$RESOURCES/distill.js"
cp "$ROOT/course.js" "$RESOURCES/course.js"
cp "$ROOT/library-data.js" "$RESOURCES/library-data.js"
cp "$ROOT/app.js" "$RESOURCES/app.js"
ditto "$ROOT/lesson-assets" "$RESOURCES/lesson-assets"

xcrun swiftc \
  -parse-as-library \
  "$ROOT/native/App.swift" \
  -o "$MACOS/ICT2022Study" \
  -framework Cocoa \
  -framework WebKit

codesign --force --deep --sign - "$APP"
plutil -lint "$CONTENTS/Info.plist"
echo "Built: $APP"
