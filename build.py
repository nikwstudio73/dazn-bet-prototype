#!/usr/bin/env python3
"""Bundle public/index.html + public/assets/ into one self-contained HTML file (fonts and images inlined as base64).

Usage:  python3 build.py            -> dist/DAZN-Bet-in-Scores-prototype.html
The single file is what gets shared / screen-shared; it works offline with no server.
"""
import base64, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'public')  # the folder Vercel serves
MIME = {'.png': 'image/png', '.woff2': 'font/woff2', '.svg': 'image/svg+xml', '.jpg': 'image/jpeg', '.webp': 'image/webp'}

def inline(m):
    path = m.group(0)
    ext = os.path.splitext(path)[1].lower()
    with open(os.path.join(SRC, path), 'rb') as f:
        return f'data:{MIME[ext]};base64,' + base64.b64encode(f.read()).decode()

src = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()
out = re.sub(r'assets/(?:img|fonts)/[\w.-]+\.(?:png|woff2|svg|jpg|webp)', inline, src)
os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
dst = os.path.join(ROOT, 'dist', 'DAZN-Bet-in-Scores-prototype.html')
open(dst, 'w', encoding='utf-8').write(out)
print(f'{dst}  {len(out) // 1024} KB')
