journey = input()

itemstack = []

index = 0

def add(item):
    itemstack.append(item)

def solution():
    for i in journey:
        if i == "p":
            add(i)
        elif i == "g":
            add(i)
        elif i == "o":
            add(i)
        elif i == "P":
            while len(itemstack) != 0 and itemstack[-1] != "p":
                itemstack.pop() #Remove all other items
            if len(itemstack) == 0:
                return ["Neibb"]
            itemstack.pop() #Give item
        elif i == "G":
            while len(itemstack) != 0 and itemstack[-1] != "g":
                itemstack.pop() #Remove all other items
            if len(itemstack) == 0:
                return ["Neibb"]
            itemstack.pop() #Give item
        elif i == "O":
            while len(itemstack) != 0 and itemstack[-1] != "o":
                itemstack.pop() #Remove all other items
            if len(itemstack) == 0:
                return ["Neibb"]
            itemstack.pop() #Give item
    result = [0,0,0]
    for item in itemstack:
        if item == "p":
            result[0] += 1
        if item == "g":
            result[1] += 1
        if item == "o":
            result[2] += 1
    return result

answer = solution()

for line in answer:
    print(line)