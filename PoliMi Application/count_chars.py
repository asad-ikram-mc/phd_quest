#!/usr/bin/env python3
"""
PoliMi character counter.

The call counts CHARACTERS INCLUDING SPACES AND PUNCTUATION, and excludes the
bibliography and pictures. Word processors disagree about this, so count here.

Usage:
    python3 count_chars.py proposal.txt

Put your text in a plain .txt file with these three markers on their own lines:

    ===SUMMARY===          (max 500)
    ===DESCRIPTION===      (min 4,000, max 8,000)
    ===MOTIVATIONS===      (max 2,000)
    ===BIBLIOGRAPHY===     (not counted; put references after this marker)
"""
import sys, re

LIMITS = {
    "SUMMARY":      (0,     500),
    "DESCRIPTION":  (4000,  8000),
    "MOTIVATIONS":  (0,     2000),
}

def main(path):
    text = open(path, encoding="utf-8").read()
    parts, current = {}, None
    for line in text.splitlines():
        m = re.match(r"^\s*===\s*([A-Z]+)\s*===\s*$", line)
        if m:
            current = m.group(1)
            parts[current] = []
            continue
        if current:
            parts[current].append(line)

    if not parts:
        print("No ===SECTION=== markers found. See the docstring at the top of this file.")
        return 1

    print(f"\n  {'SECTION':<14} {'CHARS':>7}  {'LIMIT':>13}   STATUS")
    print("  " + "-" * 56)
    ok = True
    for name, (lo, hi) in LIMITS.items():
        if name not in parts:
            print(f"  {name:<14} {'--':>7}  {f'{lo}-{hi}' if lo else f'max {hi}':>13}   MISSING")
            ok = False
            continue
        # Join with newlines, strip leading/trailing blank lines, keep internal spacing.
        body = "\n".join(parts[name]).strip()
        n = len(body)
        if n < lo:
            status, ok = f"SHORT by {lo - n}", False
        elif n > hi:
            status, ok = f"OVER by {n - hi}", False
        else:
            status = f"ok, {hi - n} spare"
        label = f"{lo}-{hi}" if lo else f"max {hi}"
        print(f"  {name:<14} {n:>7}  {label:>13}   {status}")

    if "BIBLIOGRAPHY" in parts:
        b = len("\n".join(parts["BIBLIOGRAPHY"]).strip())
        print(f"  {'BIBLIOGRAPHY':<14} {b:>7}  {'not counted':>13}   excluded by the call")

    print()
    print("  " + ("ALL SECTIONS WITHIN LIMITS" if ok else "NOT READY - fix the rows above"))
    print()
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "proposal.txt"))
