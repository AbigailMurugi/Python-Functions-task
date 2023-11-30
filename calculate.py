#create an app that takes temp. in degrees
#celsius and convert to farenheit
# (0°C × 9/5) + 32 = 32°F
celsius= input ("degrees in celcius: ")
#after the prompt, declare the input
#as a float
cf = float (celsius)
farenheit = (cf * 9/5) + 32
print(farenheit)
