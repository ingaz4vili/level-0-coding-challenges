def maxi(num1,num2,num3):
    if(num1>=num2) and (num1>=num3):
        high_num=num1
    elif(num2>=num1) and (num2>=num3):
         high_num=num2
    elif(num3>=num1) and (num3>=num3):
             high_num=num3
    return high_num
print (maxi(2,4,2))