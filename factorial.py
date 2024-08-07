def factorial(num):
    j=1
    for i in range (1,num+1):
        j=j*i
    return j
a=int(input("enter the number"))
print("factorial of ",a ,"is " ,factorial(a))