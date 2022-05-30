def convert(number):
    num1 = 60
    num2 = 1 
    hour = number // num1 
    minutes = number % num1
    if hour == num2 and minutes == num2:
        print(f'{hour} hour, {minutes} minute')
    elif hour > num2 and minutes == num2:
         print(f'{hour} hours, {minutes} minute') 
    elif minutes > num2 and hour == num2:
        print(f'{hour} hour, {minutes} minutes')
    elif minutes == num2 and hour == num2:
            print(f'{hour} hour, {minutes} minutes')
    else:
        print(f'{hour} hours, {minutes} minutes')
convert(1)


 
      
