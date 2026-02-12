#!/usr/bin/env python3
"""
WhatsApp Watcher for AI Employee
Monitors WhatsApp Web for important messages using Playwright
"""

import os
import time
import json
import asyncio
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

# Configuration
VAULT_PATH = Path(__file__).parent
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
LOGS_FOLDER = VAULT_PATH / "Logs"
SESSION_FILE = VAULT_PATH / "whatsapp_session.json"
PROCESSED_IDS_FILE = VAULT_PATH / "processed_whatsapp.json"

# Keywords to monitor
URGENT_KEYWORDS = ['urgent', 'asap', 'emergency', 'critical', 'help', 'problem']
BUSINESS_KEYWORDS = ['pricing', 'quote', 'order', 'payment', 'invoice', 'delivery']
INQUIRY_KEYWORDS = ['question', 'inquiry', 'information', 'details', 'available']

# Ensure folders exist
NEEDS_ACTION_FOLDER.mkdir(exist_ok=True)
LOGS_FOLDER.mkdir(exist_ok=True)


class WhatsAppWatcher:
    """WhatsApp Web monitoring and task creation"""

    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self.processed_ids = self.load_processed_ids()
        self.log_file = LOGS_FOLDER / f"whatsapp_watcher_{datetime.now().strftime('%Y%m%d')}.md"
        self.session_dir = VAULT_PATH / "whatsapp_session_data"
        self.session_dir.mkdir(exist_ok=True)
        self.log("WhatsApp Watcher initialized")

    def log(self, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        print(log_entry.strip())

    def load_processed_ids(self):
        """Load list of already processed message IDs"""
        if PROCESSED_IDS_FILE.exists():
            try:
                with open(PROCESSED_IDS_FILE, 'r') as f:
                    return set(json.load(f))
            except Exception as e:
                self.log(f"Error loading processed IDs: {e}")
                return set()
        return set()

    def save_processed_ids(self):
        """Save processed message IDs to file"""
        try:
            with open(PROCESSED_IDS_FILE, 'w') as f:
                json.dump(list(self.processed_ids), f)
        except Exception as e:
            self.log(f"Error saving processed IDs: {e}")

    def determine_priority(self, message_text, sender):
        """Determine message priority based on content"""
        text = message_text.lower()

        # Check for urgent keywords
        if any(keyword in text for keyword in URGENT_KEYWORDS):
            return 'P0 - Critical'

        # Check for business keywords
        if any(keyword in text for keyword in BUSINESS_KEYWORDS):
            return 'P1 - High'

        # Check for inquiry keywords
        if any(keyword in text for keyword in INQUIRY_KEYWORDS):
            return 'P2 - Medium'

        return 'P2 - Medium'

    def create_whatsapp_task(self, message_data):
        """Create task file for WhatsApp message"""
        try:
            priority = self.determine_priority(
                message_data['text'],
                message_data['sender']
            )

            # Generate task filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_sender = "".join(c if c.isalnum() or c in ('-', '_') else '_'
                                 for c in message_data['sender'][:30])
            task_filename = f"whatsapp_{safe_sender}_{timestamp}.md"
            task_path = NEEDS_ACTION_FOLDER / task_filename

            # Create task content
            task_content = f"""# WhatsApp Message: {message_data['sender']}

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Priority:** {priority}
**Status:** Pending
**Source:** WhatsApp Watcher

---

## 💬 Message Details

- **From:** {message_data['sender']}
- **Received:** {message_data['time']}
- **Message ID:** `{message_data['id']}`
- **Chat Type:** {message_data.get('chat_type', 'Unknown')}

---

## 📝 Message Content

```
{message_data['text']}
```

---

## 🎯 Suggested Actions

- [ ] Read and analyze message
- [ ] Determine appropriate response
- [ ] Check Company_Handbook for response templates
- [ ] Draft reply
- [ ] Get approval if needed (new contact or sensitive)
- [ ] Send response via WhatsApp
- [ ] Update Dashboard

---

## 💡 Response Guidelines

Based on priority level **{priority}**:

- If **P0 (Critical)**: Respond within 30 minutes
- If **P1 (High)**: Respond within 2 hours
- If **P2 (Medium)**: Respond within 4 hours
- If **P3 (Low)**: Respond within 24 hours

---

## 📋 Response Template Suggestions

### For Pricing Inquiries:
"Thank you for your interest! I'd be happy to provide a quote. Could you share more details about [specific requirements]?"

### For Urgent Issues:
"I understand this is urgent. Let me look into this immediately and get back to you within [timeframe]."

### For General Inquiries:
"Thanks for reaching out! [Answer their question]. Is there anything else I can help you with?"

---

## 📝 Notes

*Add analysis and response notes here*

---

## ✅ Completion Checklist

- [ ] Message reviewed
- [ ] Context gathered (previous conversations)
- [ ] Response drafted
- [ ] Approval obtained (if required)
- [ ] Response sent
- [ ] Dashboard updated
- [ ] Task moved to Done

---

**Task File:** `{task_filename}`
**Generated by:** WhatsApp Watcher (Automated)
"""

            # Write task file
            with open(task_path, 'w', encoding='utf-8') as f:
                f.write(task_content)

            self.log(f"Created task: {task_filename}")
            return True

        except Exception as e:
            self.log(f"Error creating WhatsApp task: {e}")
            return False

    async def initialize_browser(self):
        """Initialize Playwright browser with persistent session"""
        try:
            playwright = await async_playwright().start()

            # Launch browser with persistent context (saves session)
            self.context = await playwright.chromium.launch_persistent_context(
                user_data_dir=str(self.session_dir),
                headless=False,  # Set to True for production
                args=['--no-sandbox', '--disable-setuid-sandbox']
            )

            self.page = await self.context.new_page()
            self.log("Browser initialized successfully")
            return True

        except Exception as e:
            self.log(f"Error initializing browser: {e}")
            return False

    async def login_whatsapp(self):
        """Navigate to WhatsApp Web and handle login"""
        try:
            self.log("Navigating to WhatsApp Web...")
            await self.page.goto('https://web.whatsapp.com', wait_until='networkidle')

            # Check if already logged in
            try:
                await self.page.wait_for_selector('div[data-testid="chat-list"]', timeout=10000)
                self.log("Already logged in to WhatsApp Web")
                return True
            except:
                self.log("Please scan QR code to login...")
                self.log("Waiting for login (60 seconds)...")

                # Wait for login
                await self.page.wait_for_selector('div[data-testid="chat-list"]', timeout=60000)
                self.log("Login successful!")
                return True

        except Exception as e:
            self.log(f"Error during WhatsApp login: {e}")
            return False

    async def get_unread_messages(self):
        """Fetch unread messages from WhatsApp Web"""
        try:
            # Find all chats with unread badge
            unread_chats = await self.page.query_selector_all('span[data-testid="icon-unread-count"]')

            if not unread_chats:
                return []

            messages = []

            for badge in unread_chats[:5]:  # Limit to 5 chats at a time
                try:
                    # Click on the chat
                    chat_element = await badge.evaluate_handle('el => el.closest("div[role=\'listitem\']")')
                    await chat_element.as_element().click()
                    await asyncio.sleep(1)

                    # Get sender name
                    sender_element = await self.page.query_selector('header span[dir="auto"]')
                    sender = await sender_element.inner_text() if sender_element else "Unknown"

                    # Get unread messages in this chat
                    message_elements = await self.page.query_selector_all('div[data-testid="msg-container"]')

                    for msg_elem in message_elements[-5:]:  # Last 5 messages
                        try:
                            # Check if message is incoming (not sent by us)
                            is_incoming = await msg_elem.evaluate('el => el.querySelector("div[data-testid=\'msg-container-incoming\']") !== null')

                            if not is_incoming:
                                continue

                            # Get message text
                            text_elem = await msg_elem.query_selector('span.selectable-text')
                            if not text_elem:
                                continue

                            text = await text_elem.inner_text()

                            # Get timestamp
                            time_elem = await msg_elem.query_selector('span[data-testid="msg-meta"]')
                            msg_time = await time_elem.inner_text() if time_elem else "Unknown"

                            # Create unique ID
                            msg_id = f"{sender}_{msg_time}_{hash(text)}"

                            # Check if already processed
                            if msg_id in self.processed_ids:
                                continue

                            # Check for keywords
                            all_keywords = URGENT_KEYWORDS + BUSINESS_KEYWORDS + INQUIRY_KEYWORDS
                            if any(keyword in text.lower() for keyword in all_keywords):
                                messages.append({
                                    'id': msg_id,
                                    'sender': sender,
                                    'text': text,
                                    'time': msg_time,
                                    'chat_type': 'Individual'
                                })

                        except Exception as e:
                            self.log(f"Error processing message: {e}")
                            continue

                except Exception as e:
                    self.log(f"Error processing chat: {e}")
                    continue

            return messages

        except Exception as e:
            self.log(f"Error getting unread messages: {e}")
            return []

    async def check_messages(self):
        """Check for new messages and create tasks"""
        try:
            messages = await self.get_unread_messages()

            if not messages:
                self.log("No new messages with keywords")
                return 0

            new_count = 0
            for msg in messages:
                if self.create_whatsapp_task(msg):
                    self.processed_ids.add(msg['id'])
                    new_count += 1

            if new_count > 0:
                self.save_processed_ids()
                self.log(f"Processed {new_count} new message(s)")

            return new_count

        except Exception as e:
            self.log(f"Error checking messages: {e}")
            return 0

    async def run(self, interval=30):
        """Run watcher continuously"""
        self.log("=" * 60)
        self.log("WhatsApp Watcher Started")
        self.log(f"Check interval: {interval} seconds")
        self.log("=" * 60)

        if not await self.initialize_browser():
            self.log("Browser initialization failed. Exiting.")
            return

        if not await self.login_whatsapp():
            self.log("WhatsApp login failed. Exiting.")
            return

        try:
            while True:
                await self.check_messages()
                await asyncio.sleep(interval)
        except KeyboardInterrupt:
            self.log("Watcher stopped by user")
            if self.context:
                await self.context.close()
            print("\nWhatsApp Watcher stopped.")


async def main():
    """Main entry point"""
    watcher = WhatsAppWatcher()
    await watcher.run(interval=30)  # Check every 30 seconds


if __name__ == "__main__":
    asyncio.run(main())
