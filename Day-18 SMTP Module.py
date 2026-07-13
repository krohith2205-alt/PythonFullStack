# SMTP module

# email.message

import smtplib
import ssl
from email.message import EmailMessage

sender_email = "krohith2205@gmail.com"
password = "uysx flll ckff glrs"
receiver_email = "kalarohith888@gmail.com"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Welcome Mail"
message.set_content(f"""
Hello Kalahasthi Rohtih

Welcome to the Python Class

Regards,
Python Team
""")

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.send_message(message)
    
                                    
