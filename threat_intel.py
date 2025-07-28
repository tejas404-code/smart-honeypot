import requests

def check_ip(ip):
    headers = {"Key": "YOUR_ABUSEIPDB_API_KEY"}
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90"
    response = requests.get(url, headers=headers)
    return response.json()