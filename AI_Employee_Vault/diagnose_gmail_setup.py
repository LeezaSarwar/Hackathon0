"""
Quick diagnostic to check Gmail API setup
"""

print("=" * 60)
print("Gmail API Setup Diagnostic")
print("=" * 60)
print()

# Check credentials file
import json
from pathlib import Path

vault_path = Path(__file__).parent
creds_file = vault_path / "gmail_credentials.json"

if creds_file.exists():
    print("[OK] Credentials file found")
    with open(creds_file, 'r') as f:
        creds = json.load(f)
        client_id = creds['installed']['client_id']
        project_id = creds['installed'].get('project_id', 'Not found')
        print(f"  Client ID: {client_id[:30]}...")
        print(f"  Project ID: {project_id}")
else:
    print("[ERROR] Credentials file NOT found")
    print()
    exit(1)

print()
print("=" * 60)
print("NEXT STEPS TO FIX 400 ERROR:")
print("=" * 60)
print()
print("The 400 error means OAuth consent screen is not properly configured.")
print()
print("Follow these steps EXACTLY:")
print()
print("1. Go to OAuth Consent Screen:")
print(f"   https://console.cloud.google.com/apis/credentials/consent?project={project_id}")
print()
print("2. Check Publishing Status:")
print("   - Should show 'Testing' status")
print("   - If not configured, click 'EDIT APP'")
print()
print("3. Fill Required Fields:")
print("   - App name: AI Employee Gmail Watcher")
print("   - User support email: (your email)")
print("   - Developer contact: (your email)")
print("   - Click 'SAVE AND CONTINUE'")
print()
print("4. Add Scopes:")
print("   - Click 'ADD OR REMOVE SCOPES'")
print("   - Search: gmail.readonly")
print("   - Check: https://www.googleapis.com/auth/gmail.readonly")
print("   - Click 'UPDATE'")
print("   - Click 'SAVE AND CONTINUE'")
print()
print("5. Add Test Users (MOST IMPORTANT!):")
print("   - Click 'ADD USERS'")
print("   - Enter YOUR Gmail address")
print("   - Click 'ADD'")
print("   - Click 'SAVE AND CONTINUE'")
print()
print("6. Enable Gmail API:")
print(f"   https://console.cloud.google.com/apis/library/gmail.googleapis.com?project={project_id}")
print("   - Click 'ENABLE' if not already enabled")
print()
print("=" * 60)
print("After completing these steps, run the watcher again!")
print("=" * 60)
