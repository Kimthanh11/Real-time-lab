#pip install adafruit-io
import random
import time
import  sys
from  Adafruit_IO import  MQTTClient


AIO_USERNAME = "lhkthNH"
AIO_KEY = "aio_suds157VVkEq9sXjDG59cDdrdfiA"


client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.connect()
client.loop_background()
time.sleep(5)

while True:
    value = random.randint(0, 100)
    client.publish("your_feed", value)
    time.sleep(30)