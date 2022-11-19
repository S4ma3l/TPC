def pairs(sizeList):
    pairCount = 0
    for key in set(sizeList):
        count = sizeList.count(key)
        pairCount +=count//2;
    return pairCount
sockList = [10,20,20,10,10,30,50,10,20]
print(set(sockList))
print(pairs(sockList))