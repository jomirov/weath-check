import ipinfo, os
from dotenv import load_dotenv

load_dotenv()

api_key_ip = os.getenv("API_KEY_IP")
handler = ipinfo.getHandler(api_key_ip)
details = handler.getDetails()

def getCity():
    return details.city