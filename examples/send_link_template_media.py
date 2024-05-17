import logging
from os import getenv
from dotenv import load_dotenv
from lolapy_whatsapp.wasap import WhatsappConnector
from lolapy_whatsapp.wasap import Image, Text


logging.basicConfig(level=logging.INFO)

load_dotenv("./examples/.env")

PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )

img1 = Image("https://i.imgur.com/Fh7XVYY.jpeg")
img2 = Image("https://firebasestorage.googleapis.com/v0/b/numichat.appspot.com/o/test_images%2F1_ENG.jpg?alt=media&token=99f80dcd-fbde-4b85-81dc-60b794741897")
text = Text("123")

# connector.send_template("link_multimedia", PHONE, header_params=[str(img1)], button_params=[text], lang="en_US")
connector.send_template("link_multimedia", PHONE, header_params=[str(img2)], button_params=[text], lang="en_US")