def area_triangle(semiperimeter1, semiperimeter2, semiperimeter3):
    tota_semiperimeter = (semiperimeter1 + semiperimeter2 + semiperimeter3) / 2
    area = (tota_semiperimeter * (tota_semiperimeter - semiperimeter1) * (tota_semiperimeter - semiperimeter2) * (tota_semiperimeter - semiperimeter3)) ** 0.5
    return area
print (area_triangle(2,6,7))

