def second_largest(a,b,c):
    #checking if all 3 numbers are equal
    if (a==b==c):
        print('All are equal')
    #checking is any two numbers are equal
    elif (a==b) or (b==c) or (a==c):
    #assigning them to a list
        list1=[a,b,c]
    #sorting them in the list
        list1.sort()
    #comparing the first and second value to arrive at the second largest
        if list1[1]>list1[0]:
            print(f'{list1[0]} is the second largest')
        else:
            print(f'{list1[1]} is the second largest')
    #conditions for when all numbers are different
    elif (a>b):
        if (b>c):
            print(f'{b} is the second largest')
        elif (a>c):
            print(f'{c} is the second largest')
        else:
            print(f'{a} is the second largest')
    else:
        if (b<c):
            print(f'{b} is the second largest')
        elif (a>c):
            print(f'{a} is the second largest')
        else:
            print(f'{c} is the second largest')