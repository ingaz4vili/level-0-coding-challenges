def common_letters(s1,s2):
    str1=s1.lower()
    str2=s2.lower()
    letter = list()
    print("Common letters:",end='')
    for i in str2:
        if  i in str1:
           letter.append(i) 
    print(','.join(letter),end='')
common_letters("house","COMPUTERS")