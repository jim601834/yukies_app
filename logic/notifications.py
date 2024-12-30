import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'jim.601834@gmail.com'
SENDER_PASSWORD = 'diie byqr knav hqtg'  # Use your Gmail app-specific password
RECIPIENT_EMAIL = 'jimandrada1940@gmail.com'
RECIPIENT_PHONE = '5203015469@vtext.com'  # Verizon email-to-SMS gateway

def send_error_notification(error_message):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = 'Database Transaction Error Notification'

    body = f"An error occurred during a database transaction:\n\n{error_message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)
        server.sendmail(SENDER_EMAIL, RECIPIENT_PHONE, text)  # Send to phone as SMS
        server.quit()
        print("Error notification sent successfully.")
    except Exception as e:
        print(f"Failed to send error notification: {e}")