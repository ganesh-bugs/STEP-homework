def LCD(num):
    numlist = list(str(num))    
    line1 = [" _ ","   "," _ "," _ ","   "," _ "," _ "," _ "," _ "," _ "]
    line2 = ["| |","  |"," _|"," _|","|_|","|_ ","|_ ","  |","|_|","|_|"]
    line3 = ["|_|","  |","|_ "," _|","  |"," _|","|_|","  |","|_|"," _|"]
    line1print = ''
    line2print = ''
    line3print = ''
    for i in range(0,len(numlist)):
        line1print = line1print + line1[int(numlist[i])]
        line2print = line2print + line2[int(numlist[i])]
        line3print = line3print + line3[int(numlist[i])]
    print(f'{line1print}\n{line2print}\n{line3print}')