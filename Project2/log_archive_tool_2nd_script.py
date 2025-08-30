#!/usr/bin/env python3

import os
import sys
import tarfile
from datetime import datetime

'''import yagmail'''

# emailing user updates for archive
'''def send_email_notification(recipient_email, archive_path):
    yag = yagmail.SMTP("enter your email", "enter your password")
    subject = "Archive Update Notification"
    body = f"The latest archive has been created and is available at: {archive_path}"
    yag.send(to=recipient_email, subject=subject, contents=body)'''

# Step 1: Check if the user provided a log directory as an argument
if len(sys.argv) != 2:
    print("Usage: python log_archive.py <log-directory>")
    sys.exit(1)

log_dir = sys.argv[1]

# Step 2: Verify the log directory exists
if not os.path.isdir(log_dir):
    print(f"Error: The directory '{log_dir}' does not exist.")
    sys.exit(1)

# Step 3: Create a timestamp for the archive name
timestamp = datetime.now().strftime("%Y%m%d_%I%M%S%p")
archive_name = f"logs_archive_{timestamp}.tar.gz"

# Step 4: Create a directory to store archived logs
archive_dir = os.path.expanduser("~/log_archives")  # You can change this path
os.makedirs(archive_dir, exist_ok=True)

# Step 5: Full path for the archive file
archive_path = os.path.join(archive_dir, archive_name)

# Step 6: Compress the log directory into a .tar.gz archive
with tarfile.open(archive_path, "w:gz") as tar:
    tar.add(log_dir, arcname=os.path.basename(log_dir))

print(f"✅ Logs archived successfully to: {archive_path}")

# Step 7: Log the archive operation to a log file
log_file_path = os.path.join(archive_dir, "archive_log.txt")
with open(log_file_path, "a") as log_file:
    log_file.write(f"{timestamp} - Archived {log_dir} to {archive_name}\n")

print(f"📝 Archive operation logged in: {log_file_path}")
