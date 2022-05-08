
def conv_fah(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print ("Celsius Tempreture",celsius)
conv_fah(45)
    
def conv_ce(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print ("Fahrenheit Tempreture",fahrenheit)
conv_ce(45)