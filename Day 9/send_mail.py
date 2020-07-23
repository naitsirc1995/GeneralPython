import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'mlpm.cristian.unal@gmail.com'
password = 'Cristian1995'

def send_mail(text = 'You know what, this is nice !', subject = 'Hello World',to_emails = None,from_email = 'Cristian Chavez <mlpm.cristian.unal@gmail.com>', password = 'Cristian1995',html = None):
    assert isinstance(to_emails,list)

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject 

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:    
        html_part = MIMEText(html,"<h1><This is working/h1>",'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    
    #login to my smpt server
    server = smtplib.SMTP(host = 'smtp.gmail.com',port = 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()
    return 1
    