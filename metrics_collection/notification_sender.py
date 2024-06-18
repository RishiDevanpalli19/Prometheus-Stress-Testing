import twilio.rest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_whatsapp_notification(message):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = twilio.rest.Client(account_sid, auth_token)

    from_whatsapp_number = 'whatsapp:+00000000'  # Twilio WhatsApp sandbox number
    to_whatsapp_number = 'whatsapp:+000000000'  # Your WhatsApp number

    try:
        client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)
        print("WhatsApp message sent successfully.")
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")

def send_email_notification(subject, message):
    smtp_server = SMTP_SERVER
    smtp_port = SMTP_PORT
    sender_email = SENDER_EMAIL
    receiver_email = RECEIVER_EMAIL
    sender_password = SENDER_PASSWORD

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.close()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")