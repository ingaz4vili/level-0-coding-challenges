def common_letters(s1,s2):
    letters=list(set(s1)&set(s2))
    print("The common letters:")
    for i in letters:
        print(i,end=" ")
common_letters("house","computers")