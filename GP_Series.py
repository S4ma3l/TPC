#Question - In a series of numbers all odd numbers are replaced by numbers in a series of Geometric progression with formula (a*(r**(n-1))) here a = 1, and r=2 for #first series. All even positions are replaced by another geometric progression series of the formula (a*(r**(n-1))) here a =1 and r=3
#Find the nth term in the series?

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
