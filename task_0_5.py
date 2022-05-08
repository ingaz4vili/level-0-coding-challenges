def area_of_triangle(num1,num2,num3):
       num = (num1 + num2 + num3) / 2
       Area = (num*(num-num1)*(num-num2)*(num-num3)) ** 0.5
       print ("The Area of a Triangle is: ",Area)
       return Area
area_of_triangle(5,6,7)