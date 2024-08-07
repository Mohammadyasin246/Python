def tech(num):
    s=len(num)
    copy=str(num)
    copy=int(copy)
    num=int(num)
    sum=0
    sq=1
    if s%2==0:
        while num>0:
            digit=num%100
            sum+=digit
            num//=100
        sq=sum**2
        if copy==sq:
            return "tech number"
        else:
            return "not tech number"
    else:
        return "plaese enter the even digit number"
a=input("enter the number")
print(tech(a))