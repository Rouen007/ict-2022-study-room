import Cocoa

let size = NSSize(width: 1024, height: 1024)
let image = NSImage(size: size)
image.lockFocus()

// 1. Base macOS Squircle with deep obsidian-navy gradient
let bgRect = NSRect(x: 36, y: 36, width: 952, height: 952)
let bgPath = NSBezierPath(roundedRect: bgRect, xRadius: 215, yRadius: 215)
let gradient = NSGradient(colors: [
    NSColor(calibratedRed: 0.07, green: 0.09, blue: 0.14, alpha: 1.0),
    NSColor(calibratedRed: 0.13, green: 0.16, blue: 0.25, alpha: 1.0)
])!
gradient.draw(in: bgPath, angle: -55)

// Champagne gold outer rim
NSColor(calibratedRed: 0.90, green: 0.72, blue: 0.34, alpha: 0.55).setStroke()
bgPath.lineWidth = 10
bgPath.stroke()

// 2. Subtle "Inner Circle" concentric rings in upper center
let center = NSPoint(x: 512, y: 585)
for radius in [CGFloat(310), CGFloat(225), CGFloat(140)] {
    let ring = NSBezierPath(ovalIn: NSRect(x: center.x - radius, y: center.y - radius, width: radius * 2, height: radius * 2))
    NSColor(calibratedRed: 0.92, green: 0.75, blue: 0.38, alpha: 0.11).setStroke()
    ring.lineWidth = 4
    ring.stroke()
}

// 3. Dashed BSL Liquidity Sweep line near top
let bslLine = NSBezierPath()
bslLine.move(to: NSPoint(x: 155, y: 815))
bslLine.line(to: NSPoint(x: 869, y: 815))
let dashPattern: [CGFloat] = [18, 12]
bslLine.setLineDash(dashPattern, count: 2, phase: 0)
bslLine.lineWidth = 6
NSColor(calibratedRed: 0.95, green: 0.42, blue: 0.42, alpha: 0.85).setStroke()
bslLine.stroke()

// 4. Fair Value Gap (FVG) golden highlight zone across middle
let fvgRect = NSRect(x: 210, y: 500, width: 620, height: 120)
let fvgPath = NSBezierPath(roundedRect: fvgRect, xRadius: 14, yRadius: 14)
NSColor(calibratedRed: 0.95, green: 0.75, blue: 0.28, alpha: 0.22).setFill()
fvgPath.fill()
NSColor(calibratedRed: 0.95, green: 0.75, blue: 0.28, alpha: 0.85).setStroke()
fvgPath.lineWidth = 5
fvgPath.stroke()

("FVG" as NSString).draw(
    at: NSPoint(x: 725, y: 534),
    withAttributes: [
        .font: NSFont.monospacedSystemFont(ofSize: 38, weight: .bold),
        .foregroundColor: NSColor(calibratedRed: 0.98, green: 0.82, blue: 0.42, alpha: 0.95)
    ]
)

// 5. Three ICT Displacement Candlesticks (Stop Hunt -> Displacement -> Retracement into FVG)
// Candle 1: Sweep BSL high then reject
let c1Wick = NSBezierPath()
c1Wick.move(to: NSPoint(x: 265, y: 600))
c1Wick.line(to: NSPoint(x: 265, y: 865)) // Sweeps above 815 BSL line!
c1Wick.lineWidth = 14
NSColor(calibratedRed: 0.95, green: 0.76, blue: 0.34, alpha: 1.0).setStroke()
c1Wick.stroke()
NSColor(calibratedRed: 0.95, green: 0.76, blue: 0.34, alpha: 1.0).setFill()
NSBezierPath(roundedRect: NSRect(x: 215, y: 635, width: 100, height: 155), xRadius: 12, yRadius: 12).fill()

// Candle 2: Massive Bearish Displacement Candle leaving the FVG
let c2Wick = NSBezierPath()
c2Wick.move(to: NSPoint(x: 455, y: 340))
c2Wick.line(to: NSPoint(x: 455, y: 785))
c2Wick.lineWidth = 14
NSColor(calibratedRed: 0.94, green: 0.36, blue: 0.36, alpha: 1.0).setStroke()
c2Wick.stroke()
NSColor(calibratedRed: 0.94, green: 0.36, blue: 0.36, alpha: 1.0).setFill()
NSBezierPath(roundedRect: NSRect(x: 403, y: 380, width: 104, height: 365), xRadius: 12, yRadius: 12).fill()

// Candle 3: Tap back into FVG (500..620) and continue down
let c3Wick = NSBezierPath()
c3Wick.move(to: NSPoint(x: 645, y: 300))
c3Wick.line(to: NSPoint(x: 645, y: 565)) // Taps right into FVG!
c3Wick.lineWidth = 14
NSColor(calibratedRed: 0.30, green: 0.84, blue: 0.68, alpha: 1.0).setStroke()
c3Wick.stroke()
NSColor(calibratedRed: 0.30, green: 0.84, blue: 0.68, alpha: 1.0).setFill()
NSBezierPath(roundedRect: NSRect(x: 595, y: 335, width: 100, height: 150), xRadius: 12, yRadius: 12).fill()

// 6. Bottom Badge: "ICT 22"
let titleAttr: [NSAttributedString.Key: Any] = [
    .font: NSFont.systemFont(ofSize: 132, weight: .black),
    .foregroundColor: NSColor.white
]
let subAttr: [NSAttributedString.Key: Any] = [
    .font: NSFont.monospacedSystemFont(ofSize: 116, weight: .heavy),
    .foregroundColor: NSColor(calibratedRed: 0.96, green: 0.78, blue: 0.35, alpha: 1.0)
]
("ICT" as NSString).draw(at: NSPoint(x: 205, y: 108), withAttributes: titleAttr)
("22" as NSString).draw(at: NSPoint(x: 585, y: 116), withAttributes: subAttr)

image.unlockFocus()
let bitmap = NSBitmapImageRep(data: image.tiffRepresentation!)!
try bitmap.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: CommandLine.arguments[1]))
