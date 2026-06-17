# ============= cozy_kit/_internal/helpers/smtp_helpers.py =============

# ============= IMPORTS =============
from smtplib import SMTP
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from cozy_kit._internal import errors
from email import encoders


class SMTPHelpers:
    def __init__(self, port, host, email, password, use_tls):
        self.port = port
        self.host = host
        self.email = email
        self.password = password
        self.use_tls = use_tls

    @staticmethod
    def _attach_files(attachments: list[str] | None, msg: MIMEMultipart) -> None:
        if attachments:
            for file_path in attachments:
                path = Path(file_path)

                try:
                    with open(path, "rb") as f:  # Open file
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(f.read())
                except (
                    FileNotFoundError
                ):  # Raise exception if the attachment doesn't exist
                    raise errors.AttachmentNotFoundError(
                        "The attachment you provided does not exist. It may have been deleted or moved to another place."
                    )

                encoders.encode_base64(part)

                part.add_header(
                    "Content-Disposition", f'attachment; filename="{path.name}"'
                )

                msg.attach(part)  # Attach attachment to the email

    def _send(self, msg: MIMEMultipart) -> None:
        with SMTP(self.host, self.port) as server:  # Open SMTP server
            if self.use_tls:
                server.starttls()

            if self.email and self.password:
                server.login(self.email, self.password)  # Login to send mail

            else:  # Raise Exception if password or email unfilled
                raise errors.UnfilledPasswordAndEmailError(
                    "You didn't enter your email and password. Please enter your email and password to send the email."
                )
            server.send_message(msg)  # Send mail
