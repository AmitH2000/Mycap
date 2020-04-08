num=int(input("Enter the limit :"))
a,b=0,1
while a<num:
    print(a,end=",")
    a,b=b,a+b
    print()

