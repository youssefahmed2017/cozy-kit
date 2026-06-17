# ============= cozy_kit/mailer.py =============

# ============= IMPORTS =============
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from cozy_kit._internal import errors
from cozy_kit._internal.helpers.smtp_helpers import SMTPHelpers


# ============= SMTPMailer CLASS =============
class SMTPMailer(SMTPHelpers):
    """A mailer class that sends mails and HTML mails.
    Methods:
        send_mail()
        send_html_mail()

    Parameters:
        host: str
        email: str
        password: str
        use_tls: bool
        port: int
    """

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
        super().__init__(
            email=self.email,
            host=self.host,
            port=self.port,
            password=self.password,
            use_tls=self.use_tls,
        )

    def send_mail(
        self,
        subject: str,
        body: str,
        to_addrs: list[str],
        attachments: list[str] | None = None,
    ) -> None:
        """Send a mail using SMTP Servers.
        Parameters:
            subject: str
            body: str
            to_addrs: list[str]
            attachments: list[str] | None

        Raises:
            NoRecipientError
            AttachmentNotFoundError
        """

        msg = MIMEMultipart()
        # Set mail parameters
        msg["From"] = self.email
        msg["To"] = ", ".join(to_addrs)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        if not to_addrs:  # Check if recipient not provided
            raise errors.NoRecipientError(
                "No recipient provided. Please provide a recipient before you can send the email."
            )

        self._attach_files(attachments, msg)

        self._send(msg)  # Send mail

    def send_html_mail(
        self,
        html: str,
        to_addrs: list[str],
        subject: str,
        attachments: list[str] | None = None,
    ) -> None:
        """Sends an HTML mail using SMTP Servers.
        Parameters:
            html: str
            to_addrs: list[str]
            subject: str
            attachments: list[str] | None
        Raises:
            NoRecipientError
            AttachmentNotFoundError
        """
        msg = MIMEMultipart()
        # Set mail parameters
        msg["From"] = self.email
        msg["To"] = ", ".join(to_addrs)
        msg["Subject"] = subject
        msg.attach(MIMEText(html, "html"))

        if not to_addrs:  # Check if recipient not provided
            raise errors.NoRecipientError(
                "No recipient provided. Please provide a recipient before you can send the email."
            )

        self._attach_files(attachments, msg)

        self._send(msg)  # Send mail
