#!/usr/bin/env python3
"""
Orchestrator for AI Employee
Monitors approved actions and executes them via MCP server
"""

import os
import time
import json
import shutil
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import re

# Configuration
VAULT_PATH = Path(__file__).parent
PENDING_APPROVAL = VAULT_PATH / "Pending_Approval"
APPROVED = VAULT_PATH / "Approved"
REJECTED = VAULT_PATH / "Rejected"
DONE = VAULT_PATH / "Done"
LOGS_FOLDER = VAULT_PATH / "Logs"
LINKEDIN_POSTED = VAULT_PATH / "LinkedIn_Posted"

# Ensure folders exist
for folder in [PENDING_APPROVAL, APPROVED, REJECTED, DONE, LOGS_FOLDER, LINKEDIN_POSTED]:
    folder.mkdir(exist_ok=True)


class Orchestrator:
    """Orchestrates approved actions and manages workflow"""

    def __init__(self):
        self.log_file = LOGS_FOLDER / f"orchestrator_{datetime.now().strftime('%Y%m%d')}.md"
        self.log("Orchestrator initialized")

    def log(self, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        print(log_entry.strip())

    def check_expiry(self, file_path):
        """Check if approval request has expired"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract expiry time
            expiry_match = re.search(r'\*\*Expires:\*\*\s+(.+)', content)
            if not expiry_match:
                return False

            expiry_str = expiry_match.group(1).strip()
            expiry_time = datetime.strptime(expiry_str, '%Y-%m-%d %H:%M:%S')

            if datetime.now() > expiry_time:
                self.log(f"Approval expired: {file_path.name}")
                # Move to rejected
                rejected_path = REJECTED / file_path.name
                shutil.move(str(file_path), str(rejected_path))

                # Add expiry note
                with open(rejected_path, 'a', encoding='utf-8') as f:
                    f.write(f"\n\n---\n**EXPIRED:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("**Reason:** Approval request expired before review\n")

                return True

            return False

        except Exception as e:
            self.log(f"Error checking expiry for {file_path.name}: {e}")
            return False

    def extract_email_details(self, content):
        """Extract email details from approval file"""
        try:
            # Extract To
            to_match = re.search(r'\*\*To:\*\*\s+(.+)', content)
            to = to_match.group(1).strip() if to_match else None

            # Extract Subject
            subject_match = re.search(r'\*\*Subject:\*\*\s+(.+)', content)
            subject = subject_match.group(1).strip() if subject_match else None

            # Extract Body (between ``` markers or after Body:)
            body_match = re.search(r'\*\*Body:\*\*\s+```\n(.*?)\n```', content, re.DOTALL)
            if not body_match:
                body_match = re.search(r'\*\*Body:\*\*\s+(.+?)(?=\n\*\*|---)', content, re.DOTALL)

            body = body_match.group(1).strip() if body_match else None

            return {
                'to': to,
                'subject': subject,
                'body': body
            }

        except Exception as e:
            self.log(f"Error extracting email details: {e}")
            return None

    def extract_linkedin_content(self, content):
        """Extract LinkedIn post content from approval file"""
        try:
            # Extract content between ``` markers
            content_match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
            if content_match:
                return content_match.group(1).strip()

            # Fallback: look for Content: field
            content_match = re.search(r'\*\*Content:\*\*\s+(.+?)(?=\n\*\*|---)', content, re.DOTALL)
            if content_match:
                return content_match.group(1).strip()

            return None

        except Exception as e:
            self.log(f"Error extracting LinkedIn content: {e}")
            return None

    def send_email_via_mcp(self, email_details):
        """Send email using MCP server"""
        try:
            # This would call the MCP server
            # For now, we'll simulate it
            self.log(f"Sending email to {email_details['to']}")
            self.log(f"Subject: {email_details['subject']}")

            # In production, you would:
            # 1. Call the MCP server via Claude Code
            # 2. Or use direct API call to Gmail
            # 3. Or use subprocess to call MCP CLI

            # Simulated success
            self.log("Email sent successfully (simulated)")
            return True

        except Exception as e:
            self.log(f"Error sending email: {e}")
            return False

    def post_to_linkedin(self, content):
        """Post to LinkedIn via automation script"""
        try:
            self.log("Posting to LinkedIn...")

            # In production, this would:
            # 1. Call the linkedin_automation.py script
            # 2. Or trigger the posting directly

            # For now, create a queue file
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            queue_file = VAULT_PATH / "LinkedIn_Queue" / f"post_{timestamp}.md"

            with open(queue_file, 'w', encoding='utf-8') as f:
                f.write(f"# LinkedIn Post - Ready to Publish\n\n")
                f.write(f"**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(f"---\n\n")
                f.write(f"## Content\n\n```\n{content}\n```\n")

            self.log(f"LinkedIn post queued: {queue_file.name}")
            return True

        except Exception as e:
            self.log(f"Error posting to LinkedIn: {e}")
            return False

    def execute_approved_action(self, file_path):
        """Execute an approved action"""
        try:
            self.log(f"Processing approved action: {file_path.name}")

            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Determine action type
            action_type = None
            if 'email_approval' in file_path.name:
                action_type = 'email'
            elif 'linkedin_post_approval' in file_path.name:
                action_type = 'linkedin'
            elif 'payment_approval' in file_path.name:
                action_type = 'payment'

            if not action_type:
                # Try to extract from content
                type_match = re.search(r'\*\*Action Type:\*\*\s+(.+)', content)
                if type_match:
                    action_type = type_match.group(1).strip().lower()

            # Execute based on type
            success = False

            if action_type == 'email':
                email_details = self.extract_email_details(content)
                if email_details and all(email_details.values()):
                    success = self.send_email_via_mcp(email_details)
                else:
                    self.log("Error: Incomplete email details")

            elif action_type == 'linkedin':
                linkedin_content = self.extract_linkedin_content(content)
                if linkedin_content:
                    success = self.post_to_linkedin(linkedin_content)
                else:
                    self.log("Error: Could not extract LinkedIn content")

            elif action_type == 'payment':
                self.log("Payment actions require manual processing")
                success = False

            else:
                self.log(f"Unknown action type: {action_type}")
                success = False

            # Move to appropriate folder
            if success:
                # Move to Done or LinkedIn_Posted
                if action_type == 'linkedin':
                    dest_path = LINKEDIN_POSTED / file_path.name
                else:
                    dest_path = DONE / file_path.name

                shutil.move(str(file_path), str(dest_path))

                # Add execution timestamp
                with open(dest_path, 'a', encoding='utf-8') as f:
                    f.write(f"\n\n---\n**EXECUTED:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"**Status:** Success\n")

                self.log(f"Action executed successfully: {file_path.name}")
            else:
                # Move back to pending with error note
                pending_path = PENDING_APPROVAL / file_path.name
                shutil.move(str(file_path), str(pending_path))

                with open(pending_path, 'a', encoding='utf-8') as f:
                    f.write(f"\n\n---\n**EXECUTION FAILED:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("**Status:** Failed - Moved back to Pending\n")

                self.log(f"Action execution failed: {file_path.name}")

            return success

        except Exception as e:
            self.log(f"Error executing action {file_path.name}: {e}")
            return False

    def check_pending_expiry(self):
        """Check all pending approvals for expiry"""
        try:
            pending_files = list(PENDING_APPROVAL.glob("*_approval_*.md"))

            for file_path in pending_files:
                self.check_expiry(file_path)

        except Exception as e:
            self.log(f"Error checking pending expiry: {e}")

    def process_approved_actions(self):
        """Process all approved actions"""
        try:
            approved_files = list(APPROVED.glob("*_approval_*.md"))

            if not approved_files:
                return 0

            processed_count = 0

            for file_path in approved_files:
                if self.execute_approved_action(file_path):
                    processed_count += 1

            return processed_count

        except Exception as e:
            self.log(f"Error processing approved actions: {e}")
            return 0

    def generate_daily_summary(self):
        """Generate daily summary of activities"""
        try:
            summary_file = LOGS_FOLDER / f"daily_summary_{datetime.now().strftime('%Y%m%d')}.md"

            # Count files in each folder
            pending_count = len(list(PENDING_APPROVAL.glob("*.md")))
            approved_count = len(list(APPROVED.glob("*.md")))
            rejected_count = len(list(REJECTED.glob("*.md")))
            done_count = len(list(DONE.glob("*.md")))

            summary = f"""# Daily Summary - {datetime.now().strftime('%Y-%m-%d')}

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 Status Overview

- **Pending Approval:** {pending_count}
- **Approved (Processing):** {approved_count}
- **Rejected:** {rejected_count}
- **Completed:** {done_count}

---

## 🎯 Actions Today

[This section would be populated with actual actions taken]

---

## 📈 Performance Metrics

- **Average Approval Time:** [To be calculated]
- **Success Rate:** [To be calculated]
- **Expiry Rate:** [To be calculated]

---

**Generated by:** Orchestrator
"""

            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(summary)

            self.log(f"Daily summary generated: {summary_file.name}")

        except Exception as e:
            self.log(f"Error generating daily summary: {e}")

    def run(self, check_interval=60):
        """Run orchestrator continuously"""
        self.log("=" * 60)
        self.log("Orchestrator Started")
        self.log(f"Check interval: {check_interval} seconds")
        self.log("=" * 60)

        last_summary_date = None

        try:
            while True:
                # Check for expired approvals
                self.check_pending_expiry()

                # Process approved actions
                processed = self.process_approved_actions()
                if processed > 0:
                    self.log(f"Processed {processed} approved action(s)")

                # Generate daily summary (once per day)
                current_date = datetime.now().date()
                if last_summary_date != current_date:
                    self.generate_daily_summary()
                    last_summary_date = current_date

                time.sleep(check_interval)

        except KeyboardInterrupt:
            self.log("Orchestrator stopped by user")
            print("\nOrchestrator stopped.")


def main():
    """Main entry point"""
    orchestrator = Orchestrator()
    orchestrator.run(check_interval=60)  # Check every minute


if __name__ == "__main__":
    main()
