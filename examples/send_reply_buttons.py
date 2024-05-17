import logging
from os import getenv
from dotenv import load_dotenv
from lolapy_whatsapp.wasap import WhatsappConnector
from lolapy_whatsapp.wasap import ReplyButton



logging.basicConfig(level=logging.INFO)

load_dotenv("./examples/.env")

PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )


button1 = ReplyButton("id_yes", "Yes")
button2 = ReplyButton("id_no", "No")


connector.send_button_reply("Header Testing", "Body Testing", [button1, button2], PHONE, footer="Footer Testing")
# connector.send_button_reply("Header Testing", "Body Testing", [button1, button2], PHONE)