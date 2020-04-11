import smtplib, imghdr,os
from email.message import EmailMessage

#for multiple people add as list
emailuser = os.environ.get('EMAIL_USER')
emailpass = os.environ.get('EMAIL_PASS')

contacts =['rubarajankcs@hotmail.com']
msg = EmailMessage()
msg['Subject'] = "Test mail with attachment"
msg['From'] = "mrubarajan@gmail.com"
msg['To'] = contacts #'rubarajankcs@hotmail.com'
msg.set_content("This is a plain text email")

#alternative
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
<h2>HTML Links</h2>
<p>HTML links are defined with the a tag:</p>
<a href="https://www.w3schools.com">This is a link</a>
</body>
</html>
""",subtype='html'
)

#files =['puppy.jpg','puppy2.jpg']

files =['sample.pdf']

for file in files:
    with open(file,'rb') as pupimg:
        file_data = pupimg.read()
        # file_type = imghdr.what(pupimg.name)
        file_name = pupimg.name
    msg.add_attachment(file_data,maintype='application', subtype='octet-stream',filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.login("mrubarajan@gmail.com", "******")
    smtp.login(emailuser, emailpass)
    smtp.send_message(msg)

    # subject = "Test Subject"
    # body = "Testing the Body"
    # msg = f"Subject: {subject}\n\n{body}"
    # smtp.sendmail("mrubarajan@gmail.com", 'rubarajankcs@hotmail.com', msg)