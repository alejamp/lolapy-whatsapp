
<p align="center">
  <img src="https://firebasestorage.googleapis.com/v0/b/numichat.appspot.com/o/Perf_Lola%2BH.way%20banner.png?alt=media&token=8a0dac42-1f76-4754-ac9c-40a93ba02125" alt="Logo">
</p>



# Lola v2 Python SDK Extension

This project is a Python SDK for the Prompter API. It is intended to be used by developers who want to integrate Lola into their own applications.

## Installation

``` pip install lolapy-whatsapp ```


# Examples

Check the examples folder for more examples

## Send a message

```python
PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )

connector.send_text_message("Hello World!", PHONE)
```


## Send reply buttons

```python
PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )


button1 = ReplyButton("id_yes", "Yes")
button2 = ReplyButton("id_no", "No")

connector.send_button_reply("Header Testing", "Body Testing", [button1, button2], PHONE, footer="Footer Testing")
```

## Send link template

```python

PHONE = getenv("RECIPIENT_PHONE")

connector = WhatsappConnector(
                token=getenv("TOKEN"),
                phone_number_id=getenv("PHONE_NUMBER_ID")
            )


connector.send_template("lola_verify_account", PHONE, body_params=["Alejandro", "*email*"], button_params=["PAYLOAD"])
```














# Intall for dev locally

Create a virtual environment
```bash
python3.11 -m venv .venv
```

Then activate the virtual environment
```bash
source .venv/bin/activate
```
## For development purposes
```bash
pip install git+https://github.com/alejamp/whatsapp#egg=whatsapp-python
```


