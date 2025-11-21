import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import ttk
import threading
import os

root = tk.Tk()
root.title("Automated Email Sender")

# ==== UI Elements ====
filename_label = ttk.Label(root, text="Filename")
filename_label.grid(row=0, column=0, padx=5, pady=5)
filename_entry = ttk.Entry(root)
filename_entry.grid(row=0, column=1, padx=5, pady=5)

subject_label = ttk.Label(root, text="Subject")
subject_label.grid(row=1, column=0, padx=5, pady=5)
subject_entry = ttk.Entry(root)
subject_entry.grid(row=1, column=1, padx=5, pady=5)

body_label = ttk.Label(root, text="Body")
body_label.grid(row=2, column=0, padx=5, pady=5)
body_text = tk.Text(root, width=40, height=10)
body_text.grid(row=2, column=1, padx=5, pady=5)

status_label = ttk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# ==== Functions ====
def get_recipients_from_file(filename):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def get_info(filename, subject, body):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")

        recipients = get_recipients_from_file(filename)
        if not recipients:
            raise ValueError("No recipients found in file.")

        msg = EmailMessage()
        msg["from"] = "sunilpokharel111@gmail.com"
        msg["to"] = ",".join(recipients)
        msg["subject"] = subject
        msg.set_content(body)

        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        server.starttls()
        server.login("YOUR_EMAIL@gmail.com", "YOUR_APP_PASSWORD")
        server.send_message(msg)
        server.quit()

        root.after(0, lambda: status_label.config(text="Email sent successfully"))

    except Exception as e:
        root.after(0, lambda: status_label.config(text=f"Error: {e}"))

    finally:
        root.after(0, lambda: send_button.config(state="normal"))

def send_email_thread():
    filename = filename_entry.get().strip()
    subject = subject_entry.get().strip()
    body = body_text.get("1.0", "end-1c")

    if not filename:
        status_label.config(text="Error: filename is empty")
        return

    send_button.config(state="disabled")
    status_label.config(text="Sending...")
    threading.Thread(target=get_info, args=(filename, subject, body)).start()

send_button = ttk.Button(root, text="Send Email", command=send_email_thread)
send_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
