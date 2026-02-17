#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn Post Assistant - Semi-Automated
Opens LinkedIn and shows you the post content to copy-paste manually
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'ignore')

# Configuration
VAULT_PATH = Path(__file__).parent
APPROVED_FOLDER = VAULT_PATH / "Approved"
LINKEDIN_POSTED = VAULT_PATH / "LinkedIn_Posted"
LOGS_FOLDER = VAULT_PATH / "Logs"

# Ensure folders exist
APPROVED_FOLDER.mkdir(exist_ok=True)
LINKEDIN_POSTED.mkdir(exist_ok=True)
LOGS_FOLDER.mkdir(exist_ok=True)

def extract_post_content(file_path):
    """Extract post content from approval file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract content between ``` markers
        if '```' in content:
            parts = content.split('```')
            if len(parts) >= 3:
                return parts[1].strip()
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    """Main function"""
    print("=" * 70)
    print("LinkedIn Post Assistant - Semi-Automated")
    print("=" * 70)
    print()

    # Check for approved posts
    approved_files = list(APPROVED_FOLDER.glob("linkedin_post_approval_*.md"))

    if not approved_files:
        print("No approved LinkedIn posts found.")
        print(f"Place approval files in: {APPROVED_FOLDER}")
        print()
        input("Press Enter to exit...")
        return

    print(f"Found {len(approved_files)} approved post(s)")
    print()

    # Process each approved post
    for i, file_path in enumerate(approved_files, 1):
        print(f"\n{'=' * 70}")
        print(f"POST {i} of {len(approved_files)}: {file_path.name}")
        print('=' * 70)

        # Extract content
        post_content = extract_post_content(file_path)

        if not post_content:
            print("Could not extract post content. Skipping...")
            continue

        # Display the post content
        print("\nPOST CONTENT TO COPY:")
        print("-" * 70)
        print(post_content)
        print("-" * 70)
        print()

        # Copy to clipboard if possible
        try:
            import pyperclip
            pyperclip.copy(post_content)
            print("[SUCCESS] Content copied to clipboard!")
        except:
            print("[INFO] Install 'pyperclip' to auto-copy to clipboard")

        print()
        print("INSTRUCTIONS:")
        print("1. A browser will open with LinkedIn")
        print("2. Click 'Start a post' button")
        print("3. Paste the content (Ctrl+V)")
        print("4. Click 'Post' button")
        print()

        input("Press Enter to open LinkedIn...")

        # Open LinkedIn in browser
        try:
            session_dir = VAULT_PATH / "linkedin_session_data"
            session_dir.mkdir(exist_ok=True)

            with sync_playwright() as playwright:
                print("\nOpening LinkedIn...")
                context = playwright.chromium.launch_persistent_context(
                    user_data_dir=str(session_dir),
                    headless=False,
                    args=['--no-sandbox', '--disable-setuid-sandbox']
                )

                page = context.new_page()
                page.goto('https://www.linkedin.com/feed/')

                print("LinkedIn opened!")
                print()
                print("Did you post it successfully?")
                response = input("Type 'yes' when done (or 'skip' to skip): ").strip().lower()

                if response == 'yes':
                    # Move to posted folder
                    posted_path = LINKEDIN_POSTED / file_path.name
                    file_path.rename(posted_path)

                    # Add timestamp
                    with open(posted_path, 'a', encoding='utf-8') as f:
                        f.write(f"\n\n---\n**Posted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

                    print(f"[SUCCESS] Marked as posted: {file_path.name}")
                elif response == 'skip':
                    print(f"[SKIPPED] {file_path.name}")

                context.close()

        except Exception as e:
            print(f"Error opening browser: {e}")
            print()
            print("You can manually:")
            print(f"1. Open LinkedIn in your browser")
            print(f"2. Copy the content above")
            print(f"3. Create a new post and paste it")
            print()
            input("Press Enter to continue...")

    print()
    print("=" * 70)
    print("All posts processed!")
    print("=" * 70)

if __name__ == "__main__":
    main()
