import smtplib
import imaplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 發送郵件
def send_email(message, recipient_email):
    sender_email = "h34104028@gs.ncku.edu.tw"  # 替換為你的 Gmail 地址
    sender_password = "esks cohm zegf xyam"  # 替換為你的 Gmail 應用專用密碼

    # 設定郵件標題與內容
    subject = "Signal Email"
    body = message

    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = recipient_email
    email_message['Subject'] = subject
    email_message.attach(MIMEText(body, 'plain'))

    try:
        # 設定 SMTP 伺服器
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 啟用加密
        server.login(sender_email, sender_password)  # 登入

        # 發送郵件
        server.sendmail(sender_email, recipient_email, email_message.as_string())
        server.quit()

        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
