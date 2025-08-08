import stat
import pdfkit
import fitz
from autogen_core.tools import FunctionTool
import markdown
import smtplib
from email.message import EmailMessage
import os

class Tools:
    @staticmethod
    def markdown_to_pdf(markdown_text: str, output_path: str):
        # Convert markdown to basic HTML
        body_content = markdown.markdown(markdown_text)

        # Wrap in full HTML with styling
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Policy Report</title>
            <style>
                body {{
                    font-family: 'Helvetica', sans-serif;
                    font-size: 14px;
                    line-height: 1.6;
                    padding: 40px;
                    color: #333;
                }}
                h1, h2, h3 {{
                    color: #2c3e50;
                }}
                ul, ol {{
                    margin-bottom: 1em;
                    padding-left: 1.2em;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            {body_content}
        </body>
        </html>
        """

        # Configure pdfkit with wkhtmltopdf path
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        # Generate PDF
        pdfkit.from_string(full_html, output_path, configuration=config)
        return output_path

    @staticmethod
    def send_email_with_attachment(to_email: str, subject: str, body: str, attachment_path: str):
        sender_email = "mkumari233107@gmail.com"
        sender_password = "vokm mkzj wuow wfye"

        if not sender_email or not sender_password:
            raise ValueError("Sender email or password not found")

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email
        msg.set_content(body)

        with open(attachment_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
            msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(sender_email, sender_password)
                smtp.send_message(msg)
                print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
    
    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        text = ""
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
