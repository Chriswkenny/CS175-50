#Declaring variables:
statement1 = "Temperature (Fahrenheit):"
statement2 = "Temperature (Celsius):"
statement3 = "Wind Speed (mph):"
statement4 = "Wind Direction:"

#User Inputs
weather_station = input("Weather Station Name: ")
weather_station_name = weather_station + " Weather Station"
current_temp = float(input("What is the current temperature (Fahrenheit)? "))
wind_speed = int(input("What is the wind speed? "))
wind_direction = input("What is the wind direction? ")

#Converting Fahrenheit to Celcius
current_tempC = (current_temp - 32) * 5/9

#Displays to Users
print()
print(f"{weather_station_name:^80}")
print()
print(f"{statement1:>50} {current_temp:<5.1f}")
print(f"{statement2:>50} {current_tempC:<5.1f}")
print(f"{statement3:>50} {wind_speed:<5}")
print(f"{statement4:>50} {wind_direction:<5}")
