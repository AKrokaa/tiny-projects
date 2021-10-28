from datetime import date
from datetime import datetime
import python_weather
import asyncio
import time
import warnings
import calendar

warnings.filterwarnings("ignore")

now = datetime.now()
today = date.today()
hour = int(now.strftime("%H"))
curr_date = date.today()

name = input("What's your name?\n= ")

def timeofday(x):
    if x > 6 and x <= 12:
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return'Afternoon'
    elif (x > 16) and (x <= 24):
        return 'Evening'
    elif (x > 24) and (x <= 6):
        return 'Night'

print(f"Good {timeofday(hour)}, {name}\n")

time.sleep(2)

clock = now.strftime("%H:%M:%S")
print("It's currently:", clock)

datetoday = today.strftime("%B %d, %Y")
print("The date is:", datetoday, "\n")

time.sleep(1)

async def getweather():
    client = python_weather.Client(format=python_weather.IMPERIAL)
    
    weather = (await client.find("Horten"))
    currentTemp = float(f'{(weather.current.temperature - 32) * 0.5556:.1f}')


    print(f"The temperature right now is", currentTemp, "degrees celcius")
    if currentTemp >= 16:
        print("It's pretty hot out right now, remember to drink water!")
    elif  currentTemp < 16:
        print("It's a little chilly out, remember to wear enough clothes!")

    time.sleep(1)

    print("\nThe weather forecast for the next five days are:\n")

    for forecast in weather.forecasts:
        print(
            str(
            calendar.day_name[forecast.date.weekday()]),
            forecast.sky_text, 
            f'{(forecast.temperature - 32) * 0.5556:.1f}', "°C")

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())