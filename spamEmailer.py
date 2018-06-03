import smtplib
import csv
from email.mime.text import MIMEText
#using Gmail server
s = smtplib.SMTP('smtp.gmail.com', 587)
s.set_debuglevel(1)
s.ehlo()
s.starttls()
s.ehlo()
s.login("<EMAIL>", "<PASSWORD>")
sender = '<name>'
with open('thing.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        #assuming the email address is in the first column of csv
        recipient = row[0]
        #assuming the name is in the second column of the csv
        msg = MIMEText("Your child, {} is a nice person.".format(row[1]))
        msg['Subject'] = "Have a lovely day"
        msg['From'] = sender
        msg['To'] = recipient
        s.sendmail(sender, recipient, msg.as_string())
