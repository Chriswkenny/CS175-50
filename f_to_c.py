# CS 175
# Christopher Kenny
# Problem 4

#Allow user to enter given temperature
temp = int(input("Enter the temperature in Farenheit you would like converted to Celcius: "))

#Conversion Formula
celcius = (temp - 32) * 5/9

#Output to User
print(f"{temp}°F converted to celcius is {celcius}°C")
