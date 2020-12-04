# Naomi Ighodaro
# Code is given any date with month day and year as integers
#and then returns the corresponding day of the week that date occurred
#e.g Monday, Tuesday ...

import math

y=int(input("Enter the 4-digit year :"))
m=int(input("Enter the month as an integer :"))
d=int(input("Enter the day as an integer :"))


def getDayName(d):
    d=str(d)
          
    return d

def getMonthName(m):
    if m==1:
        m = "January"
    elif m==2:
        m = "February"
    elif m==3:
        m = "March"
    elif m==4:
        m = "April"
    elif m==5:
        m = "May"
    elif m==6:
        m = "June"
    elif m==7:
        m = "July"
    elif m==8:
        m = "August"
    elif m==9:
        m = "September"
    elif m==10:
        m = "October"
    elif m==11:
        m = "November"
    elif m==12:
        m = "December"

    return m 

def getDayNum(y,m,d):
    if (m==1 or m==2) :
        y=y-1
    else :
        y=y
    y= str(y)
    p= int(y[-2]+y[-1])
    q= int(y[0]+y[1])
    r=((m+9) % 12) +1
    s=((13*r)-1)//5
    t=p//4
    u=q//4
    v=d+p+s+t+u+(5*q)
    w= v % 7
    if w==0 :
        w= "Sunday"
    elif w==1 :
        w= "Monday"
    elif w==2 :
        w= "Tuesday"
    elif w==3 :
        w= "Wednesday"
    elif w==4 :
        w= "Thursday"
    elif w==5 :
        w= "Friday"
    elif w==6 :
        w= "Saturday"

    return w

def main():
    getDayName(d)
    getMonthName(m)
    getDayNum(y,m,d)
    print(getMonthName(m),getDayName(d),",",y,"is a ", getDayNum(y,m,d))

main()
    
    
    
    

