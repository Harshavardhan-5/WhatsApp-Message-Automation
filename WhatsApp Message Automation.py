from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step-2 twilio credential
account_sid = 'ACb8d861ba04634d28e169e40985d02e08'
auth_token = '1b77c42a96d2fde5b5ac82c6b1df5480'

client = Client(account_sid, auth_token)

#step-3 degine send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID{message.sid}")
    except Exception as e:
        print("An error occurred")

#step-4 user input
name = input("Enter the recipient name = ")
recipient_number = input("Enter the recipient Whatapp number with country code: ")
message_body = input(f"Enter the message you want to sent to {name}: ")

#step - 5 parse date/time and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message(HH:MM in 24hour format): ")
b
#datetime
schedule_datetime = datetime.strptime(f"{date_str} {time_str}","%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_second = time_difference.total_seconds()

if delay_second <=0:
    print("The specified time is in the past. Please enter a future and time: ")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

#wait until the scheduled time
time.sleep(delay_second)#1000

#send the message
send_whatsapp_message(recipient_number,message_body)


