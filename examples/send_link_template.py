import logging
from os import getenv
from dotenv import load_dotenv
from lolapy_whatsapp.wasap import WhatsappConnector
from lolapy_whatsapp.wasap import ReplyButton
from lolapy_whatsapp.wasap.components.image import Image


logging.basicConfig(level=logging.INFO)

load_dotenv("./examples/.env")

PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )

img = Image("https://i.imgur.com/Fh7XVYY.jpeg")

connector.send_template("lola_verify_account", PHONE, body_params=["Alejandro", "*email*"], button_params=["PAYLOAD"], lang="en_US")