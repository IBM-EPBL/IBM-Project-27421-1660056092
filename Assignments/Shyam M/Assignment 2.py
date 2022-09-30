import random
import time

def getTemperature():
    return random.randint(0,50)
def getHumidity():
    return random.randint(0,100)

while(True):

    currTemp=getTemperature()
    currHumidity=getHumidity()
    
    print("Current Temperature: ",currTemp)
    if currTemp > 30:
        print("Temperature is too high !!")

    print("Current Humidity: ",currHumidity)
    if currHumidity < 20:
        print("Humidity is too low !!")

    print("------------------------------------")
    time.sleep(1)    
    
