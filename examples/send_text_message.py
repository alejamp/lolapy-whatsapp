import logging
from os import getenv
from dotenv import load_dotenv
from lolapy.wasap import WhatsappConnector


logging.basicConfig(level=logging.INFO)


load_dotenv("./examples/.env")

PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )

connector.send_text_message("Hello World!", PHONE)
