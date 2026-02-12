#!/usr/bin/env python3
"""
LinkedIn Automation for AI Employee
Monitors LinkedIn engagement and posts business updates
"""

import os
import time
import json
from datetime import datetime, timedelta
from pathlib import Path
from playwright.sync_api import sync_playwright

# Configuration
VAULT_PATH = Path(__file__).parent
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
LOGS_FOLDER = VAULT_PATH / "Logs"
LINKEDIN_QUEUE = VAULT_PATH / "LinkedIn_Queue"
LINKEDIN_POSTED = VAULT_PATH / "LinkedIn_Posted"
PENDING_APPROVAL = VAULT_PATH / "Pending_Approval"
SESSION_FILE = VAULT_PATH / "linkedin_session.json"
POSTED_IDS_FILE = VAULT_PATH / "posted_linkedin.json"

# Ensure folders exist
NEEDS_ACTION_FOLDER.mkdir(exist_ok=True)
LOGS_FOLDER.mkdir(exist_ok=True)
LINKEDIN_QUEUE.mkdir(exist_ok=True)
LINKEDIN_POSTED.mkdir(exist_ok=True)
PENDING_APPROVAL.mkdir(exist_ok=True)


class LinkedInAutomation:
    """LinkedIn posting and monitoring automation"""

    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self.posted_ids = self.load_posted_ids()
        self.log_file = LOGS_FOLDER / f"linkedin_automation_{datetime.now().strftime('%Y%m%d')}.md"
        self.session_dir = VAULT_PATH / "linkedin_session_data"
        self.session_dir.mkdir(exist_ok=True)
        self.log("LinkedIn Automation initialized")

    def log(self, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        print(log_entry.strip())

    def load_posted_ids(self):
        """Load list of already posted content IDs"""
        if POSTED_IDS_FILE.exists():
            try:
                with open(POSTED_IDS_FILE, 'r') as f:
                    return set(json.load(f))
            except Exception as e:
                self.log(f"Error loading posted IDs: {e}")
                return set()
        return set()

    def save_posted_ids(self):
        """Save posted content IDs to file"""
        try:
            with open(POSTED_IDS_FILE, 'w') as f:
                json.dump(list(self.posted_ids), f)
        except Exception as e:
            self.log(f"Error saving posted IDs: {e}")

    def initialize_browser(self):
        """Initialize Playwright browser with persistent session"""
        try:
            playwright = sync_playwright().start()

            # Launch browser with persistent context
            self.context = playwright.chromium.launch_persistent_context(
                user_data_dir=str(self.session_dir),
                headless=False,  # Set to True for production
                args=['--no-sandbox', '--disable-setuid-sandbox']
            )

            self.page = self.context.new_page()
            self.log("Browser initialized successfully")
            return True

        except Exception as e:
            self.log(f"Error initializing browser: {e}")
            return False

    def login_linkedin(self):
        """Navigate to LinkedIn and handle login"""
        try:
            self.log("Navigating to LinkedIn...")
            self.page.goto('https://www.linkedin.com/feed/', wait_until='networkidle')

            # Check if already logged in
            try:
                self.page.wait_for_selector('div[data-test-id="feed-container"]', timeout=5000)
                self.log("Already logged in to LinkedIn")
                return True
            except:
                self.log("Please login to LinkedIn manually...")
                self.log("Waiting for login (60 seconds)...")

                # Wait for login
                self.page.wait_for_selector('div[data-test-id="feed-container"]', timeout=60000)
                self.log("Login successful!")
                return True

        except Exception as e:
            self.log(f"Error during LinkedIn login: {e}")
            return False

    def generate_post_content(self, topic, style="professional"):
        """Generate LinkedIn post content based on topic"""
        # This is a template-based approach
        # In production, you'd use Claude API to generate content

        templates = {
            "product_launch": """🚀 Exciting News!

We're thrilled to announce {topic}!

This has been months in the making, and we can't wait to share it with you.

Key highlights:
• [Benefit 1]
• [Benefit 2]
• [Benefit 3]

Want to learn more? Drop a comment or DM me!

#Innovation #ProductLaunch #Business""",

            "industry_insight": """💡 Industry Insight

{topic}

Here's what this means for businesses:

1. [Point 1]
2. [Point 2]
3. [Point 3]

What's your take on this? Let's discuss in the comments!

#Industry #BusinessStrategy #Insights""",

            "client_success": """🎉 Client Success Story

We recently helped {topic}

The results:
✅ [Metric 1]
✅ [Metric 2]
✅ [Metric 3]

Proud of what we accomplished together!

#ClientSuccess #Results #Partnership""",

            "tips": """📌 Quick Tip

{topic}

This simple approach can help you:
→ [Benefit 1]
→ [Benefit 2]
→ [Benefit 3]

Try it out and let me know how it works for you!

#Tips #BusinessGrowth #Productivity"""
        }

        return templates.get(style, templates["tips"]).format(topic=topic)

    def create_approval_request(self, post_content, post_type="business_update"):
        """Create approval request for LinkedIn post"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            approval_filename = f"linkedin_post_approval_{timestamp}.md"
            approval_path = PENDING_APPROVAL / approval_filename

            # Set expiry time (24 hours from now)
            expiry_time = (datetime.now() + timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S')

            approval_content = f"""# LinkedIn Post Approval Request

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Expires:** {expiry_time}
**Type:** LinkedIn Post
**Category:** {post_type}
**Status:** PENDING

---

## 📝 Post Content

```
{post_content}
```

---

## 🎯 Post Details

- **Estimated Reach:** 500-1000 connections
- **Best Time to Post:** 8:00 AM or 12:00 PM or 5:00 PM
- **Hashtags:** Included in content
- **Call-to-Action:** Yes

---

## ✅ APPROVAL INSTRUCTIONS

To **APPROVE** this post:
1. Move this file to the `/Approved` folder
2. The orchestrator will automatically post it

To **REJECT** this post:
1. Move this file to the `/Rejected` folder
2. Add rejection reason in the Notes section below

To **MODIFY** this post:
1. Edit the content above
2. Move to `/Approved` folder when ready

---

## 📋 Notes

*Add any notes or modifications here*

---

## ⚠️ Important

- This approval expires in 24 hours
- After expiry, the request will be automatically rejected
- Once posted, content will be moved to `/LinkedIn_Posted`

---

**Approval File:** `{approval_filename}`
**Generated by:** LinkedIn Automation
"""

            with open(approval_path, 'w', encoding='utf-8') as f:
                f.write(approval_content)

            self.log(f"Created approval request: {approval_filename}")
            return approval_path

        except Exception as e:
            self.log(f"Error creating approval request: {e}")
            return None

    def post_to_linkedin(self, content):
        """Post content to LinkedIn"""
        try:
            self.log("Attempting to post to LinkedIn...")

            # Navigate to feed if not already there
            if 'linkedin.com/feed' not in self.page.url:
                self.page.goto('https://www.linkedin.com/feed/')
                time.sleep(2)

            # Click "Start a post" button
            start_post_button = self.page.query_selector('button[aria-label*="Start a post"]')
            if not start_post_button:
                start_post_button = self.page.query_selector('button.share-box-feed-entry__trigger')

            if start_post_button:
                start_post_button.click()
                time.sleep(1)
            else:
                self.log("Could not find 'Start a post' button")
                return False

            # Find the text editor
            editor = self.page.query_selector('div[role="textbox"]')
            if not editor:
                self.log("Could not find post editor")
                return False

            # Type the content
            editor.click()
            editor.fill(content)
            time.sleep(1)

            # Click Post button
            post_button = self.page.query_selector('button[aria-label*="Post"]')
            if not post_button:
                post_button = self.page.query_selector('button.share-actions__primary-action')

            if post_button:
                post_button.click()
                time.sleep(3)
                self.log("Post published successfully!")
                return True
            else:
                self.log("Could not find Post button")
                return False

        except Exception as e:
            self.log(f"Error posting to LinkedIn: {e}")
            return False

    def check_approved_posts(self):
        """Check for approved posts and publish them"""
        try:
            approved_folder = VAULT_PATH / "Approved"
            if not approved_folder.exists():
                return 0

            approved_files = list(approved_folder.glob("linkedin_post_approval_*.md"))

            if not approved_files:
                return 0

            posted_count = 0

            for file_path in approved_files:
                try:
                    # Read the file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Extract post content (between ``` markers)
                    if '```' in content:
                        parts = content.split('```')
                        if len(parts) >= 3:
                            post_content = parts[1].strip()

                            # Post to LinkedIn
                            if self.post_to_linkedin(post_content):
                                # Move to posted folder
                                posted_path = LINKEDIN_POSTED / file_path.name
                                file_path.rename(posted_path)

                                # Update posted file with timestamp
                                with open(posted_path, 'a', encoding='utf-8') as f:
                                    f.write(f"\n\n---\n**Posted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

                                posted_count += 1
                                self.log(f"Posted and archived: {file_path.name}")
                            else:
                                self.log(f"Failed to post: {file_path.name}")

                except Exception as e:
                    self.log(f"Error processing approved post {file_path.name}: {e}")
                    continue

            return posted_count

        except Exception as e:
            self.log(f"Error checking approved posts: {e}")
            return 0

    def monitor_engagement(self):
        """Monitor engagement on recent posts"""
        try:
            self.log("Checking post engagement...")

            # Navigate to profile posts
            self.page.goto('https://www.linkedin.com/in/me/recent-activity/all/')
            time.sleep(2)

            # Get recent posts
            posts = self.page.query_selector_all('div[data-id]')[:5]  # Last 5 posts

            engagement_data = []

            for post in posts:
                try:
                    # Get likes count
                    likes_elem = post.query_selector('span[aria-label*="reaction"]')
                    likes = likes_elem.inner_text() if likes_elem else "0"

                    # Get comments count
                    comments_elem = post.query_selector('span[aria-label*="comment"]')
                    comments = comments_elem.inner_text() if comments_elem else "0"

                    engagement_data.append({
                        'likes': likes,
                        'comments': comments
                    })

                except Exception as e:
                    continue

            if engagement_data:
                self.log(f"Engagement check complete: {len(engagement_data)} posts analyzed")
                # Could create a report here
                return engagement_data

            return []

        except Exception as e:
            self.log(f"Error monitoring engagement: {e}")
            return []

    def run(self, check_interval=300):
        """Run LinkedIn automation continuously"""
        self.log("=" * 60)
        self.log("LinkedIn Automation Started")
        self.log(f"Check interval: {check_interval} seconds")
        self.log("=" * 60)

        if not self.initialize_browser():
            self.log("Browser initialization failed. Exiting.")
            return

        if not self.login_linkedin():
            self.log("LinkedIn login failed. Exiting.")
            return

        try:
            while True:
                # Check for approved posts
                posted = self.check_approved_posts()
                if posted > 0:
                    self.log(f"Posted {posted} approved post(s)")

                # Monitor engagement every 5 cycles
                if int(time.time()) % (check_interval * 5) == 0:
                    self.monitor_engagement()

                time.sleep(check_interval)

        except KeyboardInterrupt:
            self.log("Automation stopped by user")
            if self.context:
                self.context.close()
            print("\nLinkedIn Automation stopped.")


def main():
    """Main entry point"""
    automation = LinkedInAutomation()
    automation.run(check_interval=300)  # Check every 5 minutes


if __name__ == "__main__":
    main()
