import os
from dotenv import load_dotenv
import httpx

load_dotenv()

sms_api_username = os.getenv("SMS_API_USER")
sms_api_password = os.getenv("SMS_API_PASSWORD")
it_hjelp_stedkode = os.getenv("IT_HJELP_STEDKODE")



def send_sms(phone_number, message):
    url = "https://sms.uio.no/sms/send"
    data = {
        "b" : sms_api_username, #Brukernavn
        "p" : sms_api_password, #Passord
        "s" : it_hjelp_stedkode, #Stedkode
        "t" : phone_number,
        "m" : message
    }

    response = httpx.post(url, data=data)
    parsed = response.text.split("¤")

    if len(parsed) == 1:
        return {
            "status" : "failed",
            "success" : False,
            "error" : parsed[0]
        }

    return {
        "id" : parsed[0],
        "status" : parsed[1],
        "number" : parsed[2],
        "time" : parsed[3],
        "message" : parsed[6],
        "success" : True
    }



