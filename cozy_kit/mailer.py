from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from . import errors


class SMTPMailer:
    def __init__(
        self,
        host: str,
        email: str,
        password: str,
        use_tls: bool = True,
        port: int = 587,
    ) -> None:
        self.host = host
        self.password = password
        self.email = email
        self.use_tls = use_tls
        self.port = port

    @staticmethod
    def __attach_files(attachments: list[str] | None, msg: MIMEMultipart) -> None:
        if attachments:
            for file_path in attachments:
                path = Path(file_path)
                try:
                    with open(path, "rb") as f:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(f.read())
                except FileNotFoundError:
                    raise errors.AttachmentNotFoundError(
                        "The attachment you provided does not exist. It may have been deleted or moved to another place."
                    )

                encoders.encode_base64(part)

                part.add_header(
                    "Content-Disposition", f'attachment; filename="{path.name}"'
                )

                msg.attach(part)

    def __send(self, msg: MIMEMultipart) -> None:
        with SMTP(self.host, self.port) as server:
            if self.use_tls:
                server.starttls()

            if self.email and self.password:
                server.login(self.email, self.password)

            else:
                raise errors.UnfilledPasswordAndEmailError(
                    "You didn't enter your email and password. Please enter your email and password to send the email."
                )
            server.send_message(msg)

    def send_mail(
        self,
        subject: str,
        body: str,
        to_addrs: list[str],
        attachments: list[str] | None = None,
    ) -> None:
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = ", ".join(to_addrs)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        if not to_addrs:
            raise errors.NoRecipientError(
                "No recipients provided. Please provide a recipient before you can send the email."
            )

        self.__attach_files(attachments, msg)

        self.__send(msg)

    def send_html_mail(
        self,
        html: str,
        to_addrs: list[str],
        subject: str,
        attachments: list[str] | None = None,
    ) -> None:
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = ", ".join(to_addrs)
        msg["Subject"] = subject
        msg.attach(MIMEText(html, "html"))

        if not to_addrs:
            raise errors.NoRecipientError(
                "No recipients provided. Please provide a recipient before you can send the email."
            )

        self.__attach_files(attachments, msg)

        self.__send(msg)
