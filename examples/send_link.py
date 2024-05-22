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


    
res = connector.send_link(
    image_url="https://firebasestorage.googleapis.com/v0/b/numichat.appspot.com/o/Raas%2FTemplate_images%2F2_ENG.jpg?alt=media&token=7a323913-8c57-4977-9147-3fb9b2a66d6a", 
    link_label="Book Now",
    body="Tap the button below to see available dates.", 
    link="https://www.google.com", 
    phone=getenv("RECIPIENT_PHONE"), 
    footer="Dates subject to change."
)

print(res)