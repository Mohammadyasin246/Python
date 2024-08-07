def ranger(x,y):
    for i in range(x,y+1):
        if i>1:
            for k in range(2,i):
                if i%k==0:
                    break
            else:
                print(i)
num1=int(input("enter the starting number"))
num2=int(input("enter the ending number"))
print(ranger(num1,num2))