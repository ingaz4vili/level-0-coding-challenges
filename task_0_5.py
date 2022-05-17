def area_triangle(num1, num2, num3):
    num = (num1 + num2 + num3) / 2
    area = (num * (num - num1) * (num - num2) * (num - num3)) ** 0.5
    return area
print (area_triangle(2,6,7))

