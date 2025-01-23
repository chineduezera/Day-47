import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from twilio.rest import Client
load_dotenv(".env")

AMAZON_URL = "https://www.amazon.com/Google-Smartwatch-Compatible-Cellular-Packaging/dp/B0DLLBVWXX/ref=sr_1_6?crid=ALV0FWSCZCBW&dib=eyJ2IjoiMSJ9.b4NCX5O8kblLVx09aH6ty9PRAmsbf881zDMqgg7XdYLLCSntQwVp4qcWHBDcWwJGg2dJR8x4DCsNBjOZfIuzuTMR3XXqwMirHrxRfN9C4tLK4fyNB8oEuCy0I0GnyWEvcWudeppXxocoHOe4pELBVQDbqmA4NcgY0t7rCEsGpHt2_I3-lG0rmpJ-P1mnuIfoa58pP1ycG94t_5YeI1oNdHEVVtGX0qr3zEbWRHtcCP4.J-hwnaUeIUer79tmr_AqttM9N74zjoqMnEuVbMYMKac&dib_tag=se&keywords=pixel%2Bwatch&qid=1737655343&sprefix=pixel%2Bwatch%2Caps%2C327&sr=8-6&th=1"

amazon_response = requests.get(url = AMAZON_URL, headers= os.getenv("HEADERS"))
amazon_data = amazon_response.text
soup = BeautifulSoup(amazon_data, "html.parser")
find_price = soup.find(name = "span", class_="a-price-whole")
price = find_price.text.split(".")[0]

def send_message(message):
    account_sid = os.getenv("TW_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body= message,
        from_="whatsapp:+14155238886",
        to=os.getenv("CONTACT"),
    )
    return message.status

if int(price) < 100:
    message = "The price of the Pixel Watch is now below $100. Buy it now!"
    status = send_message(message)
    print(status)
else:
    message = "The price of the Pixel Watch is still above $100"
    status = send_message(message)
    print(status)
    