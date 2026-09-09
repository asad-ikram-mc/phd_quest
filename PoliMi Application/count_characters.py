#!/usr/bin/env python3
# Usage: python3 count.py summary.txt description.txt motivations.txt
# Each file holds ONE section's body text only: no headings, no bibliography, no figure captions.
import sys, re
LIMITS = {"summary": (0, 500), "description": (4000, 8000), "motivations": (0, 2000)}
for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    strict = len(s.replace("\n", ""))          # Word-equivalent: paragraph marks not counted
    loose  = len(s)                            # every newline counted as one character
    key = next((k for k in LIMITS if k in path.lower()), None)
    lo, hi = LIMITS.get(key, (0, 0))
    flag = ""
    if hi:
        if loose > hi: flag = f"  OVER by {loose-hi} (worst case)"
        elif strict < lo: flag = f"  UNDER minimum by {lo-strict}"
        else: flag = "  OK on both counts"
    print(f"{path}: strict={strict}  worst-case={loose}  limit={lo}-{hi}{flag}")
