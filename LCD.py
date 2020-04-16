#LCD with a fixed height
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

    
#LCD with changeable height
def LCD(num,height=1,width=1):
    numlist = list(str(num))    
    line1 = [" _ ","   "," _ "," _ ","   "," _ "," _ "," _ "," _ "," _ "]
    lin1x = ["| |","  |","  |","  |","| |","|  ","|  ","  |","| |","| |"]
    line2 = ["| |","  |"," _|"," _|","|_|","|_ ","|_ ","  |","|_|","|_|"]
    lin2x = ["| |","  |","|  ","  |","  |","  |","| |","  |","| |","  |"]
    line3 = ["|_|","  |","|_ "," _|","  |"," _|","|_|","  |","|_|"," _|"]
    line1print = ''
    line2print = ''
    line3print = ''
    line1xprint = ''
    line2xprint = ''
    for i in range(0,len(numlist)):
        line1print = line1print + line1[int(numlist[i])]
        line2print = line2print + line2[int(numlist[i])]
        line3print = line3print + line3[int(numlist[i])]
        line1xprint = line1xprint + lin1x[int(numlist[i])]
        line2xprint = line2xprint + lin2x[int(numlist[i])]
    
    print(line1print)
    for i in range(1,height):
        print(line1xprint)
    print(line2print)
    for i in range(1,height):
        print(line2xprint)
    print(line3print)
