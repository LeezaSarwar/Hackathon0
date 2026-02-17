#!/usr/bin/env python3
"""
Quick test script for WhatsApp AI draft reply feature
Tests the draft generation without needing actual WhatsApp connection
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Add AI_Employee_Vault to path
sys.path.insert(0, str(Path(__file__).parent / "AI_Employee_Vault"))

from whatsapp_watcher import WhatsAppWatcher

def test_draft_generation():
    """Test AI draft reply generation"""

    print("=" * 60)
    print("WhatsApp AI Draft Reply - Test Script")
    print("=" * 60)
    print()

    # Check API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("[X] ANTHROPIC_API_KEY not set!")
        print()
        print("To set it:")
        print("  Windows PowerShell: $env:ANTHROPIC_API_KEY='your-key'")
        print("  Windows CMD: set ANTHROPIC_API_KEY=your-key")
        print()
        print("[!] Test will continue but AI draft generation will be skipped")
        print()
    else:
        print(f"[OK] API Key found: {api_key[:20]}...")
        print()

    # Create watcher instance
    print("Creating WhatsApp Watcher instance...")
    watcher = WhatsAppWatcher()
    print("[OK] Watcher initialized")
    print()

    # Test message data
    test_messages = [
        {
            'id': 'test_001',
            'sender': 'John Doe',
            'text': 'Hi, I need urgent pricing for 100 units of your product. Can you help?',
            'time': datetime.now().strftime('%H:%M'),
            'chat_type': 'Individual'
        },
        {
            'id': 'test_002',
            'sender': 'Sarah Smith',
            'text': 'Hello, I have a question about delivery times for orders to Karachi.',
            'time': datetime.now().strftime('%H:%M'),
            'chat_type': 'Individual'
        },
        {
            'id': 'test_003',
            'sender': 'Ahmed Khan',
            'text': 'URGENT: Payment issue with invoice #12345. Need immediate help!',
            'time': datetime.now().strftime('%H:%M'),
            'chat_type': 'Individual'
        }
    ]

    print("=" * 60)
    print("Testing Draft Reply Generation")
    print("=" * 60)
    print()

    for i, msg_data in enumerate(test_messages, 1):
        print(f"\n{'='*60}")
        print(f"Test Message {i}/{len(test_messages)}")
        print(f"{'='*60}")
        print(f"From: {msg_data['sender']}")
        print(f"Message: {msg_data['text']}")
        print()

        # Determine priority
        priority = watcher.determine_priority(msg_data['text'], msg_data['sender'])
        print(f"Priority: {priority}")
        print()

        # Generate draft reply
        if api_key:
            print("[AI] Generating AI draft reply...")
            draft = watcher.generate_draft_reply(msg_data, priority)

            if draft:
                print("[OK] Draft generated successfully!")
                print()
                print("Draft Reply:")
                print("-" * 60)
                print(draft)
                print("-" * 60)
            else:
                print("[X] Draft generation failed")
        else:
            print("[!] Skipping AI draft (no API key)")

        print()

        # Create task file
        print("Creating task file...")
        if watcher.create_whatsapp_task(msg_data):
            print("[OK] Task file created successfully!")
        else:
            print("[X] Task file creation failed")

        print()

    print("=" * 60)
    print("Test Complete!")
    print("=" * 60)
    print()
    print("Check the following locations:")
    print(f"  - Task files: AI_Employee_Vault/Needs_Action/")
    print(f"  - Log file: AI_Employee_Vault/Logs/whatsapp_watcher_{datetime.now().strftime('%Y%m%d')}.md")
    print()

if __name__ == "__main__":
    try:
        test_draft_generation()
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
    except Exception as e:
        print(f"\n[X] Error during test: {e}")
        import traceback
        traceback.print_exc()
