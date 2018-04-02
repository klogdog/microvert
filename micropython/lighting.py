

from wifi import wifi_connect
from umqtt.simple import MQTTClient
import machine
import time
from machine import Pin



mqttServer = "mqttServer"
mqttPort = "1883"
mqttKeepAlive = 60
mqttUsername = "mqttUsername"
mqttPassword = "mqttPassword"
mqttTopic = "mqttTopic"
mqttClientID = "123456"
wifissid = "wifissid"
wifiPassword = "wifiPassword"
relayPin = Pin(5,Pin.OUT)
mqttTopic = "actuators/relay"


wifi_connect(wifissid,wifiPassword)

relayFlag = 0




def subscribeCallBack(topic, msg):
  global relayFlag
  if topic == b'actuators/relay':
    if msg == b'0':
      relayFlag = 0
    if msg == b'1':
      relayFlag = 1


try:
 client = MQTTClient("123456",mqttServer, port=1883, user= mqttUsername, password= mqttPassword)
 client.set_callback(sub_cb)
 client.connect()
 client.subscribe(mqttTopic)
except:
  print("connection error")
  time.sleep(5)
  machine.reset()
while True:
  try:
    client.check_msg()
  except:
    print("unhandled exception")
    time.sleep(5)
    machine.reset()
  if relayFlag == 1:
      relayPin.value(1)
  else:
      relayPin.value(0)
  time.sleep(10
