def primeOrNot(num):

    for i in range(2,num):
        if num%i==0:
            return False
    return True
#print(primeOrNot(int(input("Enter a number to check whether it's prime or not"))))
def returnnthPrime(nthNumber):
    count = 0
    numToCheck =1
    while (count!=nthNumber):
        numToCheck += 1
        if primeOrNot(numToCheck):
            count +=1
    return numToCheck


print("Nth: ", returnnthPrime(int(input("Enter a number"))))
