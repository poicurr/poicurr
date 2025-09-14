#!/usr/bin/env python3
from datetime import datetime, timezone, timedelta
import random, pathlib

# ============ 設定 ============
W, H = 800, 200
JST = timezone(timedelta(hours=9))
GAGS = [
  "Today's Reflection: Don't stake your life on the README",
  "Abandon previous projects when new ideas pop up",
  "Get bored halfway through",
  "Revolutionary ideas strike late at night.",
  "Development fueled by sheer willpower",
  "Tip: Read the README before running ‘npm start’",
  "Bugs are features. Features are gods. Gods rush deployment",
  "CI isn't just red-glowing decor",
  "Zero issues. Not peace, but indifference",
  "TODOs written in the README mostly stay TODOs",
  "Optimize after it works. Decorate the README first",
  "Screenshots over comments",
  "LGTMeow 🐱: Appearance is justice",
  "Documentation is an asset. Maintenance is an obligation",
  "The space between README lines matters more than code",
  "Don't put off tests or README until tomorrow. Do them today",
  "404 is a performance",
]

# ============ 動的テキスト ============
now = datetime.now(JST)
dstr = now.strftime("%Y-%m-%d %H:%M JST")
msg = random.choice(GAGS)

# ============ SVGアニメ ============
svg_anim = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g2" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0%" stop-color="#00ffe5"/>
      <stop offset="50%" stop-color="#a700ff"/>
      <stop offset="100%" stop-color="#00ffe5"/>
      <animate attributeName="x1" values="0;1;0" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="1;0;1" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
    <filter id="glow2">
      <feGaussianBlur stdDeviation="3" result="b1"/>
      <feMerge><feMergeNode in="b1"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="flicker">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="1" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="1">
        <animate attributeName="scale" values="0;2;0" dur="0.8s" repeatCount="indefinite"/>
      </feDisplacementMap>
    </filter>
  </defs>
  <rect width="{W}" height="{H}" fill="#0D1117"/>
  <g font-family="Consolas, monospace">
    <text x="24" y="48" fill="#7f8c8d" font-size="16">{dstr}
      <animate attributeName="opacity" values="1;0.6;1" dur="2s" repeatCount="indefinite"/>
    </text>
  </g>
  <g filter="url(#glow2)">
    <text x="24" y="115" fill="none" stroke="url(#g2)" stroke-width="2"
          font-family="Segoe UI, system-ui, -apple-system, sans-serif"
          font-size="28" filter="url(#flicker)">{msg}</text>
    <text x="24" y="115" fill="url(#g2)"
          font-family="Segoe UI, system-ui, -apple-system, sans-serif"
          font-size="28" opacity="0.18">{msg}</text>
    <rect x="24" y="90" width="752" height="34" fill="none" stroke="#00ffe5" opacity="0.25">
      <animate attributeName="opacity" values="0.25;0.6;0.25" dur="3s" repeatCount="indefinite"/>
    </rect>
  </g>
  <rect x="0" y="-40" width="{W}" height="40" fill="url(#g2)" opacity="0.08">
    <animate attributeName="y" values="-40;{H};-40" dur="4s" repeatCount="indefinite"/>
  </rect>
</svg>
'''

# 書き出し
root = pathlib.Path(__file__).resolve().parents[1]
(root / "assets").mkdir(parents=True, exist_ok=True)
(root / "assets" / "daily_animated.svg").write_text(svg_anim, encoding="utf-8")



