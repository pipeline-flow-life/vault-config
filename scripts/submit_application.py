#!/usr/bin/env python3
"""
submit_application.py — Move application docs from ToSubmit/ to Submitted/
and update Application Tracker.md status.

Usage:
    python3 submit_application.py <VaultRoot> <CompanyShort> <RoleShort>

Example:
    python3 submit_application.py \
        "/Users/jonchristiansen/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault" \
        "NetStandard" "vCIO"

What it does:
    1. Moves all files matching *<CompanyShort>*<RoleShort>* from ToSubmit/ to Submitted/
    2. In Application Tracker.md, replaces the [!success] Ready to Submit callout
       for that company with a [!note] Submitted callout including today's date
    3. Prints a summary of what moved and what changed

Why a script instead of a shell one-liner:
    Path handling with spaces (iCloud vault path) is fragile in bash.
    Python handles it cleanly and gives us readable error messages.
"""

import sys
import os
import shutil
import re
from datetime import date

def main():
    if len(sys.argv) != 4:
        print("Usage: submit_application.py <VaultRoot> <CompanyShort> <RoleShort>")
        sys.exit(1)

    vault    = sys.argv[1]
    company  = sys.argv[2]
    role     = sys.argv[3]
    pattern  = f"{company}.*{role}"

    to_submit = os.path.join(vault, "Career (Jon)", "ToSubmit")
    submitted = os.path.join(vault, "Career (Jon)", "Submitted")
    tracker   = os.path.join(vault, "Career (Jon)", "Application Tracker.md")

    os.makedirs(submitted, exist_ok=True)

    # ── Step 1: Move matching files ──────────────────────────────────────────
    moved = []
    if not os.path.isdir(to_submit):
        print(f"ERROR: ToSubmit folder not found at {to_submit}")
        sys.exit(1)

    for fname in os.listdir(to_submit):
        if re.search(pattern, fname, re.IGNORECASE):
            src = os.path.join(to_submit, fname)
            dst = os.path.join(submitted, fname)
            shutil.move(src, dst)
            moved.append(fname)

    if not moved:
        print(f"No files matching '{pattern}' found in ToSubmit/. Nothing moved.")
    else:
        print(f"Moved {len(moved)} file(s) to Submitted/:")
        for f in moved:
            print(f"  {f}")

    # ── Step 2: Update Application Tracker.md ───────────────────────────────
    if not os.path.isfile(tracker):
        print(f"WARNING: Application Tracker not found at {tracker}. Skipping status update.")
        sys.exit(0)

    with open(tracker, "r") as f:
        content = f.read()

    today = date.today().strftime("%Y-%m-%d")

    # Replace the Ready to Submit callout for this company with Submitted
    # Matches: > [!success] Ready to Submit\n> Applied: <date>
    old_pattern = (
        r'(## ' + re.escape(company) + r'.*?\n\n)'   # section header + blank
        r'> \[!success\] Ready to Submit\n'
        r'> (Applied: [^\n]+)'
    )
    replacement = (
        r'\1'
        r'> [!note] Submitted\n'
        r'> \2 · Submitted: ' + today
    )

    new_content, count = re.subn(old_pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        # Try replacing [!warning] Applied as well (if already past ready state)
        old_pattern2 = (
            r'(## ' + re.escape(company) + r'.*?\n\n)'
            r'> \[!warning\] Applied\n'
            r'> (Applied: [^\n]+)'
        )
        new_content, count = re.subn(old_pattern2, replacement, content, flags=re.DOTALL)

    if count > 0:
        with open(tracker, "w") as f:
            f.write(new_content)
        print(f"Application Tracker updated: {company} status → Submitted ({today})")
    else:
        print(f"WARNING: Could not find a 'Ready to Submit' or 'Applied' block for '{company}' in tracker. Update manually.")

if __name__ == "__main__":
    main()
