#!/usr/bin/env python3
"""
Regenerate AI drafts with the fixed prompt
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import anthropic
from datetime import datetime

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables
load_dotenv()

# Configuration
VAULT_PATH = Path("AI_Employee_Vault")
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

def generate_draft_reply(message_text, sender, priority):
    """Generate AI draft reply using Claude with fixed prompt"""
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        prompt = f"""Draft a professional WhatsApp reply for a business to send to this customer message.

**Customer Message:**
From: {sender}
Priority: {priority}
Message: {message_text}

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

def regenerate_all_drafts():
    """Regenerate AI drafts for all WhatsApp message files"""
    print("\n" + "="*60)
    print("Regenerating AI Drafts with Fixed Prompt")
    print("="*60 + "\n")

    whatsapp_files = list(NEEDS_ACTION_FOLDER.glob("whatsapp_*.md"))

    if not whatsapp_files:
        print("No WhatsApp message files found")
        return

    print(f"Found {len(whatsapp_files)} WhatsApp message file(s)\n")

    for file_path in whatsapp_files:
        print(f"\n📄 Processing: {file_path.name}")
        print("-" * 60)

        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

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

        # Generate NEW AI draft
        print(f"   🤖 Generating NEW AI draft reply...")
        draft_reply = generate_draft_reply(message_text, sender, priority)

        if not draft_reply:
            print("   ❌ Failed to generate draft")
            continue

        print(f"   ✅ Draft generated ({len(draft_reply)} chars)")

        # Create new AI section
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

            print(f"   ✅ File updated with NEW AI draft")
        else:
            print("   ⚠️  Could not find section markers - skipping update")

    print("\n" + "="*60)
    print("✅ Regeneration Complete!")
    print("="*60)
    print("\nCheck the files in AI_Employee_Vault/Needs_Action/")
    print("The AI drafts should now be proper business responses.")
    print("="*60 + "\n")

if __name__ == "__main__":
    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == "your_anthropic_api_key_here":
        print("❌ API key not configured")
        sys.exit(1)

    regenerate_all_drafts()
