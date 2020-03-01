import Adafruit_SSD1306
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import Adafruit_DHT
import time

sensor=Adafruit_DHT.DHT22
gpio=4
count=0

RST = None
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
font = ImageFont.load_default()
while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
        if humidity is not None and temperature is not None:
            contents1 = "Temperature:{0:0.1f}".format(temperature)
            contents2 = "Humidity{0:0.1f}".format(humidity)
        else:
            content1 = "failed to get reading. Try again!"
            content2 = 'Mr.Yao'
        # print(contents)
        image = Image.new('1', (width, height), color=0)
        draw = ImageDraw.Draw(image)
        draw.text((4, 2), text=contents1, fill=255)
        draw.text((4, 12), text=contents2, fill=255)
        disp.image(image)
        disp.display()
    except Exception as e:
        print(e)
    finally:
        time.sleep(5)
