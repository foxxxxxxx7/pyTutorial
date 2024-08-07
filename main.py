import smtplib

sender= "pytut45@gmail.com"
receiver= "rob.fox7@hotmail.com"
password= "Passw0rd123!"
subject= "Email Subject"
body= "Email Body"

message=f"""From: Sender Fox {sender}
To: Reciever Fox {receiver}
Subject: {subject}\n
{body}
"""

server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in!")