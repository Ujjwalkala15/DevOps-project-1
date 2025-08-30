---

## 📦 Log Archive Automation Tool 

A Python-based utility that compresses log files from a specified directory, timestamps the archive, and optionally sends email notifications or uploads the archive to a remote server or cloud storage.

---

## 🚀 Features

- Compresses logs into `.tar.gz` format with timestamped filenames  
- Supports custom source directories  
- Optional email notifications on archive creation  
- Optional upload to remote server (via SCP) or AWS S3  
- Modular and extensible for production use

---

## 🛠️ Requirements

- Python 3.12+
- `yagmail` (for email notifications)
- `boto3` (for AWS S3 uploads)
- Linux/WSL environment recommended

Install dependencies using a virtual environment:

```bash
sudo apt install python3.12-venv
python3 -m venv ~/email_env
source ~/email_env/bin/activate
pip install yagmail boto3
```

---

## 📂 Folder Structure

```
Project 2/
├── log_archive_tool_2nd_script.py
├── README.md
├── archives/                # Optional: stores compressed logs
└── logs/                    # Source log files
```

---

## 📋 How to Use

### 1. **Run the Script**

```bash
python3 log_archive_tool_2nd_script.py /path/to/logs
```

Example:

```bash
python3 log_archive_tool_2nd_script.py /var/log
```

This creates an archive like:

```
logs_archive_20250830_045648PM.tar.gz
```

### 2. **Enable Email Notifications (Optional)**

Update the script with your Gmail credentials and recipient email:

```python
yag = yagmail.SMTP("your_email@gmail.com", "your_app_password")
yag.send(to="recipient@example.com", subject="Log Archive Created", contents="Your archive is ready.")
```

> Use [App Passwords](https://myaccount.google.com/apppasswords) if 2FA is enabled.

### 3. **Upload to Remote Server (Optional)**

Set remote credentials and path:

```python
upload_to_remote_server("/path/to/archive", "user", "host.com", "/remote/path/")
```

### 4. **Upload to AWS S3 (Optional)**

Configure AWS credentials and bucket:

```python
upload_to_s3("my-bucket", "/path/to/archive", "archives/logs_archive.tar.gz")
```

---

## 🧠 Notes

- Avoid running as `root` unless necessary — use your regular user for safety.
- Always activate your virtual environment before running the script.
- YOPmail cannot send emails — use Gmail or another SMTP-compatible provider.

---

Project URL : https://roadmap.sh/projects/log-archive-tool

---

## 📌 To Do

- Add retry logic for email and upload failures  
- Encrypt archives for sensitive logs  
- Add CLI flags for verbosity, dry-run, and cleanup

---
