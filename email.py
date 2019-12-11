import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp = "smtp.qq.com"
sender = "2282310940@qq.com"
receiver = "1328497946@qq.com"

# pwd = ""
pwd = ''
title = "早上好"
contents = "From Python-email: Hi"

try:
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
