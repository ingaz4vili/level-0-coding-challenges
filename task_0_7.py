def celsius_to_fahrenheit(fahrenheit):
    fahrenheit = (fahrenheit - 32) * 5 / 9
    return fahrenheit
def fahrenheit_to_celsius(celsius):
    celsius = (celsius * 9 / 5) + 32
    return celsius
fahrenheit = 21
celsius = 21
print(celsius_to_fahrenheit(fahrenheit),"Fahrenheit value")
print(fahrenheit_to_celsius(celsius),"Celsius value")




