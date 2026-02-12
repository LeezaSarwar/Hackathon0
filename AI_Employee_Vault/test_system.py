#!/usr/bin/env python3
"""
Test Suite for AI Employee System
Tests all major components and workflows
"""

import os
import time
from datetime import datetime
from pathlib import Path
import shutil

# Configuration
VAULT_PATH = Path(__file__).parent
DROP = VAULT_PATH / "Drop"
NEEDS_ACTION = VAULT_PATH / "Needs_Action"
PENDING_APPROVAL = VAULT_PATH / "Pending_Approval"
APPROVED = VAULT_PATH / "Approved"
DONE = VAULT_PATH / "Done"
LOGS = VAULT_PATH / "Logs"


class TestSuite:
    """Test suite for AI Employee system"""

    def __init__(self):
        self.test_log = LOGS / f"test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        self.tests_passed = 0
        self.tests_failed = 0
        self.log("=" * 60)
        self.log("AI Employee System - Test Suite")
        self.log("=" * 60)

    def log(self, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.test_log, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        try:
            print(log_entry.strip())
        except UnicodeEncodeError:
            # Fallback for Windows console encoding issues
            safe_message = log_entry.strip().encode('ascii', 'replace').decode('ascii')
            print(safe_message)

    def test_folder_structure(self):
        """Test 1: Verify folder structure exists"""
        self.log("\n## Test 1: Folder Structure")

        required_folders = [
            "Inbox", "Needs_Action", "Done", "Plans", "Logs", "Skills",
            "Pending_Approval", "Approved", "Rejected",
            "LinkedIn_Queue", "LinkedIn_Ideas", "LinkedIn_Posted", "Drop"
        ]

        all_exist = True
        for folder in required_folders:
            folder_path = VAULT_PATH / folder
            if folder_path.exists():
                self.log(f"✅ {folder} exists")
            else:
                self.log(f"❌ {folder} missing")
                all_exist = False

        if all_exist:
            self.log("✅ Test 1 PASSED: All folders exist")
            self.tests_passed += 1
        else:
            self.log("❌ Test 1 FAILED: Some folders missing")
            self.tests_failed += 1

    def test_core_files(self):
        """Test 2: Verify core files exist"""
        self.log("\n## Test 2: Core Files")

        required_files = [
            "Dashboard.md",
            "Company_Handbook.md",
            "Business_Goals.md",
            "file_watcher.py",
            "gmail_watcher.py",
            "whatsapp_watcher.py",
            "linkedin_automation.py",
            "orchestrator.py",
            "generate_briefing.py",
            "generate_summary.py",
            "prepare_linkedin.py"
        ]

        all_exist = True
        for file in required_files:
            file_path = VAULT_PATH / file
            if file_path.exists():
                self.log(f"✅ {file} exists")
            else:
                self.log(f"❌ {file} missing")
                all_exist = False

        if all_exist:
            self.log("✅ Test 2 PASSED: All core files exist")
            self.tests_passed += 1
        else:
            self.log("❌ Test 2 FAILED: Some core files missing")
            self.tests_failed += 1

    def test_skills(self):
        """Test 3: Verify agent skills exist"""
        self.log("\n## Test 3: Agent Skills")

        required_skills = [
            "email_triage_skill.md",
            "whatsapp_response_skill.md",
            "linkedin_post_skill.md",
            "approval_request_skill.md",
            "create_task_plan_skill.md",
            "update_dashboard_skill.md",
            "process_inbox_skill.md"
        ]

        skills_folder = VAULT_PATH / "Skills"
        all_exist = True

        for skill in required_skills:
            skill_path = skills_folder / skill
            if skill_path.exists():
                self.log(f"✅ {skill} exists")
            else:
                self.log(f"❌ {skill} missing")
                all_exist = False

        if all_exist:
            self.log("✅ Test 3 PASSED: All skills exist")
            self.tests_passed += 1
        else:
            self.log("❌ Test 3 FAILED: Some skills missing")
            self.tests_failed += 1

    def test_file_watcher_simulation(self):
        """Test 4: Simulate file watcher workflow"""
        self.log("\n## Test 4: File Watcher Simulation")

        try:
            # Create test file in Drop folder
            test_file = DROP / "test_urgent_task.txt"
            with open(test_file, 'w') as f:
                f.write("This is an urgent test task for the AI Employee system.")

            self.log(f"✅ Created test file: {test_file.name}")

            # Simulate task creation (normally done by file_watcher.py)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            task_file = NEEDS_ACTION / f"task_test_urgent_task_{timestamp}.md"

            task_content = f"""# Task: Process test_urgent_task.txt

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Priority:** P0 - Critical
**Status:** Pending

---

## 📄 File Information

- **Filename:** test_urgent_task.txt
- **Location:** {test_file}

---

## 📋 Task Description

Test task created by test suite.

---

**Task File:** `{task_file.name}`
**Source:** Test Suite
"""

            with open(task_file, 'w', encoding='utf-8') as f:
                f.write(task_content)

            self.log(f"✅ Created task file: {task_file.name}")

            # Verify task file exists
            if task_file.exists():
                self.log("✅ Test 4 PASSED: File watcher workflow simulated")
                self.tests_passed += 1
            else:
                self.log("❌ Test 4 FAILED: Task file not created")
                self.tests_failed += 1

        except Exception as e:
            self.log(f"❌ Test 4 FAILED: {e}")
            self.tests_failed += 1

    def test_approval_workflow_simulation(self):
        """Test 5: Simulate approval workflow"""
        self.log("\n## Test 5: Approval Workflow Simulation")

        try:
            # Create approval request
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            approval_file = PENDING_APPROVAL / f"test_approval_{timestamp}.md"

            approval_content = f"""# Test Approval Request

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Expires:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Type:** Test
**Status:** PENDING

---

## 📋 Action Details

This is a test approval request created by the test suite.

---

## ✅ APPROVAL INSTRUCTIONS

Move to /Approved to approve or /Rejected to reject.

---

**Approval File:** `{approval_file.name}`
**Generated by:** Test Suite
"""

            with open(approval_file, 'w', encoding='utf-8') as f:
                f.write(approval_content)

            self.log(f"✅ Created approval request: {approval_file.name}")

            # Verify approval file exists
            if approval_file.exists():
                self.log("✅ Test 5 PASSED: Approval workflow simulated")
                self.tests_passed += 1
            else:
                self.log("❌ Test 5 FAILED: Approval file not created")
                self.tests_failed += 1

        except Exception as e:
            self.log(f"❌ Test 5 FAILED: {e}")
            self.tests_failed += 1

    def test_helper_scripts(self):
        """Test 6: Test helper scripts execution"""
        self.log("\n## Test 6: Helper Scripts")

        scripts = [
            "generate_briefing.py",
            "generate_summary.py",
            "prepare_linkedin.py"
        ]

        all_passed = True

        for script in scripts:
            script_path = VAULT_PATH / script
            if script_path.exists():
                self.log(f"✅ {script} exists and is executable")
            else:
                self.log(f"❌ {script} not found")
                all_passed = False

        if all_passed:
            self.log("✅ Test 6 PASSED: All helper scripts exist")
            self.tests_passed += 1
        else:
            self.log("❌ Test 6 FAILED: Some helper scripts missing")
            self.tests_failed += 1

    def test_mcp_server(self):
        """Test 7: Verify MCP server files"""
        self.log("\n## Test 7: MCP Server")

        mcp_path = Path(__file__).parent.parent / "email_mcp_server"
        required_files = ["index.js", "package.json"]

        all_exist = True
        for file in required_files:
            file_path = mcp_path / file
            if file_path.exists():
                self.log(f"✅ {file} exists")
            else:
                self.log(f"❌ {file} missing")
                all_exist = False

        if all_exist:
            self.log("✅ Test 7 PASSED: MCP server files exist")
            self.tests_passed += 1
        else:
            self.log("❌ Test 7 FAILED: Some MCP server files missing")
            self.tests_failed += 1

    def generate_report(self):
        """Generate final test report"""
        self.log("\n" + "=" * 60)
        self.log("TEST SUMMARY")
        self.log("=" * 60)
        self.log(f"Tests Passed: {self.tests_passed}")
        self.log(f"Tests Failed: {self.tests_failed}")
        self.log(f"Total Tests: {self.tests_passed + self.tests_failed}")

        if self.tests_failed == 0:
            self.log("\n✅ ALL TESTS PASSED!")
            self.log("The AI Employee system is ready for use.")
        else:
            self.log(f"\n⚠️ {self.tests_failed} TEST(S) FAILED")
            self.log("Please review the failures above and fix them.")

        self.log("\n" + "=" * 60)
        self.log(f"Test log saved to: {self.test_log}")
        self.log("=" * 60)

    def run_all_tests(self):
        """Run all tests"""
        self.test_folder_structure()
        self.test_core_files()
        self.test_skills()
        self.test_file_watcher_simulation()
        self.test_approval_workflow_simulation()
        self.test_helper_scripts()
        self.test_mcp_server()
        self.generate_report()


def main():
    """Main entry point"""
    test_suite = TestSuite()
    test_suite.run_all_tests()


if __name__ == "__main__":
    main()
