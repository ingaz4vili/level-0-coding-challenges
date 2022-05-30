def common_letters(s1,s2):
    letters=list(set(s1.lower())&set(s2.lower()))
    print("Common letters:",end='')
    for i in letters:
        print(',',i,end=' ')
common_letters("house","COMPUTERS")