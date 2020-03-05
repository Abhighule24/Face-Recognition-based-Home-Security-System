import imghdr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

def FDSendMail(dt,x):
    fromaddr = 
    toaddr = 
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "STRANGER NOTIFICATION"
    
    body = ("%s HAS ARRIVED AT YOUR DOORSTEP"%x)
    
    msg.attach(MIMEText(body, 'plain'))
    filename="DetectImg/"+dt+".png"
    attachment = open(filename,"rb")
    header="PHOTO "+dt+".png"
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % header)
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr," ")#password
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("MAIL SENT TO: "+toaddr)
    with open("MailLog.txt",'a') as f:
        f.write("Mail sent to abhighule24@gmail.com at %s \n"%dt)

def NFDSendMail(dt):
    fromaddr = 
    toaddr = 
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "STRANGER NOTIFICATION"
    
    body = "UNKNOWN PERSON HAS ARRIVED AT YOUR DOORSTEP"
    
    msg.attach(MIMEText(body, 'plain'))
    filename="CapImg/"+dt+".png"
    attachment = open(filename,"rb")
    header="PHOTO"+dt+".png"
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % header)
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("MAIL SENT TO: "+toaddr)
    with open("MailLog.txt",'a') as f:
        f.write("Mail sent at %s \n"%dt)
