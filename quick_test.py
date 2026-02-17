#!/usr/bin/env python3
"""Quick test to see if WhatsApp is accessible"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

SESSION_DIR = Path(__file__).parent / "AI_Employee_Vault" / "whatsapp_session_data"

async def quick_test():
    print("="*60)
    print("Quick WhatsApp Test")
    print("="*60)

    playwright = await async_playwright().start()

    context = await playwright.chromium.launch_persistent_context(
        user_data_dir=str(SESSION_DIR),
        headless=False,
        args=['--no-sandbox']
    )

    page = await context.new_page()

    print("\n1. Going to WhatsApp Web...")
    await page.goto('https://web.whatsapp.com', wait_until='domcontentloaded')
    await asyncio.sleep(5)

    print("2. Checking login...")
    try:
        await page.wait_for_selector('#pane-side', timeout=10000)
        print("   ✓ Logged in!")
    except:
        print("   ✗ Not logged in")
        await asyncio.sleep(60)

    print("\n3. Looking for chats...")
    chats = await page.query_selector_all('div[role="listitem"]')
    print(f"   Found {len(chats)} chats")

    if chats:
        print("\n4. Opening first chat...")
        await chats[0].click()
        await asyncio.sleep(2)

        # Get chat name
        name_elem = await page.query_selector('header span[dir="auto"]')
        if name_elem:
            name = await name_elem.inner_text()
            print(f"   Chat: {name}")

        # Get messages
        messages = await page.query_selector_all('div[data-testid="msg-container"]')
        print(f"   Messages: {len(messages)}")

        if messages:
            print("\n5. Last 3 messages:")
            for i, msg in enumerate(messages[-3:]):
                text_elem = await msg.query_selector('span.selectable-text')
                if text_elem:
                    text = await text_elem.inner_text()
                    print(f"   {i+1}. {text[:50]}...")

                    # Check keywords
                    keywords = ['urgent', 'help', 'pricing', 'payment']
                    found = [k for k in keywords if k in text.lower()]
                    if found:
                        print(f"      ✓ Keywords: {', '.join(found)}")

    print("\n" + "="*60)
    print("Test complete! Browser will close in 10 seconds...")
    print("="*60)
    await asyncio.sleep(10)

    await context.close()

if __name__ == "__main__":
    asyncio.run(quick_test())
