from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo
from base64 import b85encode
import requests, os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)


def getCurrDate():
    now = datetime.now()
    now = now.replace(tzinfo=ZoneInfo("America/New_York"))
    return now


def sendAlert(e):
    now = getCurrDate()

    message = Mail(
        from_email="a@example.com",
        to_emails=["b@example.com", "c@example.com"],
        subject="LAWN Data Collection box error",
        html_content="<strong>Hello, Course registration is open.</strong><br/>Open at:"
        + now.strftime("%m/%d/%Y, %H:%M:%S")
        + str(e),
    )

    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


def send_image(image):
    try:
        url = "http://127.0.0.1:5000/image"
        body = {"img": b85encode(image).decode()}
        response = requests.post(
            url,
            headers={
                "accept": "application/json, text/plain, */*",
                "content-type": "application/json",
            },
            json=body,
        )

        app.logger.info(response)

        return {}

    except Exception as e:
        app.logger.error(e)
        sendAlert(e)
        return {}


if __name__ == "__main__":
    with open("tree.jpg", "rb") as img:
        send_image(img.read())
