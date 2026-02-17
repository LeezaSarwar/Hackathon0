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
import anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
VAULT_PATH = Path(__file__).parent
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
LOGS_FOLDER = VAULT_PATH / "Logs"
SESSION_FILE = VAULT_PATH / "whatsapp_session.json"
PROCESSED_IDS_FILE = VAULT_PATH / "processed_whatsapp.json"
COMPANY_HANDBOOK = VAULT_PATH / "Company_Handbook.md"
WHATSAPP_SKILL = VAULT_PATH / "Skills" / "whatsapp_response_skill.md"

# API Configuration
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

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
        self.debug_log = LOGS_FOLDER / "whatsapp_debug.log"
        self.session_dir = VAULT_PATH / "whatsapp_session_data"
        self.session_dir.mkdir(exist_ok=True)
        self.log("WhatsApp Watcher initialized")
        self.debug_log_entry("=== WhatsApp Watcher Session Started ===")

        # Check API key status
        if ANTHROPIC_API_KEY:
            self.log(f"✅ ANTHROPIC_API_KEY loaded (length: {len(ANTHROPIC_API_KEY)})")
            self.debug_log_entry(f"API Key Status: LOADED (starts with: {ANTHROPIC_API_KEY[:10]}...)")
        else:
            self.log("❌ ANTHROPIC_API_KEY NOT SET - AI draft replies will be disabled")
            self.debug_log_entry("API Key Status: NOT SET - Check .env file")

    def log(self, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            # If logging fails, just print to console
            pass

        print(log_entry.strip())

    def debug_log_entry(self, message):
        """Write detailed debug log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        log_entry = f"[{timestamp}] {message}\n"

        try:
            with open(self.debug_log, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception:
            # If debug logging fails, silently continue
            pass

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
        matched_keywords = []

        # Check for urgent keywords
        urgent_matches = [kw for kw in URGENT_KEYWORDS if kw in text]
        if urgent_matches:
            matched_keywords.extend(urgent_matches)
            self.debug_log_entry(f"PRIORITY: P0 - Critical | Keywords: {', '.join(urgent_matches)}")
            return 'P0 - Critical'

        # Check for business keywords
        business_matches = [kw for kw in BUSINESS_KEYWORDS if kw in text]
        if business_matches:
            matched_keywords.extend(business_matches)
            self.debug_log_entry(f"PRIORITY: P1 - High | Keywords: {', '.join(business_matches)}")
            return 'P1 - High'

        # Check for inquiry keywords
        inquiry_matches = [kw for kw in INQUIRY_KEYWORDS if kw in text]
        if inquiry_matches:
            matched_keywords.extend(inquiry_matches)
            self.debug_log_entry(f"PRIORITY: P2 - Medium | Keywords: {', '.join(inquiry_matches)}")
            return 'P2 - Medium'

        self.debug_log_entry("PRIORITY: P2 - Medium | Keywords: None matched")
        return 'P2 - Medium'

    def generate_draft_reply(self, message_data, priority):
        """Generate AI draft reply using Claude"""
        try:
            # Check if API key is available
            if not ANTHROPIC_API_KEY:
                self.log("[WARNING] ANTHROPIC_API_KEY not set - skipping AI draft generation")
                return None

            # Read Company Handbook for context
            handbook_content = ""
            if COMPANY_HANDBOOK.exists():
                with open(COMPANY_HANDBOOK, 'r', encoding='utf-8') as f:
                    handbook_content = f.read()

            # Read WhatsApp skill templates
            skill_content = ""
            if WHATSAPP_SKILL.exists():
                with open(WHATSAPP_SKILL, 'r', encoding='utf-8') as f:
                    skill_content = f.read()

            # Initialize Claude client
            client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

            # Create prompt for Claude
            prompt = f"""Draft a professional WhatsApp reply for a business to send to this customer message.

**Customer Message:**
From: {message_data['sender']}
Priority: {priority}
Message: {message_data['text']}

**Company Context:**
{handbook_content[:1000] if handbook_content else "General business communication"}

**Your Task:**
Write a draft WhatsApp reply that a business representative could send. This is a DRAFT that will be reviewed by a human before sending.

**Guidelines:**
1. **Tone:** Professional, warm, and conversational (WhatsApp style)
2. **Length:** 2-4 short paragraphs maximum
3. **Emojis:** Use 1-2 appropriate emojis for friendliness
4. **Content:**
   - Acknowledge their message
   - Address their specific concern or question
   - Provide helpful information or next steps
   - Ask clarifying questions if needed
5. **Urgency Level ({priority}):**
   - P0 (Critical): Express immediate attention, offer quick resolution
   - P1 (High): Show attentiveness, provide clear timeline
   - P2 (Medium): Be thorough and helpful
6. **Closing:** End with a clear question or call to action

**Example for urgent pricing request:**
"Hi! Thanks for reaching out! 👋

I'd be happy to help with pricing for 100 units. To give you the most accurate quote, could you let me know:
- Which product model you need
- Your preferred delivery timeline
- Any specific requirements

I'll get you a detailed quote within the hour. Sound good?"

**Now write the draft reply for the customer message above:**"""

            # Call Claude API
            self.log("[AI] Generating AI draft reply...")
            self.debug_log_entry("Calling Claude API...")
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=500,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            draft_reply = message.content[0].text.strip()
            self.log("✅ [OK] AI draft reply generated successfully")
            self.debug_log_entry(f"✅ AI Draft Generated (length: {len(draft_reply)} chars)")
            self.debug_log_entry(f"Draft preview: {draft_reply[:100]}...")
            return draft_reply

        except Exception as e:
            self.log(f"⚠️ [WARNING] Error generating AI draft reply: {e}")
            self.debug_log_entry(f"⚠️ AI Generation Failed: {e}")
            return None

    def create_whatsapp_task(self, message_data):
        """Create task file for WhatsApp message"""
        try:
            self.debug_log_entry(f"\n{'='*60}")
            self.debug_log_entry(f"MESSAGE RECEIVED:")
            self.debug_log_entry(f"  Sender: {message_data['sender']}")
            self.debug_log_entry(f"  Time: {message_data['time']}")
            self.debug_log_entry(f"  Text: {message_data['text'][:100]}...")
            self.debug_log_entry(f"  Message ID: {message_data['id']}")

            priority = self.determine_priority(
                message_data['text'],
                message_data['sender']
            )

            # Generate AI draft reply
            self.debug_log_entry(f"Attempting to generate AI draft reply...")
            draft_reply = self.generate_draft_reply(message_data, priority)

            # Generate task filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_sender = "".join(c if c.isalnum() or c in ('-', '_') else '_'
                                 for c in message_data['sender'][:30])
            task_filename = f"whatsapp_{safe_sender}_{timestamp}.md"
            task_path = NEEDS_ACTION_FOLDER / task_filename

            # Build AI draft section
            ai_draft_section = ""
            if draft_reply:
                ai_draft_section = f"""## AI-Generated Draft Reply

**Status:** Ready for Review
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

```
{draft_reply}
```

**IMPORTANT:** This is an AI-generated draft. Please review and modify as needed before sending.

**Approval Required:** {'Yes - New contact or sensitive' if priority in ['P0 - Critical', 'P1 - High'] else 'Review recommended'}

---

"""
            else:
                ai_draft_section = """## AI-Generated Draft Reply

**Status:** Not Available
**Reason:** API key not configured or generation failed

*Please draft reply manually using templates below*

---

"""

            # Create task content
            task_content = f"""# WhatsApp Message: {message_data['sender']}

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Priority:** {priority}
**Status:** Pending
**Source:** WhatsApp Watcher

---

## Message Details

- **From:** {message_data['sender']}
- **Received:** {message_data['time']}
- **Message ID:** `{message_data['id']}`
- **Chat Type:** {message_data.get('chat_type', 'Unknown')}

---

## Message Content

```
{message_data['text']}
```

---

{ai_draft_section}

## Suggested Actions

- [ ] Read and analyze message
- [ ] Determine appropriate response
- [ ] Check Company_Handbook for response templates
- [ ] Draft reply
- [ ] Get approval if needed (new contact or sensitive)
- [ ] Send response via WhatsApp
- [ ] Update Dashboard

---

## Response Guidelines

Based on priority level **{priority}**:

- If **P0 (Critical)**: Respond within 30 minutes
- If **P1 (High)**: Respond within 2 hours
- If **P2 (Medium)**: Respond within 4 hours
- If **P3 (Low)**: Respond within 24 hours

---

## Response Template Suggestions

### For Pricing Inquiries:
"Thank you for your interest! I'd be happy to provide a quote. Could you share more details about [specific requirements]?"

### For Urgent Issues:
"I understand this is urgent. Let me look into this immediately and get back to you within [timeframe]."

### For General Inquiries:
"Thanks for reaching out! [Answer their question]. Is there anything else I can help you with?"

---

## Notes

*Add analysis and response notes here*

---

## Completion Checklist

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
            self.debug_log_entry(f"Creating file: {task_path}")
            with open(task_path, 'w', encoding='utf-8') as f:
                f.write(task_content)

            self.log(f"✅ Created task: {task_filename}")
            self.debug_log_entry(f"✅ FILE CREATED SUCCESSFULLY: {task_filename}")
            self.debug_log_entry(f"   Location: {task_path}")
            self.debug_log_entry(f"   Priority: {priority}")
            self.debug_log_entry(f"   AI Draft: {'YES' if draft_reply else 'NO'}")
            self.debug_log_entry(f"{'='*60}\n")

            # Console output for user
            print(f"\n{'='*60}")
            print(f"📱 MESSAGE RECEIVED: {message_data['sender']}")
            print(f"📝 Message: {message_data['text'][:80]}...")
            print(f"⚡ Priority: {priority}")
            print(f"🤖 AI Draft: {'Generated' if draft_reply else 'Not Available'}")
            print(f"📄 File: {task_filename}")
            print(f"{'='*60}\n")

            return True

        except Exception as e:
            self.log(f"❌ Error creating WhatsApp task: {e}")
            self.debug_log_entry(f"❌ ERROR creating task: {e}")
            self.debug_log_entry(f"{'='*60}\n")
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
            await self.page.goto('https://web.whatsapp.com', wait_until='domcontentloaded')
            await asyncio.sleep(3)

            # Try multiple selectors to detect if logged in
            login_selectors = [
                'div[data-testid="chat-list"]',
                '#pane-side',
                'div[id="side"]',
                'div._2Ts6i',
                '[aria-label="Chat list"]'
            ]

            # Check if already logged in
            self.log("Checking login status...")
            for selector in login_selectors:
                try:
                    await self.page.wait_for_selector(selector, timeout=5000)
                    self.log(f"✅ Already logged in (detected via: {selector})")
                    return True
                except:
                    continue

            # Not logged in, wait for QR scan
            self.log("=" * 60)
            self.log("🔐 NOT LOGGED IN - QR CODE SCAN REQUIRED")
            self.log("=" * 60)
            self.log("1. Look at the browser window that opened")
            self.log("2. Scan the QR code with your WhatsApp mobile app")
            self.log("3. Wait for the chat list to appear")
            self.log("=" * 60)
            self.log("Waiting for login (up to 5 minutes)...")

            # Wait for login with multiple attempts
            max_attempts = 60  # 5 minutes (5 second intervals)
            for attempt in range(max_attempts):
                await asyncio.sleep(5)

                # Try each selector
                for selector in login_selectors:
                    try:
                        element = await self.page.query_selector(selector)
                        if element:
                            self.log(f"✅ LOGIN SUCCESSFUL! (detected via: {selector})")
                            self.log("WhatsApp Web is now connected!")
                            self.log("Starting message monitoring...")
                            await asyncio.sleep(2)  # Give it time to fully load
                            return True
                    except:
                        continue

                # Progress indicator every 30 seconds
                if (attempt + 1) % 6 == 0:
                    elapsed = (attempt + 1) * 5
                    self.log(f"Still waiting for login... ({elapsed} seconds elapsed)")

            self.log("❌ Login timeout - QR code was not scanned in time")
            return False

        except Exception as e:
            self.log(f"Error during WhatsApp login: {e}")
            self.debug_log_entry(f"Login error details: {e}")
            return False

    async def get_unread_messages(self):
        """Fetch unread messages from WhatsApp Web"""
        try:
            print("\n" + "="*70)
            print("🔍 CHECKING FOR MESSAGES...")
            print("="*70)
            self.debug_log_entry("Starting message check...")

            # First, try to dismiss any popups/overlays
            try:
                # Look for "Get WhatsApp for Windows" or other popups
                popup_selectors = [
                    'div[data-testid="popup-controls-ok"]',
                    'button[aria-label="Close"]',
                    'div[data-animate-modal-popup="true"]'
                ]
                for selector in popup_selectors:
                    popup = await self.page.query_selector(selector)
                    if popup:
                        await popup.click()
                        await asyncio.sleep(1)
                        print("✓ Dismissed popup")
                        break
            except:
                pass

            # ALWAYS check first 10 chats, regardless of unread status
            chat_list_selectors = [
                'div[role="listitem"]',
                'div[data-testid="cell-frame-container"]',
                'div[id="pane-side"] > div > div > div',
            ]

            all_chats = []
            for selector in chat_list_selectors:
                all_chats = await self.page.query_selector_all(selector)
                if all_chats and len(all_chats) > 0:
                    print(f"✅ Found {len(all_chats)} chats using: {selector}")
                    self.debug_log_entry(f"Found {len(all_chats)} chats using: {selector}")
                    break

            if not all_chats:
                print("❌ No chats found!")
                self.debug_log_entry("No chats found at all")
                return []

            messages = []
            chats_to_check = min(10, len(all_chats))  # Check up to 10 chats
            print(f"\n📋 Will check first {chats_to_check} chats...")

            for idx in range(chats_to_check):
                try:
                    chat_elem = all_chats[idx]
                    print(f"\n--- Chat {idx + 1}/{chats_to_check} ---")
                    self.debug_log_entry(f"Processing chat {idx + 1}...")

                    # Click on the chat with force option to bypass overlays
                    try:
                        await chat_elem.click(timeout=5000, force=True)
                    except:
                        # If force click fails, try JavaScript click
                        await chat_elem.evaluate('element => element.click()')

                    await asyncio.sleep(2)

                    # Get sender name
                    sender = "Unknown"
                    sender_selectors = [
                        'header span[dir="auto"]',
                        'header span[title]',
                        'div[data-testid="conversation-header"] span',
                        'header h1'
                    ]

                    for selector in sender_selectors:
                        try:
                            sender_element = await self.page.query_selector(selector)
                            if sender_element:
                                sender = await sender_element.inner_text()
                                if sender and len(sender) > 0:
                                    print(f"👤 Sender: {sender}")
                                    self.debug_log_entry(f"Chat with: {sender}")
                                    break
                        except:
                            continue

                    # Wait a bit for messages to load
                    await asyncio.sleep(1)

                    # Get all messages in this chat - try multiple selectors
                    message_elements = []
                    message_selectors = [
                        'div[data-testid="msg-container"]',
                        'div.message-in',
                        'div[class*="message"]',
                        'div[role="row"]'
                    ]

                    for msg_selector in message_selectors:
                        message_elements = await self.page.query_selector_all(msg_selector)
                        if message_elements and len(message_elements) > 0:
                            print(f"   📨 Found {len(message_elements)} messages using: {msg_selector}")
                            self.debug_log_entry(f"Found {len(message_elements)} messages using: {msg_selector}")
                            break

                    if not message_elements:
                        print(f"   ⚠️ No messages found in this chat")
                        self.debug_log_entry("No messages found in this chat")
                        continue

                    # Check last 5 messages (increased from 3)
                    messages_to_check = message_elements[-5:]
                    print(f"   🔎 Checking last {len(messages_to_check)} messages...")

                    for msg_idx, msg_elem in enumerate(messages_to_check):
                        try:
                            # Get message text - try multiple selectors
                            text = None
                            text_selectors = [
                                'span.selectable-text',
                                'div.selectable-text',
                                'span[dir="ltr"]',
                                'div[class*="copyable-text"] span',
                                'span[class*="selectable"]'
                            ]

                            for text_selector in text_selectors:
                                try:
                                    text_elem = await msg_elem.query_selector(text_selector)
                                    if text_elem:
                                        text = await text_elem.inner_text()
                                        if text and text.strip():
                                            break
                                except:
                                    continue

                            if not text or not text.strip():
                                print(f"      Message {msg_idx + 1}: [No text found]")
                                continue

                            print(f"      Message {msg_idx + 1}: {text[:60]}...")
                            self.debug_log_entry(f"Message text: {text[:100]}...")

                            # Get timestamp
                            msg_time = datetime.now().strftime('%H:%M')

                            # Create unique ID
                            msg_id = f"{sender}_{msg_time}_{hash(text)}"

                            # Check if already processed
                            if msg_id in self.processed_ids:
                                print(f"         ⏭️ Already processed")
                                self.debug_log_entry(f"Message already processed")
                                continue

                            # Check for keywords
                            all_keywords = URGENT_KEYWORDS + BUSINESS_KEYWORDS + INQUIRY_KEYWORDS
                            matched_keywords = [kw for kw in all_keywords if kw in text.lower()]

                            if matched_keywords:
                                print(f"         ✅ KEYWORDS MATCHED: {', '.join(matched_keywords)}")
                                print(f"         🎯 This message will be processed!")
                                self.debug_log_entry(f"✅ MATCH! Keywords: {matched_keywords}")

                                messages.append({
                                    'id': msg_id,
                                    'sender': sender,
                                    'text': text,
                                    'time': msg_time,
                                    'chat_type': 'Individual'
                                })
                            else:
                                print(f"         ❌ No keywords found")
                                self.debug_log_entry(f"No keywords matched")

                        except Exception as e:
                            print(f"      ⚠️ Error reading message: {e}")
                            self.debug_log_entry(f"Error processing message: {e}")
                            continue

                except Exception as e:
                    print(f"   ⚠️ Error processing chat: {e}")
                    self.debug_log_entry(f"Error processing chat {idx + 1}: {e}")
                    continue

            print(f"\n{'='*70}")
            print(f"📊 RESULT: Found {len(messages)} message(s) with keywords")
            print(f"{'='*70}\n")
            self.debug_log_entry(f"Total messages found with keywords: {len(messages)}")
            return messages

        except Exception as e:
            print(f"\n❌ ERROR: {e}")
            self.log(f"Error getting unread messages: {e}")
            self.debug_log_entry(f"Critical error in get_unread_messages: {e}")
            return []

    async def check_messages(self):
        """Check for new messages and create tasks"""
        try:
            self.log("🔍 Checking for new messages...")
            self.debug_log_entry(f"\n{'='*60}")
            self.debug_log_entry(f"MESSAGE CHECK CYCLE - {datetime.now().strftime('%H:%M:%S')}")
            self.debug_log_entry(f"Keywords being monitored:")
            self.debug_log_entry(f"  Urgent: {', '.join(URGENT_KEYWORDS)}")
            self.debug_log_entry(f"  Business: {', '.join(BUSINESS_KEYWORDS)}")
            self.debug_log_entry(f"  Inquiry: {', '.join(INQUIRY_KEYWORDS)}")
            self.debug_log_entry(f"{'='*60}")

            messages = await self.get_unread_messages()

            if not messages:
                self.log("✓ No new messages with keywords found")
                self.debug_log_entry("Check complete - no matching messages")
                return 0

            self.log(f"📬 Found {len(messages)} new message(s) with keywords!")
            new_count = 0
            for msg in messages:
                if self.create_whatsapp_task(msg):
                    self.processed_ids.add(msg['id'])
                    new_count += 1

            if new_count > 0:
                self.save_processed_ids()
                self.log(f"✅ Successfully processed {new_count} new message(s)")

            return new_count

        except Exception as e:
            self.log(f"❌ Error checking messages: {e}")
            self.debug_log_entry(f"ERROR in check_messages: {e}")
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
