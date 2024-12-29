import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'yukieandrada@gmail.com'
SENDER_PASSWORD = 'Gbella@345'
RECIPIENT_EMAIL = 'dba_email@example.com'
RECIPIENT_PHONE = '5205292296@vtext.com'  # Example for Verizon; change based on carrier

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

def simulate_error():
    error_message = "Dummy error message for testing purposes."
    send_error_notification(error_message)

# Example usage
simulate_error()