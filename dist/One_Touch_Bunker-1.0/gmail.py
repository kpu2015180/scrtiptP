# -*- coding: utf-8 -*-
import mimetypes
import mysmtplib
import framework
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication



def sendMail(Shelter,reciever):
    string="도로명 주소 : "+Shelter.rddr+"\n"
    string+="지번 주소 : "+Shelter.addr+"\n"
    string+="시설명 : "+Shelter.facility_name+"\n"

    imageFileName = "Shild.png"

    # global value
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    #htmlFileName = "ShildMap.html"

    senderAddr = "ehdrpakt@gmail.com"  # 보내는 사람 email 주소.
    recipientAddr = reciever  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")

    a =MIMEText(string)
    msg['Subject'] = "대피소 정보"  # 제목
    msg['From'] = senderAddr
    msg['To'] = recipientAddr





    # MIME 문서를 생성합니다.
    #htmlFD = open(htmlFileName, 'rb')
    #HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
    #htmlFD.close()

    imageFD = open(imageFileName, 'rb')
    ImagePart = MIMEImage(imageFD.read())
    imageFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    #msg.attach(HtmlPart)
    msg.attach(a)
    msg.attach(ImagePart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("ehdrpakt@gmail.com", "ssiber12")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    pass







































