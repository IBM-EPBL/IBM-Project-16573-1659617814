import random
temprature=random.sample(range(30,50),1)
print("Temprature is",temprature)
if(temprature>=[45]):
    print("High Temprature")
    print("Alarm is on")
else:
    print("Temprature is Normal")
humidity=random.sample(range(30,50),1)
print("Humidity is",humidity)
if(humidity>=[50]):
    print("Humidity level is High")
else:
    print("Humidity level is Low")
soil_moisture=random.sample(range(30,60),1)
print("Soil Moisture is",soil_moisture)
if(soil_moisture>=[50]):
    print("Soil Moisture level is Normal")
else:
    print("Soil Moisture level is Low")
    print("Water Pump is on")
    
