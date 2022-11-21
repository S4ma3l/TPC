#Program to find the nth prime number


def primeOrNot(num):

    for i in range(2,num):
        if num%i==0:
            return False
    return True

def returnnthPrime(nthNumber):
    count = 0
    numToCheck =1
    while (count!=nthNumber):
        numToCheck += 1
        if primeOrNot(numToCheck):
            count +=1
    return numToCheck


print("Nth prime number is: ", returnnthPrime(int(input("Enter a number"))))
