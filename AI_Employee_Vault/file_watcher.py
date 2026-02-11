#!/usr/bin/env python3
"""
File System Watcher for AI Employee
Monitors the Drop folder and creates task files in Needs_Action
"""

import os
import time
import hashlib
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
VAULT_PATH = Path(__file__).parent
DROP_FOLDER = VAULT_PATH / "Drop"
NEEDS_ACTION_FOLDER = VAULT_PATH / "Needs_Action"
LOGS_FOLDER = VAULT_PATH / "Logs"
INBOX_FOLDER = VAULT_PATH / "Inbox"

# Ensure folders exist
DROP_FOLDER.mkdir(exist_ok=True)
NEEDS_ACTION_FOLDER.mkdir(exist_ok=True)
LOGS_FOLDER.mkdir(exist_ok=True)
INBOX_FOLDER.mkdir(exist_ok=True)


class DropFolderHandler(FileSystemEventHandler):
    """Handles file system events in the Drop folder"""

    def __init__(self):
        self.processed_files = set()
        self.log_file = LOGS_FOLDER / f"watcher_log_{datetime.now().strftime('%Y%m%d')}.md"
        self.log(f"Watcher started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def log(self, message):
        """Write log entry"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        try:
            print(log_entry.strip())
        except UnicodeEncodeError:
            # Fallback for Windows console encoding issues
            print(log_entry.strip().encode('ascii', 'replace').decode('ascii'))

    def get_file_hash(self, filepath):
        """Generate hash of file to detect duplicates"""
        try:
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            self.log(f"Error hashing file {filepath}: {e}")
            return None

    def get_file_info(self, filepath):
        """Extract file metadata"""
        path = Path(filepath)
        stats = path.stat()

        return {
            'name': path.name,
            'size': stats.st_size,
            'size_human': self.human_readable_size(stats.st_size),
            'extension': path.suffix,
            'created': datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            'modified': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
        }

    def human_readable_size(self, size_bytes):
        """Convert bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"

    def determine_priority(self, file_info):
        """Determine task priority based on file characteristics"""
        name_lower = file_info['name'].lower()

        # Check for priority keywords
        if any(word in name_lower for word in ['urgent', 'critical', 'asap', 'emergency']):
            return 'P0 - Critical'
        elif any(word in name_lower for word in ['important', 'priority', 'high']):
            return 'P1 - High'
        elif any(word in name_lower for word in ['low', 'backlog', 'someday']):
            return 'P3 - Low'
        else:
            return 'P2 - Medium'

    def create_task_file(self, filepath):
        """Create a task markdown file in Needs_Action"""
        try:
            file_info = self.get_file_info(filepath)
            priority = self.determine_priority(file_info)

            # Generate task filename
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            safe_name = "".join(c if c.isalnum() or c in ('-', '_') else '_' for c in Path(filepath).stem)
            task_filename = f"task_{safe_name}_{timestamp}.md"
            task_path = NEEDS_ACTION_FOLDER / task_filename

            # Create task content
            task_content = f"""# Task: Process {file_info['name']}

**Created:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Priority:** {priority}
**Status:** Pending

---

## 📄 File Information

- **Filename:** {file_info['name']}
- **File Type:** {file_info['extension'] or 'No extension'}
- **Size:** {file_info['size_human']} ({file_info['size']:,} bytes)
- **Created:** {file_info['created']}
- **Modified:** {file_info['modified']}
- **Location:** `{filepath}`

---

## 📋 Task Description

A new file has been detected in the Drop folder. This task requires:

1. **Review** the file contents
2. **Determine** the appropriate action
3. **Process** according to file type and content
4. **Update** the dashboard with results

---

## 🎯 Suggested Actions

- [ ] Open and review the file
- [ ] Identify the file purpose/category
- [ ] Determine if any processing is needed
- [ ] Move to appropriate folder when complete
- [ ] Update Dashboard.md

---

## 📝 Notes

*Add processing notes here*

---

## ✅ Completion Checklist

- [ ] File reviewed
- [ ] Action determined
- [ ] Processing completed
- [ ] Dashboard updated
- [ ] File moved to Done folder

---

**Task File:** `{task_filename}`
**Source:** File Watcher (Automated)
"""

            # Write task file
            with open(task_path, 'w', encoding='utf-8') as f:
                f.write(task_content)

            self.log(f"[OK] Created task file: {task_filename} for {file_info['name']}")
            return task_path

        except Exception as e:
            self.log(f"[ERROR] Error creating task file for {filepath}: {e}")
            return None

    def on_created(self, event):
        """Handle file creation events"""
        if event.is_directory:
            return

        filepath = event.src_path

        # Ignore temporary files and hidden files
        if Path(filepath).name.startswith('.') or Path(filepath).name.startswith('~'):
            return

        # Wait a moment to ensure file is fully written
        time.sleep(0.5)

        # Check if already processed
        file_hash = self.get_file_hash(filepath)
        if file_hash and file_hash in self.processed_files:
            self.log(f"[SKIP] Skipping duplicate file: {Path(filepath).name}")
            return

        self.log(f"[NEW] New file detected: {Path(filepath).name}")

        # Create task file
        task_path = self.create_task_file(filepath)

        if task_path and file_hash:
            self.processed_files.add(file_hash)
            self.log(f"[OK] Task created successfully")

    def on_modified(self, event):
        """Handle file modification events"""
        # We only care about new files, not modifications
        pass


def main():
    """Main watcher loop"""
    print("=" * 60)
    print("AI Employee File Watcher")
    print("=" * 60)
    print(f"Monitoring: {DROP_FOLDER}")
    print(f"Task Output: {NEEDS_ACTION_FOLDER}")
    print(f"Logs: {LOGS_FOLDER}")
    print("=" * 60)
    print("Press Ctrl+C to stop\n")

    # Create event handler and observer
    event_handler = DropFolderHandler()
    observer = Observer()
    observer.schedule(event_handler, str(DROP_FOLDER), recursive=False)

    # Start watching
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        event_handler.log("Watcher stopped by user")
        observer.stop()
        print("\nWatcher stopped.")

    observer.join()


if __name__ == "__main__":
    main()
