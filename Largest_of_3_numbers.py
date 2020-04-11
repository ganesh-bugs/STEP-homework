def largest(a,b,c):
    if a==b==c:
        return ("They are all equal")
    else:
        numlist = [a,b,c]
        numlist.sort()
        return numlist[2]  