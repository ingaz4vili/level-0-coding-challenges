def convert(number):
    hour = number // 60 
    minutes = number % 60
    if hour == 1 and minutes == 1:
        print(f'{hour} hour, {minutes} minute')
    elif hour > 1 and minutes == 1:
         print(f'{hour} hours, {minutes} minute') 
    elif minutes > 1 and hour == 1:
        print(f'{hour} hour, {minutes} minutes')
    else:
        print(f'{hour} hours, {minutes} minutes')
convert(133)


 
      
