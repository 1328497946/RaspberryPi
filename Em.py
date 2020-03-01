import Adafruit_SSD1306
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from poplib import POP3
from email.parser import Parser
RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width=disp.width
height=disp.height
font=ImageFont.load_default()

class Email_Yao:
    def __init__(self):
        self.user = '2282310940@qq.com'
        self.pass_ = 'vbddzghqiqhxdiej'
        self.pop_address = 'pop.qq.com'

    def get_email(self):
        try:
            pop = POP3(self.pop_address)
            pop.user(self.user)
            pop.pass_(self.pass_)
        except Exception as e:
            pop = e.__str__()
            return pop
        emails = pop.stat()[0]
        status, msg_content, weight = pop.retr(emails)
        msg_content = b'\r\n'.join(msg_content).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        title = msg.get('Subject', "该邮件没有标题")
        pop.quit()
        return title

while True:
    count=0
    try:
        print('start')
        ema=Email_Yao()
        message=ema.get_email()
        print(message)
        image=Image.new('1', (width,height),color=0)
        draw=ImageDraw.Draw(image)
        draw.text((4,4),text='Lastest Email title:',fill=255)
        draw.text((4,14),text=message,fill=255, align='left', spacing=4)
        # draw.text((4,24),text='Refresh %d times'%count, fill=255)
        disp.image(image)
        disp.display()
    except Exception as e:
        print(e)
    finally:
        time.sleep(60)
        count+=1

