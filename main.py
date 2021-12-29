from fastapi import FastAPI, HTTPException
from jinja2 import Template
from dotenv import dotenv_values
from email.mime.text import MIMEText
import smtplib

from schemas import SupportClient


app = FastAPI()

config_file = dotenv_values(".env")
with open('index.html', 'r') as file:
    html = file.read()


@app.post('/email/', response_model=SupportClient)
def post_email(client: SupportClient):
    template = Template(html)
    template = template.render(full_name=client.full_name, company=client.company, email_address=client.email_address,
                               number_phone=client.number_phone, description=client.description)
    try:
        send_email(template)
        return client
    except HTTPException(status_code=535) as _ex:
        pass


def send_email(text_html):

    # Data for email
    sender = config_file["EMAIL_SENDER"]
    password = config_file["PASS"]
    recipient = config_file["EMAIL_RECIPIENT"]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Delivery email
    server.login(sender, password)
    message = MIMEText(text_html, 'html')
    message["Subject"] = "Новая заявка"
    message["From"] = "От сайта ИТС"
    message["To"] = sender
    server.sendmail(sender, recipient, message.as_string())
