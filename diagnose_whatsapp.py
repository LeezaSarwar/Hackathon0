#!/usr/bin/env python3
"""
WhatsApp Web Diagnostic Tool
Shows exactly what the watcher can see
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from datetime import datetime

SESSION_DIR = Path(__file__).parent / "AI_Employee_Vault" / "whatsapp_session_data"

async def diagnose():
    """Diagnose WhatsApp Web to see what's visible"""
    print("="*70)
    print("WhatsApp Web Diagnostic Tool")
    print("="*70)
    print("\nThis will show you exactly what the watcher can see on WhatsApp Web")
    print("="*70)

    playwright = await async_playwright().start()

    # Launch browser (not persistent to avoid conflicts)
    browser = await playwright.chromium.launch(headless=False)

    # Create context with session data
    context = await browser.new_context(
        storage_state=str(SESSION_DIR / "state.json") if (SESSION_DIR / "state.json").exists() else None
    )

    page = await context.new_page()

    print("\n[1/6] Navigating to WhatsApp Web...")
    await page.goto('https://web.whatsapp.com')
    await asyncio.sleep(5)

    print("\n[2/6] Checking if logged in...")
    try:
        await page.wait_for_selector('#pane-side', timeout=10000)
        print("✅ Logged in successfully!")
    except:
        print("❌ Not logged in - please scan QR code")
        print("Waiting 60 seconds for you to scan...")
        await asyncio.sleep(60)

    print("\n[3/6] Looking for chats...")

    # Try to find all chats
    chat_selectors = [
        'div[role="listitem"]',
        'div[data-testid="cell-frame-container"]',
        'div._2nY6U'
    ]

    all_chats = []
    for selector in chat_selectors:
        all_chats = await page.query_selector_all(selector)
        if all_chats:
            print(f"✅ Found {len(all_chats)} chats using: {selector}")
            break

    if not all_chats:
        print("❌ No chats found!")
        await browser.close()
        return

    print(f"\n[4/6] Analyzing first 3 chats...")

    for idx, chat in enumerate(all_chats[:3]):
        print(f"\n--- Chat {idx + 1} ---")

        try:
            # Get chat name
            name_elem = await chat.query_selector('span[dir="auto"]')
            if name_elem:
                name = await name_elem.inner_text()
                print(f"Name: {name}")

            # Check for unread badge
            unread_badge = await chat.query_selector('span[data-testid="icon-unread-count"]')
            if unread_badge:
                count = await unread_badge.inner_text()
                print(f"Unread: {count} message(s)")
            else:
                print("Unread: None")

            # Get last message preview
            preview_selectors = [
                'span[title]',
                'span.matched-text',
                'div[class*="last-message"]'
            ]

            for selector in preview_selectors:
                preview_elem = await chat.query_selector(selector)
                if preview_elem:
                    preview = await preview_elem.inner_text()
                    if preview and len(preview) > 5:
                        print(f"Last message preview: {preview[:50]}...")
                        break

        except Exception as e:
            print(f"Error analyzing chat: {e}")

    print(f"\n[5/6] Opening first chat to read messages...")

    try:
        first_chat = all_chats[0]
        await first_chat.click()
        await asyncio.sleep(3)

        # Get chat name
        header_name = await page.query_selector('header span[dir="auto"]')
        if header_name:
            chat_name = await header_name.inner_text()
            print(f"Opened chat: {chat_name}")

        # Find all messages
        msg_containers = await page.query_selector_all('div[data-testid="msg-container"]')
        print(f"Total messages in chat: {len(msg_containers)}")

        if msg_containers:
            print(f"\nLast 3 messages:")
            for idx, msg in enumerate(msg_containers[-3:]):
                print(f"\n  Message {idx + 1}:")

                # Try to get message text
                text_elem = await msg.query_selector('span.selectable-text')
                if text_elem:
                    text = await text_elem.inner_text()
                    print(f"    Text: {text[:100]}")

                    # Check for keywords
                    keywords = ['urgent', 'help', 'pricing', 'payment', 'asap', 'emergency']
                    found_keywords = [kw for kw in keywords if kw in text.lower()]
                    if found_keywords:
                        print(f"    ✅ KEYWORDS FOUND: {', '.join(found_keywords)}")
                    else:
                        print(f"    ❌ No keywords found")
                else:
                    print(f"    ❌ Could not read message text")

    except Exception as e:
        print(f"Error opening chat: {e}")

    print(f"\n[6/6] Diagnosis complete!")
    print("="*70)
    print("\nSUMMARY:")
    print(f"- Total chats found: {len(all_chats)}")
    print(f"- First chat analyzed: Yes")
    print("\nWhat to do next:")
    print("1. If you see your sister's message above with keywords, the watcher should detect it")
    print("2. If keywords are NOT found, send a new message with: urgent, help, pricing")
    print("3. If no messages shown, there might be a selector issue")
    print("="*70)

    print("\nBrowser will stay open for 30 seconds...")
    await asyncio.sleep(30)

    await browser.close()

if __name__ == "__main__":
    asyncio.run(diagnose())
