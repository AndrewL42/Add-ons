import smtplib
import datetime
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

date_and_time = datetime.datetime.now()
date = (date_and_time.strftime("%Y-%m-%d %H-%M"))
full_date = ((date_and_time.strftime("%Y-%m-%d %H:%M:%S")))

file_name = str(date + ".csv")

email_from = ""
email_to = ""
password = ""

msg = MIMEMultipart()
msg["From"] = email_from
msg["To"] = email_to
msg["Subject"] = "Test attachment"

body = "Lets see if we can send an attachment!"
msg.attach(MIMEText(body, 'plain'))

attachment = open(file_name, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
attachment.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_from, password)
text = msg.as_string()
server.sendmail(email_from, email_to, text)
server.quit()