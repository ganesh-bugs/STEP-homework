#program to print fibonacci series until a given term:
num = int(input("How many terms do you want to print?"))
num1 = 0
num2 = 1
factlist = [0,1]
for i in range(1,num-1):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    factlist.append(num3)
print(factlist)