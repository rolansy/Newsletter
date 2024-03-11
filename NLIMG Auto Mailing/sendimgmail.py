import csv,smtplib,ssl,urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

efrom="thenetxnewsletter@gmail.com"
passw="aoihclfynjgbhpfq"
msubj="NewsLetter"
tolist=r"D:\NetX\NetXweb\NL Auto Mailing\testcsv.csv"
newsimg=r"D:\NetX\Newsletter\public\download-1@2x.png"

msgroot=MIMEMultipart('related')
msgroot['Subject']=msubj
msgroot['From']=efrom
msgroot['To']=efrom
msgroot.preamble='This is a multi-part message in MIME format.'



msgalt=MIMEMultipart('alternative')
msgroot.attach(msgalt)

#html embedding
with open(r'D:\NetX\Newsletter\index.html', 'r',encoding='utf-8') as f:
    html_content = f.read()
# Create a MIMEText object with the HTML content
msghtml = MIMEText(html_content, 'html')


#msghtml=MIMEText(htmlnx, 'html')
msgalt.attach(msghtml)

fp=open(newsimg, 'rb')
msgimg1=MIMEImage(fp.read(),_subtype="png")
fp.close()

msgimg1.add_header('Content-ID', '<downimg>')
msgroot.attach(msgimg1)

context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(efrom, passw)
    with open(tolist) as file:
        reader=csv.reader(file)
        next(reader)
        for name,email in reader:
            mailmsg=msgroot.as_string().format(name=name)
            server.sendmail(efrom, email, mailmsg)