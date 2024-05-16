from abc import ABC
import logging
from os import getenv
from .wc_reply_button import ReplyButton
from whatsapp import WhatsApp, Message
from dotenv import load_dotenv
import json



class WhatsappConnector:
    
    def __init__(self, token: str, phone_number_id: str, verify_token: str | None = None) -> None:
        self.token = token
        self.phone_number_id = phone_number_id
        self.verify_token = verify_token
        
        self.messenger = WhatsApp(
                    token=self.token,
                    phone_number_id=self.phone_number_id,
                    verify_token=self.verify_token
                )
        
    def send_text_message(self, message: str, phone: str) -> None:
        msg = Message(instance=self.messenger, content=message, to=phone)
        response = msg.send()
        return response
    
    def send_button_reply(self, header: str, body: str | None, buttons: list[ReplyButton], phone: str, footer: str | None = None) -> None:
        response = self.messenger.send_reply_button(
            recipient_id=phone,
            button={
                "type": "button",
                "header": {"type": "text", "text": header},
                "body": {"text": body} if body else None,
                "footer": {"text": footer} if footer else None,
                "action": {
                    "buttons": [json.loads(str(button)) for button in buttons]
                }
            }
        )
        
    def send_template(self, 
                      template_name: str, 
                      phone: str,
                      lang: str = "en_US",
                      header_params: list[str] | None = None, 
                      body_params: list[str] | None = None, 
                      button_params:list[str] | None = None, 
                      footer_params: list[str] | None = None) -> None:
                
        components = []
        
        if header_params:
            components.append({
                "type": 'header',                
                "parameters": [{"type": 'text', "text": param} for param in header_params]
            })
        if body_params:
            components.append({
                "type": 'body',
                "parameters": [{"type": 'text', "text": param} for param in body_params]
            })
        if button_params:
            components.append({
                "type": 'button',
                "sub_type": "url",
                "index": "0",                
                "parameters": [{"type": 'text', "text": param} for param in button_params]
            })
        if footer_params:
            components.append({
                "type": 'footer',
                "parameters": [{"type": 'text', "text": param} for param in footer_params]
            })
        
        json_components = json.dumps(components)
        response = self.messenger.send_template(template_name, phone, components=json_components, lang=lang)
        return response


    def send_image(self, phone: str, image_url: str, caption: str | None = None) -> None:
        response = self.messenger.send_image(image_url, phone, caption=caption)
        return response

    def get_messanger(self) -> WhatsApp:
        return self.messenger


if __name__ == "__main__":
    
        # set logging level to info
    logging.basicConfig(level=logging.INFO)

    

    load_dotenv("./examples/.env")

    PHONE = getenv("RECIPIENT_PHONE")
    connector = WhatsappConnector(
                    token=getenv("TOKEN"),
                    phone_number_id=getenv("PHONE_NUMBER_ID"),
                    verify_token="123"
                )
    
    # connector.send_text_message("Hello World!", PHONE)
    
    button1 = ReplyButton("id_yes", "Yes")
    button2 = ReplyButton("id_no", "No")

    connector.send_button_reply("Header Testing", "Body Testing", [button1, button2], PHONE, footer="Footer Testing")
    # connector.send_button_reply("Header Testing", "Body Testing", [button1, button2], PHONE)
    
    # connector.send_template("lola_verify_account", PHONE, body_params=["Alejandro", "*email*"], button_params=["PAYLOAD"])
