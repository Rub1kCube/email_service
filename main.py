import uvicorn
from fastapi import FastAPI, HTTPException
from jinja2 import Template
from dotenv import dotenv_values
from email.mime.text import MIMEText
import smtplib  # Docks https://docs.python.org/3/library/smtplib.html

from schemas import SupportClient
from settings import settings

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
    except Exception as _ex:
        raise HTTPException(status_code=500, detail=f"{_ex}")


def send_email(text_html):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Delivery email
    server.login(settings.EMAIL_SENDER, settings.PASS)
    message = MIMEText(text_html, 'html')
    message["Subject"] = "Новая заявка"
    message["From"] = "От сайта ИТС"
    message["To"] = settings.EMAIL_SENDER
    server.sendmail(settings.EMAIL_SENDER, settings.EMAIL_RECIPIENT, message.as_string())


if __name__ == '__main__':
    # DO NOT USE IN PRODUCTION!
    uvicorn.run('main:app',
                host=str(settings.HOST),
                port=settings.PORT,
                # workers=workers,
                debug=settings.DEBUG,
                reload=True)
