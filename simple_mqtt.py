import random
import time
from  Adafruit_IO import  MQTTClient


AIO_USERNAME = "vnmduy2002"
AIO_KEY = "aio_hEkU80xjFwFZj1zJDFZC8joulk4n"


client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.connect()
client.loop_background()
time.sleep(5)

while True:
    value = random.randint(0, 100)
    client.publish("testing", value)
    time.sleep(30)