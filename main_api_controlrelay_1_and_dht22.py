
from machine import Pin
from time import sleep
import network
import time
import urequests
import config

relay = Pin(26, Pin.OUT)

def connect_wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to WiFi...')
        sta_if.active(True)
        sta_if.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not sta_if.isconnected():
            time.sleep(1)
    print('Network config:', sta_if.ifconfig())


def read_sensor1():
    global temp, temp_percentage, hum
    temp = temp_percentage = hum = 0
    try:
        sensor1.measure()
        temp = sensor1.temperature()
        hum = sensor1.humidity()
      
        if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
            msg = (b'{0:3.1f},{1:3.1f}'.format(temp, hum))

            temp_percentage = (temp+6)/(40+6)*(100)
            # uncomment for Fahrenheit
            #temp = temp * (9/5) + 32.0
            #temp_percentage = (temp-21)/(104-21)*(100)

            hum = round(hum, 2)
            return(temp,hum)
        else:
            return('Invalid sensor readings.')
    except OSError as e:
        return('Failed to read sensor.')


def log_data(temperature, humidity):
    print('Invoking log webhook')
   
    url = config.WEBHOOK_URL.format(temperature=temperature,
                                    humidity=humidity,relay=relay)
    print(url)
  #  print('*************')

    response = urequests.get(url)
    
  #  print('*************')
    if response.status_code < 400:
        print('Webhook invoked')
        time.sleep(20)
        response.close()
    else:
        print('Webhook failed')
        raise RuntimeError('Webhook failed')


def log_data1(relay2):
    print('Invoking log webhook')
    response.close()
    url = config.WEBHOOK_URL.format(relay=relay2)
    print(url)
  #  print('*************')

    response = urequests.get(url)
    
  #  print('*************')
    if response.status_code < 400:
        print('Webhook invoked')
        time.sleep(20)
        response.close()
    else:
        print('Webhook failed')
        raise RuntimeError('Webhook failed')
    
def controlrelay():
    print('*************')
    url = config.WEBHOOK_URL2
    print(url)
    response = urequests.get(url)
    a = response.text 
    print(a[360])
    b = int(a[360])
    print(b==1)
    if(b==2):
        # RELAY ON
        relay(1)
        response.close()
    else:
        # RELAY OFF
        relay(0)
        response.close()

def run():
    try:
        connect_wifi()
        temperature, humidity = read_sensor1()
        log_data(temperature, humidity)
        print(read_sensor1())
        controlrelay()
    except Exception as exc:
        print('error')
     
    
while True:
    run()