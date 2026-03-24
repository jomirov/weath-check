import ipinfo, os
from dotenv import load_dotenv

load_dotenv()

ip_api_key = os.getenv("API_KEY_IP")
handler = ipinfo.getHandler(ip_api_key)
details = handler.getDetails()

def getCity():
    return details.city