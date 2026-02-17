#!/usr/bin/env python3
"""
Demo script to show diagnostic logging in action
Simulates WhatsApp message processing without needing WhatsApp Web
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()

# Configuration
VAULT_PATH = Path("AI_Employee_Vault")
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
LOGS_FOLDER = VAULT_PATH / "Logs"
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Ensure folders exist
NEEDS_ACTION_FOLDER.mkdir(exist_ok=True)
LOGS_FOLDER.mkdir(exist_ok=True)

# Create log files
debug_log = LOGS_FOLDER / "whatsapp_debug.log"
main_log = LOGS_FOLDER / f"whatsapp_watcher_{datetime.now().strftime('%Y%m%d')}.md"

def debug_log_entry(message):
    """Write detailed debug log entry"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    log_entry = f"[{timestamp}] {message}\n"

    with open(debug_log, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(log_entry.strip())

def log(message):
    """Write main log entry"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"

    with open(main_log, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(log_entry.strip())

def determine_priority(message_text):
    """Determine message priority and log keywords"""
    text = message_text.lower()

    URGENT_KEYWORDS = ['urgent', 'asap', 'emergency', 'critical', 'help', 'problem']
    BUSINESS_KEYWORDS = ['pricing', 'quote', 'order', 'payment', 'invoice', 'delivery']
    INQUIRY_KEYWORDS = ['question', 'inquiry', 'information', 'details', 'available']

    # Check for urgent keywords
    urgent_matches = [kw for kw in URGENT_KEYWORDS if kw in text]
    if urgent_matches:
        debug_log_entry(f"PRIORITY: P0 - Critical | Keywords: {', '.join(urgent_matches)}")
        return 'P0 - Critical', urgent_matches

    # Check for business keywords
    business_matches = [kw for kw in BUSINESS_KEYWORDS if kw in text]
    if business_matches:
        debug_log_entry(f"PRIORITY: P1 - High | Keywords: {', '.join(business_matches)}")
        return 'P1 - High', business_matches

    # Check for inquiry keywords
    inquiry_matches = [kw for kw in INQUIRY_KEYWORDS if kw in text]
    if inquiry_matches:
        debug_log_entry(f"PRIORITY: P2 - Medium | Keywords: {', '.join(inquiry_matches)}")
        return 'P2 - Medium', inquiry_matches

    debug_log_entry("PRIORITY: P2 - Medium | Keywords: None matched")
    return 'P2 - Medium', []

def simulate_message_processing(sender, message_text, msg_time):
    """Simulate processing a WhatsApp message"""

    debug_log_entry(f"\n{'='*60}")
    debug_log_entry(f"MESSAGE RECEIVED:")
    debug_log_entry(f"  Sender: {sender}")
    debug_log_entry(f"  Time: {msg_time}")
    debug_log_entry(f"  Text: {message_text[:100]}...")
    debug_log_entry(f"  Message ID: test_{hash(message_text) % 10000}")

    # Determine priority
    priority, keywords = determine_priority(message_text)

    # Check API key
    if ANTHROPIC_API_KEY and ANTHROPIC_API_KEY != "your_anthropic_api_key_here":
        debug_log_entry(f"API Key Status: LOADED (ready for AI generation)")
        ai_draft_status = "Would generate AI draft"
    else:
        debug_log_entry(f"API Key Status: NOT SET - Skipping AI generation")
        ai_draft_status = "Not Available"

    # Simulate file creation
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    safe_sender = "".join(c if c.isalnum() or c in ('-', '_') else '_' for c in sender[:30])
    filename = f"whatsapp_{safe_sender}_{timestamp}.md"

    debug_log_entry(f"Creating file: {NEEDS_ACTION_FOLDER / filename}")
    debug_log_entry(f"✅ FILE WOULD BE CREATED")
    debug_log_entry(f"   Location: {NEEDS_ACTION_FOLDER / filename}")
    debug_log_entry(f"   Priority: {priority}")
    debug_log_entry(f"   AI Draft: {ai_draft_status}")
    debug_log_entry(f"{'='*60}\n")

    # Console output
    print(f"\n{'='*60}")
    print(f"📱 MESSAGE RECEIVED: {sender}")
    print(f"📝 Message: {message_text[:80]}...")
    print(f"⚡ Priority: {priority}")
    print(f"🔑 Keywords: {', '.join(keywords) if keywords else 'None'}")
    print(f"🤖 AI Draft: {ai_draft_status}")
    print(f"📄 File: {filename}")
    print(f"{'='*60}\n")

def main():
    """Run diagnostic logging demo"""
    print("\n" + "="*60)
    print("WhatsApp Watcher - Diagnostic Logging Demo")
    print("="*60 + "\n")

    # Check API key status
    log("=== Diagnostic Logging Demo Started ===")
    debug_log_entry("=== WhatsApp Watcher Diagnostic Demo ===")

    if ANTHROPIC_API_KEY and ANTHROPIC_API_KEY != "your_anthropic_api_key_here":
        log(f"✅ ANTHROPIC_API_KEY loaded (length: {len(ANTHROPIC_API_KEY)})")
        debug_log_entry(f"API Key Status: LOADED (starts with: {ANTHROPIC_API_KEY[:10]}...)")
        print(f"✅ API Key: LOADED ({len(ANTHROPIC_API_KEY)} chars)")
    else:
        log("❌ ANTHROPIC_API_KEY NOT SET - AI draft replies will be disabled")
        debug_log_entry("API Key Status: NOT SET - Check .env file")
        print("❌ API Key: NOT SET (add to .env file)")

    print("\n" + "="*60)
    print("Simulating Message Processing")
    print("="*60 + "\n")

    # Test messages
    test_messages = [
        {
            "sender": "John Doe",
            "text": "Hi, I need urgent pricing for 100 units of your product. Can you help?",
            "time": "14:30"
        },
        {
            "sender": "Sarah Smith",
            "text": "Can you help me with mobile payment setup?",
            "time": "14:32"
        },
        {
            "sender": "Ahmed Khan",
            "text": "URGENT: Payment issue with invoice #12345. Need immediate help!",
            "time": "14:35"
        },
        {
            "sender": "Lisa Wong",
            "text": "Hey, just checking in. How are things?",
            "time": "14:40"
        }
    ]

    for i, msg in enumerate(test_messages, 1):
        print(f"\n--- Test Message {i}/{len(test_messages)} ---")
        simulate_message_processing(msg["sender"], msg["text"], msg["time"])

        if i < len(test_messages):
            print("Waiting for next message...\n")

    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60)
    print("\nCheck the logs:")
    print(f"1. Main Log: {main_log}")
    print(f"2. Debug Log: {debug_log}")
    print("\nTo view debug log in real-time:")
    print(f'   tail -f "{debug_log}"')
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
