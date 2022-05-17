def celsius_to_fahrenheit(temperature_01):
    temperature_01 = (temperature_01 - 32) * 5 / 9
    return temperature_01
def fahrenheit_to_celsius(temperature_02):
    temperature_02 = (temperature_02 * 9 / 5) + 32
    return temperature_02
temperature_01 = 21
temperature_02 = 21
print("Fahrenheit value:",celsius_to_fahrenheit(temperature_01))
print("Celsius value:",fahrenheit_to_celsius(temperature_02))




