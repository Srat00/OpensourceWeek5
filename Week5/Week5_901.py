import random

def getNumber():
    return random.randint(1, 46)

lottery = []
num = 0

print("L O T T E R Y !")

while True:
    num = getNumber()
    
    if lottery.count(num) == 0:
        lottery.append(num)
        
    if len(lottery) >= 6:
        break
    
print("Lottery Number >> ", end="")
    
lottery.sort()
    
for i in range(0, 6):
    print("%d " % lottery[i] , end=" ")