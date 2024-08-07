def vow(text):
    count=0
    p=0
    j=0
    for i in text:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            count+=1
        elif(i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
            count+=1
        elif(i==" "):
            j+=1
        else:
            p+=1
    print("vowels= ",count)
    print("consonants= ",p) 
    print("spaces= ",j)
a=input("enter the sentence")
print(vow(a))