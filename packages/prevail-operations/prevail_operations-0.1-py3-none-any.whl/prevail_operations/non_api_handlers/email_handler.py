import smtplib
from email.message import EmailMessage


class SendEmail:
    def __init__(self):
        return

    def send_email(
        emailFrom,
        emailTo,
        emailSubject,
        emailBody,
        emailAttachmentFileName,
        port,
        password,
    ):
        message = EmailMessage()
        message["From"] = emailFrom
        message["To"] = emailTo
        message["Subject"] = emailSubject
        message.set_content(emailBody, "plain")

        if emailAttachmentFileName:
            with open(emailAttachmentFileName, "rb") as attachment:
                message.add_attachment(
                    attachment.read(),
                    maintype="application",
                    subtype="octect-stream",
                    filename=emailAttachmentFileName,
                )

        with smtplib.SMTP("smtp-mail.outlook.com", port) as server:
            print("Connecting to email server...")
            server.starttls()
            server.login(emailFrom, password)
            print("Connected to server.")
            server.send_message(message)
            print("Email sent.")
