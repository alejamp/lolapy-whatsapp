import logging
from os import getenv
from dotenv import load_dotenv
from lolapy_whatsapp.wasap import WhatsappConnector
from lolapy_whatsapp.wasap import ReplyButton
from lolapy_whatsapp.wasap.components import Image, Text


logging.basicConfig(level=logging.INFO)

load_dotenv("./examples/.env")

PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )

text1 = Text("Alejandro")
text2 = Text("*email*")
text3 = Text("PAYLOAD")

connector.send_template("lola_verify_account", PHONE, body_params=[text1, text2], button_params=[text3], lang="en_US")