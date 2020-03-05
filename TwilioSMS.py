from twilio.rest import Client
def SendSMS():
    account_sid = 
    auth_token = 
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body='[SOS] Urgent HELP NEEDED!!!',
             from_='',
             to=''
         )
    print(message.sid)
