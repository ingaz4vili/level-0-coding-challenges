num1=1
num2=22
num3=3
num4=2
def maxi():
    if(num1>=num2) and (num1>=num3) and (num1>=num4):
        high_num=num1
    elif(num2>=num1) and (num2>=num3) and (num2>=num4):
         high_num=num2
    elif(num3>=num1) and (num3>=num3) and (num3>=num4):
             high_num=num2
    else:
         high_num=num4
    print("Largest number is",high_num)
maxi()