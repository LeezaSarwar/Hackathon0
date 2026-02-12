#!/usr/bin/env python3
"""
Gmail Watcher for AI Employee
Monitors Gmail inbox for important emails and creates tasks
"""

import os
import time
import json
import pickle
from datetime import datetime
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Configuration
VAULT_PATH = Path(__file__).parent
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
LOGS_FOLDER = VAULT_PATH / "Logs"
CREDENTIALS_FILE = VAULT_PATH / "gmail_credentials.json"
TOKEN_FILE = VAULT_PATH / "gmail_token.pickle"
PROCESSED_IDS_FILE = VAULT_PATH / "processed_emails.json"

# Keywords to monitor
URGENT_KEYWORDS = ['urgent', 'asap', 'critical', 'emergency', 'immediate']
IMPORTANT_KEYWORDS = ['invoice', 'payment', 'quote', 'proposal', 'contract', 'deadline']
BUSINESS_KEYWORDS = ['meeting', 'call', 'demo', 'presentation', 'review']

# Ensure folders exist
NEEDS_ACTION_FOLDER.mkdir(exist_ok=True)
LOGS_FOLDER.mkdir(exist_ok=True)


class GmailWatcher:
    """Gmail monitoring and task creation"""

    def __init__(self):
        self.service = None
        self.processed_ids = self.load_processed_ids()
        self.log_file = LOGS_FOLDER / f"gmail_watcher_{datetime.now().strftime('%Y%m%d')}.md"
        self.log("Gmail Watcher initialized")

    def log(self, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        print(log_entry.strip())

    def load_processed_ids(self):
        """Load list of already processed email IDs"""
        if PROCESSED_IDS_FILE.exists():
            try:
                with open(PROCESSED_IDS_FILE, 'r') as f:
                    return set(json.load(f))
            except Exception as e:
                self.log(f"Error loading processed IDs: {e}")
                return set()
        return set()

    def save_processed_ids(self):
        """Save processed email IDs to file"""
        try:
            with open(PROCESSED_IDS_FILE, 'w') as f:
                json.dump(list(self.processed_ids), f)
        except Exception as e:
            self.log(f"Error saving processed IDs: {e}")

    def authenticate(self):
        """Authenticate with Gmail API"""
        creds = None

        # Load existing token
        if TOKEN_FILE.exists():
            with open(TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)

        # If no valid credentials, authenticate
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                self.log("Refreshing expired credentials...")
                creds.refresh(Request())
            else:
                if not CREDENTIALS_FILE.exists():
                    self.log("ERROR: gmail_credentials.json not found!")
                    self.log("Please download OAuth credentials from Google Cloud Console")
                    self.log("Visit: https://console.cloud.google.com/apis/credentials")
                    return False

                self.log("Starting OAuth flow...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(CREDENTIALS_FILE), SCOPES)
                creds = flow.run_local_server(port=0)

            # Save credentials
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)

            self.log("Authentication successful")

        try:
            self.service = build('gmail', 'v1', credentials=creds)
            return True
        except Exception as e:
            self.log(f"Error building Gmail service: {e}")
            return False

    def determine_priority(self, subject, snippet, sender):
        """Determine email priority based on content"""
        text = f"{subject} {snippet}".lower()

        # Check for urgent keywords
        if any(keyword in text for keyword in URGENT_KEYWORDS):
            return 'P0 - Critical'

        # Check for important keywords
        if any(keyword in text for keyword in IMPORTANT_KEYWORDS):
            return 'P1 - High'

        # Check for business keywords
        if any(keyword in text for keyword in BUSINESS_KEYWORDS):
            return 'P2 - Medium'

        return 'P2 - Medium'

    def get_email_details(self, msg_id):
        """Fetch full email details"""
        try:
            message = self.service.users().messages().get(
                userId='me', id=msg_id, format='full').execute()

            headers = message['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown')

            # Get snippet
            snippet = message.get('snippet', '')

            return {
                'id': msg_id,
                'subject': subject,
                'sender': sender,
                'date': date,
                'snippet': snippet,
                'thread_id': message.get('threadId', '')
            }
        except Exception as e:
            self.log(f"Error fetching email details: {e}")
            return None

    def create_email_task(self, email_data):
        """Create task file for email"""
        try:
            priority = self.determine_priority(
                email_data['subject'],
                email_data['snippet'],
                email_data['sender']
            )

            # Generate task filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_subject = "".join(c if c.isalnum() or c in ('-', '_') else '_'
                                  for c in email_data['subject'][:50])
            task_filename = f"email_{safe_subject}_{timestamp}.md"
            task_path = NEEDS_ACTION_FOLDER / task_filename

            # Create task content
            task_content = f"""# Email Task: {email_data['subject']}

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Priority:** {priority}
**Status:** Pending
**Source:** Gmail Watcher

---

## 📧 Email Details

- **From:** {email_data['sender']}
- **Subject:** {email_data['subject']}
- **Received:** {email_data['date']}
- **Email ID:** `{email_data['id']}`
- **Thread ID:** `{email_data['thread_id']}`

---

## 📝 Email Preview

{email_data['snippet']}

---

## 🎯 Suggested Actions

- [ ] Read full email content
- [ ] Determine appropriate response
- [ ] Draft reply (if needed)
- [ ] Check if approval required for sending
- [ ] Update Dashboard

---

## 💡 Response Guidelines

Based on priority level **{priority}**:

- If **P0 (Critical)**: Respond within 1 hour
- If **P1 (High)**: Respond within 4 hours
- If **P2 (Medium)**: Respond within 24 hours
- If **P3 (Low)**: Respond within 48 hours

---

## 📋 Notes

*Add analysis and response notes here*

---

## ✅ Completion Checklist

- [ ] Email reviewed
- [ ] Response drafted
- [ ] Approval obtained (if required)
- [ ] Email sent
- [ ] Dashboard updated
- [ ] Task moved to Done

---

**Task File:** `{task_filename}`
**Generated by:** Gmail Watcher (Automated)
"""

            # Write task file
            with open(task_path, 'w', encoding='utf-8') as f:
                f.write(task_content)

            self.log(f"Created task: {task_filename}")
            return True

        except Exception as e:
            self.log(f"Error creating email task: {e}")
            return False

    def check_new_emails(self):
        """Check for new unread emails"""
        try:
            # Query for unread emails
            results = self.service.users().messages().list(
                userId='me',
                q='is:unread',
                maxResults=10
            ).execute()

            messages = results.get('messages', [])

            if not messages:
                self.log("No new unread emails")
                return 0

            new_count = 0
            for msg in messages:
                msg_id = msg['id']

                # Skip if already processed
                if msg_id in self.processed_ids:
                    continue

                # Get email details
                email_data = self.get_email_details(msg_id)

                if email_data:
                    # Check if email matches our criteria
                    text = f"{email_data['subject']} {email_data['snippet']}".lower()

                    # Check for any monitored keywords
                    all_keywords = URGENT_KEYWORDS + IMPORTANT_KEYWORDS + BUSINESS_KEYWORDS
                    if any(keyword in text for keyword in all_keywords):
                        self.log(f"New important email: {email_data['subject'][:50]}...")

                        if self.create_email_task(email_data):
                            self.processed_ids.add(msg_id)
                            new_count += 1
                    else:
                        # Mark as processed but don't create task
                        self.processed_ids.add(msg_id)
                        self.log(f"Skipped (no keywords): {email_data['subject'][:50]}...")

            if new_count > 0:
                self.save_processed_ids()
                self.log(f"Processed {new_count} new email(s)")

            return new_count

        except HttpError as error:
            self.log(f"Gmail API error: {error}")
            return 0
        except Exception as e:
            self.log(f"Error checking emails: {e}")
            return 0

    def run(self, interval=120):
        """Run watcher continuously"""
        self.log("=" * 60)
        self.log("Gmail Watcher Started")
        self.log(f"Check interval: {interval} seconds")
        self.log("=" * 60)

        if not self.authenticate():
            self.log("Authentication failed. Exiting.")
            return

        try:
            while True:
                self.check_new_emails()
                time.sleep(interval)
        except KeyboardInterrupt:
            self.log("Watcher stopped by user")
            print("\nGmail Watcher stopped.")


def main():
    """Main entry point"""
    watcher = GmailWatcher()
    watcher.run(interval=120)  # Check every 2 minutes


if __name__ == "__main__":
    main()
