def fibonacci(num):
    t1=0
    t2=1
    print(t1,"\n",t2)
    for i in range(3,num+1):
        next=t1+t2
        print(next)
        t1=t2
        t2=next
a=int(input("enter the number"))
fibonacci(a)