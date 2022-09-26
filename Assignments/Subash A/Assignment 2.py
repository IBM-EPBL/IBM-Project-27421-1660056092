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
    print("Current Humidity: ",currHumidity)
    
    if currTemp > 30:
        print("Warning!! Temperature is too high !!")
    if currHumidity < 20:
        print("Warning!! Humidity is too low !!")
    print("------------------------------------")
    time.sleep(2)    
    
