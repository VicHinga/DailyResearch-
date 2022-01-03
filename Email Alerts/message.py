# Email and Text message alerts
# myaccount.google.com -> security ->

import smtplib
from email.message import EmailMessage


# Structure of the message:
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to


    user = "vitukubwa1@gmail.com"
    msg["from"] = user
    # Original password "906vitukubwa"
    password = "bhohaoixlwopvydm"

    # 587 is the port Number
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

# If this is the actual main program, run the code that follows
if __name__ == "__main__":
    email_alert("Hey","Hello Hope You are well","vicmhinga@gmail.com")

