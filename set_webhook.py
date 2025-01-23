import requests

# Replace this with your actual bot token from @BotFather
TOKEN = "7982424773:AAGVBimryPaPdz6FahB_zDQKuExHbIZ7khA"

# Replace with your actual deployed Vercel URL (without trailing slash)
WEBHOOK_URL = "hacknroll2025-tau.vercel.app/webhook"

# Make the request to set the webhook
response = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")

# Print the response from Telegram API
print(response.json())
