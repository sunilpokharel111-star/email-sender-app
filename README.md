# Email Sender App

A lightweight, threaded, GUI-based email automation tool built in Python using Tkinter.

## Features
- Send emails to multiple recipients
- Threaded GUI → no freezing
- Error handling for missing files, SMTP failures, empty fields
- Recipient list loaded from a file
- Can be converted to EXE using PyInstaller

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/email-sender-app.git
cd email-sender-app
pip install -r requirements.txt
python src/email_sender.py
