from email.mime import image
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import traceback
from email import encoders



class smtp(object):
    def __init__(self, from_, server, port, user, password):
        self.From = from_
        self.SMTP_Server = server
        self.port = port
        self.user = user
        self.password = password

    def sendmail(self, to, message, subject, typ, files=None, attachments=None):
        try:
            addrs = to
            msgRoot = MIMEMultipart('related')
            msgRoot['From'] = self.From
            msgRoot['To'] = to
            msgRoot['Subject'] = subject
            #msgRoot['Cco'] = ', '.join(addrs)

            msg = MIMEMultipart('alternative')
            typ = 'plain' if typ != 'html' else 'html'
            msg.attach(MIMEText(message, typ))
            msgRoot.attach(msg)

            sm = smtplib.SMTP(self.SMTP_Server, self.port)
            sm.starttls()

            if type(attachments) == type([]):
                for x, fil in enumerate(attachments):
                    filename = os.path.basename(fil)
                    attachment = open(fil, 'rb')
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',
                                    "attachment; filename= %s" % filename)
                    msgRoot.attach(part)
                    attachment.close()

            if type(files) == type([]):
                for x, fil in enumerate(files):
                    msgImage = MIMEImage(open(fil, 'rb').read())
                    msgImage.add_header('Content-ID', f"<{str(x)}>")
                    msgRoot.attach(msgImage)

            # sm.set_debuglevel(0)
            sm.login(self.user, self.password)
            sm.sendmail(msgRoot['From'], addrs, msgRoot.as_string())

            return {
                "Status": True,
                "Message": "OK",
                "Object": None,
                "Historic": []
            }
        except:
            return {
                "Status": False,
                "Message": traceback.format_exc(),
                "Object": None,
                "Historic": ["sendmail"]
            }

            #REQUIRE EMAIL, SMTP, PORT, USER, AND PASSWORD
smtp = smtp("teste@gmail.com",'smtp.gmail.com',587, "loginSMTPSEVER", "PASSWORD_SMTPSERVER")




def SetSubject(titulo):
    global td
    td = titulo


def SetBody(body):
    global corpo
    corpo = body


def SetImg(img):
    global image
    image = img


def SetPdf(pdf):
    global anexo
    anexo = pdf


def SetTo(dest):
    global to
    to = dest


def Send():
    global corpo
    global td
    global image
    global anexo
    global to

    a = smtp.sendmail(to, corpo, td, "html","", [anexo])
    return a["Message"]

