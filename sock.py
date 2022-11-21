#A person has N number of socks in his collection of different sizes. Eg[If the person has 10 socks. 1 could be of size "1" and other could be of different sizes as well].
#Objective of this code is to find how many pairs can this person successfully sell given he has N number of socks of X sizes.
#Example : He has 9 socks in his collection [10,20,20,10,10,30,50,10,20] from this he can take 2 pair of size "10" socks since he has total 4 of size "10" socks.

def pairs(sizeList):
    pairCount = 0
    for key in set(sizeList):
        count = sizeList.count(key)
        pairCount +=count//2;
    return pairCount
sockList = [10,20,20,10,10,30,50,10,20]
print(set(sockList))
print(pairs(sockList))
