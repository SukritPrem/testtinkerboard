
import time
import urequests


    
def controlrelay():
    print('*************')
    url = 'https://api.thingspeak.com/channels/1833628/feeds.json?api_key=C2UWYL5UJQ5VB1N2&results=2'
    print(url)
    response = urequests.get(url)
    
def run():
        controlrelay()
        
        
while True:
    run()