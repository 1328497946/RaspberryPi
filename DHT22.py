import Adafruit_DHT
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sensor=Adafruit_DHT.DHT22
gpio=4
count=0

smtp = "smtp.qq.com"
sender = "2282310940@qq.com"
receiver = "1328497946@qq.com"

pwd = ''
title = "树梅派温度传感器传送"
while True:
    try:
        if count>=1:
            break
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        if humidity is not None and temperature is not None:
            contents = "早上好，今天室内温度={0:0.1f}*C 湿度={1:0.1f}%".format(temperature, humidity)
        else:
            print("failed to get reading. Try again!")
        time.sleep(3)
        count+=1
        message = MIMEText(contents, "plain", "utf-8")
        message['From'] = Header(sender, "utf-8")
        message['To'] = Header(receiver, "utf-8")
        message['Subject'] = Header(title, "utf-8")
        opt = smtplib.SMTP_SSL(smtp, 465)
        opt.login(sender, pwd)
        opt.sendmail(sender, receiver, message.as_string())
        opt.quit()
        print("邮件发送成功")
    except Exception as e:
        print(e)
