import random
import time

while True:
    currTemp = random.randint(0, 50)
    currHum = random.randint(0, 100)

    print("Temperature right now: ", currTemp)
    print("Humidity right now: ", currHum)
    if currTemp > 37:
        print("High temperature! Alarm triggered!")
    
    print("------------------------------------")

    time.sleep(3)
    