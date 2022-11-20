num = int(input("Enter value of n"))
a=1
r1=2
r2=3

if(num%2!=0):
    num = (num+1)//2
    print(a*(r1**(num-1)))
else:
    num=num//2
    print(a * r2 ** (num - 1))
