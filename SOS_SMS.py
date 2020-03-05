import imaplib
import TwilioSMS
def SendMsg():
    # Login to INBOX
    username=
    password=
    sender_of_interest=
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    imap.login(username, password)
    imap.select('INBOX')
    
    status, response = imap.search(None, '(UNSEEN)')
    unread_msg_nums = response[0].split()

    # Print all unread messages from a certain sender of interest
    status, response = imap.search(None, '(UNSEEN)', '(FROM "%s")' % (sender_of_interest))
    unread_msg_nums = response[0].split()
    da = []
    for e_id in unread_msg_nums:
        _, response = imap.fetch(e_id, "(BODY[HEADER.FIELDS (SUBJECT)])")
        da.append(response[0][1])
        try:
            if response[0][1]==b'Subject: sos\r\n\r\n':
                print("[SOS] MESSAGE SENT TO POLICE")
                TwilioSMS.SendSMS()
        except:
            print("NO MAIL RECEIVED")  
    # Mark them as seen
    for e_id in unread_msg_nums:
        imap.store(e_id, '+FLAGS', '\Seen')
