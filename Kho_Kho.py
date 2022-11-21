#A game of Kho Kho is played with N number of players. The first player is given a random number and the objective of the game is to pass this number to the next player # without saying the digit out loud. If the last player in the player group successfully gets the same number as the first player had recieved, the game is won and all #players gets a T-shirt. If that is not the case. Then each player is asked what number they guessed from the last player. Tshirts are  gifted to players guessed the #same number that the first player got. 

# Objective of this code is to find how many players DID NOT get the Tshirt. (TIP: If game is won. All players gets a T-Shirt, and output would be '0')
f=[]
n = int(input("How many friends are playing"))
for i in range(n):
    f.append(int(input("Enter the digit player understood")))
if(f[0]==f[n-1]):
    print(0)
else:
    count = f.count(f[0])
    print(n-count)



