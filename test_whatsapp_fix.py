#!/usr/bin/env python3
"""
Test script to verify WhatsApp watcher fixes and generate AI draft responses
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import anthropic
from datetime import datetime

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()

# Configuration
VAULT_PATH = Path("AI_Employee_Vault")
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
LOGS_FOLDER = VAULT_PATH / "Logs"
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

def test_api_key():
    """Test if API key is loaded"""
    print("="*60)
    print("STEP 1: Testing API Key Loading")
    print("="*60)

    if ANTHROPIC_API_KEY and ANTHROPIC_API_KEY != "your_anthropic_api_key_here":
        print(f"✅ API Key loaded successfully")
        print(f"   Length: {len(ANTHROPIC_API_KEY)} characters")
        print(f"   Starts with: {ANTHROPIC_API_KEY[:10]}...")
        return True
    else:
        print("❌ API Key NOT loaded or still has placeholder value")
        print(f"   Current value: {ANTHROPIC_API_KEY}")
        print("\n⚠️  ACTION REQUIRED:")
        print("   1. Get your API key from: https://console.anthropic.com/")
        print("   2. Edit .env file and replace 'your_anthropic_api_key_here'")
        print("   3. Run this test again")
        return False

def generate_draft_reply(message_text, sender, priority):
    """Generate AI draft reply using Claude"""
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        prompt = f"""You are an AI assistant helping to draft WhatsApp message replies.

**Message Details:**
- From: {sender}
- Priority: {priority}

**Message Content:**
{message_text}

**Task:**
Draft a professional, friendly WhatsApp reply to this message. Follow these guidelines:
1. Keep it concise and conversational (WhatsApp style)
2. Use appropriate emojis (1-2 max)
3. Address the sender's concern directly
4. Match the priority level urgency
5. End with a clear next step or question
6. Use line breaks for readability

**Draft Reply:**"""

        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return message.content[0].text.strip()

    except Exception as e:
        print(f"   ❌ Error generating draft: {e}")
        return None

def process_existing_files():
    """Process existing WhatsApp message files and add AI drafts"""
    print("\n" + "="*60)
    print("STEP 2: Processing Existing WhatsApp Messages")
    print("="*60)

    whatsapp_files = list(NEEDS_ACTION_FOLDER.glob("whatsapp_*.md"))

    if not whatsapp_files:
        print("No WhatsApp message files found in Needs_Action folder")
        return

    print(f"Found {len(whatsapp_files)} WhatsApp message file(s)\n")

    for file_path in whatsapp_files:
        print(f"\n📄 Processing: {file_path.name}")
        print("-" * 60)

        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has AI draft
        if "**Status:** Ready for Review" in content:
            print("   ✅ Already has AI draft - skipping")
            continue

        # Extract message details
        sender = None
        message_text = None
        priority = None

        for line in content.split('\n'):
            if line.startswith('# WhatsApp Message:'):
                sender = line.replace('# WhatsApp Message:', '').strip()
            elif line.startswith('**Priority:**'):
                priority = line.replace('**Priority:**', '').strip()
            elif '```' in line and message_text is None:
                # Start of message content
                idx = content.find('## Message Content')
                if idx != -1:
                    start = content.find('```', idx) + 3
                    end = content.find('```', start)
                    message_text = content[start:end].strip()

        if not sender or not message_text:
            print("   ⚠️  Could not extract message details - skipping")
            continue

        print(f"   Sender: {sender}")
        print(f"   Priority: {priority}")
        print(f"   Message: {message_text[:60]}...")

        # Generate AI draft
        print(f"   🤖 Generating AI draft reply...")
        draft_reply = generate_draft_reply(message_text, sender, priority)

        if not draft_reply:
            print("   ❌ Failed to generate draft")
            continue

        print(f"   ✅ Draft generated ({len(draft_reply)} chars)")

        # Update the file with AI draft
        new_ai_section = f"""## AI-Generated Draft Reply

**Status:** Ready for Review
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

```
{draft_reply}
```

**IMPORTANT:** This is an AI-generated draft. Please review and modify as needed before sending.

**Approval Required:** {'Yes - New contact or sensitive' if priority in ['P0 - Critical', 'P1 - High'] else 'Review recommended'}

---

"""

        # Replace the old AI section
        old_section_start = content.find("## AI-Generated Draft Reply")
        old_section_end = content.find("## Suggested Actions")

        if old_section_start != -1 and old_section_end != -1:
            new_content = content[:old_section_start] + new_ai_section + content[old_section_end:]

            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"   ✅ File updated with AI draft")
        else:
            print("   ⚠️  Could not find section markers - skipping update")

def main():
    """Main test function"""
    print("\n" + "="*60)
    print("WhatsApp Watcher Fix Test")
    print("="*60 + "\n")

    # Test API key
    if not test_api_key():
        print("\n❌ Test failed: API key not configured")
        return

    # Process existing files
    process_existing_files()

    print("\n" + "="*60)
    print("✅ Test Complete!")
    print("="*60)
    print("\nNext Steps:")
    print("1. Check AI_Employee_Vault/Needs_Action/ for updated files")
    print("2. Review the AI-generated draft replies")
    print("3. Run the WhatsApp watcher with: python AI_Employee_Vault/whatsapp_watcher.py")
    print("4. Send test messages with keywords: urgent, help, pricing")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
