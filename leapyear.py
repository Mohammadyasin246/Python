def leap(x):
    if ((x%4==0 or x%400==0)and(x%100!=0)):
        return " leap year"
    else:
        return "not leap year"
a=int(input("enter the year"))
print(leap(a))