#!/usr/bin/env python3
"""
Lunheng (论衡) one-click installer.

Usage:
    python install.py           # install both skills to ~/.claude/skills/
    python install.py --uninstall   # remove

Cross-platform: Windows / macOS / Linux. No external deps.
"""
import os, sys, shutil, argparse
from pathlib import Path

REPO = Path(__file__).resolve().parent
SKILLS_SRC = REPO / "skills"
SKILLS_DST = Path.home() / ".claude" / "skills"
SKILLS = ["lunheng", "lunheng-quick"]

def install():
    SKILLS_DST.mkdir(parents=True, exist_ok=True)
    for s in SKILLS:
        src, dst = SKILLS_SRC / s, SKILLS_DST / s
        if not src.exists():
            print(f"  ✗ source missing: {src}"); continue
        if dst.exists():
            shutil.rmtree(dst)
            print(f"  ↻ overwriting existing {s}")
        shutil.copytree(src, dst)
        print(f"  ✓ installed {s} → {dst}")
    print(f"\n✅ Done. In Claude Code, try:  /lunheng path/to/your/paper/")

def uninstall():
    for s in SKILLS:
        dst = SKILLS_DST / s
        if dst.exists():
            shutil.rmtree(dst)
            print(f"  ✗ removed {s}")
        else:
            print(f"  - not installed: {s}")
    print("\n✅ Uninstall complete.")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Install Lunheng skills to Claude Code.")
    p.add_argument("--uninstall", action="store_true")
    args = p.parse_args()
    print(f"Lunheng (论衡) installer · target: {SKILLS_DST}\n")
    uninstall() if args.uninstall else install()
