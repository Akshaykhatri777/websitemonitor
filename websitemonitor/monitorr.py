import requests
import smtplib
from email.mime.text import MIMEText

# Website and email settings
url = "https://www.examplenotworkingwebzozo.com"  # Replace with the URL you want to monitor
sender_email = "akshkhatri4@gmail.com"  # Replace with your email
receiver_email = "filmokae@gmail.com"  # Replace with recipient's email
password = "Khatarnak"  # Replace with your email password

def send_email_alert():
    try:
        # Set up SMTP server and log in
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)

        # Compose and send email
        msg = MIMEText(f"Alert: The website {url} is down!")
        msg["Subject"] = "Website Down Alert"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email alert sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Check website status
try:
    response = requests.get(url)
    if response.status_code != 200:
        send_email_alert()
    else:
        print(f"Website is up! Status: {response.status_code}")
except requests.exceptions.RequestException:
    print("Website is down!")
    send_email_alert()
