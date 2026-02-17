#!/usr/bin/env python3
"""
Test WhatsApp Web selectors to debug message detection
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
from datetime import datetime

SESSION_DIR = Path(__file__).parent / "AI_Employee_Vault" / "whatsapp_session_data"

async def test_selectors():
    """Test different selectors to find what works"""
    print("="*60)
    print("WhatsApp Web Selector Test")
    print("="*60)

    playwright = await async_playwright().start()

    # Use existing session
    context = await playwright.chromium.launch_persistent_context(
        user_data_dir=str(SESSION_DIR),
        headless=False,
        args=['--no-sandbox']
    )

    page = await context.new_page()

    print("\n1. Navigating to WhatsApp Web...")
    await page.goto('https://web.whatsapp.com')
    await asyncio.sleep(5)

    print("\n2. Testing chat list selectors...")
    chat_selectors = [
        'div[data-testid="chat-list"]',
        'div[id="pane-side"]',
        'div[role="listitem"]',
        'div._2nY6U'
    ]

    for selector in chat_selectors:
        try:
            elements = await page.query_selector_all(selector)
            print(f"   ✓ {selector}: Found {len(elements)} elements")
        except Exception as e:
            print(f"   ✗ {selector}: Error - {e}")

    print("\n3. Testing unread badge selectors...")
    unread_selectors = [
        'span[data-testid="icon-unread-count"]',
        'span[data-icon="unread-count"]',
        'div[aria-label*="unread"]',
        'span._1pJ9J'
    ]

    for selector in unread_selectors:
        try:
            elements = await page.query_selector_all(selector)
            print(f"   ✓ {selector}: Found {len(elements)} elements")
        except Exception as e:
            print(f"   ✗ {selector}: Error - {e}")

    print("\n4. Clicking on first chat...")
    try:
        # Try to find and click first chat
        first_chat = await page.query_selector('div[role="listitem"]')
        if first_chat:
            await first_chat.click()
            await asyncio.sleep(2)
            print("   ✓ Clicked on first chat")

            print("\n5. Testing sender name selectors...")
            sender_selectors = [
                'header span[dir="auto"]',
                'header div[role="button"] span',
                'div[data-testid="conversation-header"] span',
                'header span[title]'
            ]

            for selector in sender_selectors:
                try:
                    element = await page.query_selector(selector)
                    if element:
                        text = await element.inner_text()
                        print(f"   ✓ {selector}: '{text}'")
                except Exception as e:
                    print(f"   ✗ {selector}: Error - {e}")

            print("\n6. Testing message container selectors...")
            msg_selectors = [
                'div[data-testid="msg-container"]',
                'div.message-in',
                'div[class*="message"]',
                'div[role="row"]'
            ]

            for selector in msg_selectors:
                try:
                    elements = await page.query_selector_all(selector)
                    print(f"   ✓ {selector}: Found {len(elements)} messages")
                except Exception as e:
                    print(f"   ✗ {selector}: Error - {e}")

            print("\n7. Testing message text selectors on last message...")
            # Get last message
            messages = await page.query_selector_all('div[data-testid="msg-container"]')
            if messages:
                last_msg = messages[-1]

                text_selectors = [
                    'span.selectable-text',
                    'div.selectable-text',
                    'span[dir="ltr"]',
                    'div[class*="copyable-text"] span'
                ]

                for selector in text_selectors:
                    try:
                        element = await last_msg.query_selector(selector)
                        if element:
                            text = await element.inner_text()
                            print(f"   ✓ {selector}: '{text[:50]}...'")
                    except Exception as e:
                        print(f"   ✗ {selector}: Error - {e}")
            else:
                print("   ✗ No messages found to test text selectors")
        else:
            print("   ✗ Could not find first chat")
    except Exception as e:
        print(f"   ✗ Error clicking chat: {e}")

    print("\n" + "="*60)
    print("Test complete! Press Ctrl+C to exit...")
    print("="*60)

    # Keep browser open
    await asyncio.sleep(300)
    await context.close()

if __name__ == "__main__":
    asyncio.run(test_selectors())
