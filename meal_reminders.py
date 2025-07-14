from twilio.rest import Client
from dotenv import load_dotenv
import os, schedule, time
from datetime import datetime

load_dotenv()

SID = os.getenv("TWILIO_SID")
TOKEN = os.getenv("TWILIO_TOKEN")
FROM = os.getenv("TWILIO_PHONE")
TO = os.getenv("MY_PHONE")

client = Client(SID, TOKEN)

def send_meal_reminder(meal, eat_time):
    now = datetime.now().strftime("%I:%M %p")
    message = f"Hi Bhargav! It's {now} — Time to prep for {meal} at {eat_time}. 🍽️"
    client.messages.create(from_=FROM, to=TO, body=message)
    print("Sent:", message)

# Schedule meal reminders (edit times as needed)
schedule.every().day.at("07:00").do(send_meal_reminder, meal="Breakfast", eat_time="8 AM")
schedule.every().day.at("09:30").do(send_meal_reminder, meal="Mid-Morning Snack", eat_time="10:30 AM")
schedule.every().day.at("12:00").do(send_meal_reminder, meal="Lunch", eat_time="1 PM")
schedule.every().day.at("16:30").do(send_meal_reminder, meal="Evening Snack", eat_time="5:30 PM")
schedule.every().day.at("18:30").do(send_meal_reminder, meal="Dinner", eat_time="7:30 PM")
schedule.every().day.at("20:00").do(send_meal_reminder, meal="Bedtime Snack", eat_time="9 PM")

while True:
    schedule.run_pending()
    time.sleep(30)
