def prime(num):
    count=0
    for i in range (1,num+1):
        if num%i==0:
            count+=1
    if count==2 :
        return "prime"
    else:
        return " composite"
a=int(input("enter the number"))
print(prime(a))