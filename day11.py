############################## TESTOVACI ##############################

monkey0 = [79, 98]
items0 = 0
monkey1 = [54, 65, 75, 74]
items1 = 0
monkey2 = [79, 60, 97]
items2 = 0
monkey3 = [74]
items3 = 0

round = 0

while round < 20:
    items0 += len(monkey0)
    while monkey0:
        thing = monkey0.pop(0)
        worry0 = thing * 19
        worry0 = int(worry0/3)
        if worry0 % 23 == 0:
            monkey2.append(worry0)
        else:
            monkey3.append(worry0)

    items1 += len(monkey1)
    while monkey1:
        thing = monkey1.pop(0)
        worry0 = thing + 6
        worry0 = int(worry0/3)
        if worry0 % 19 == 0:
            monkey2.append(worry0)
        else:
            monkey0.append(worry0)

    items2 += len(monkey2)
    while monkey2:
        thing = monkey2.pop(0)
        worry0 = thing * thing
        worry0 = int(worry0/3)
        if worry0 % 13 == 0:
            monkey1.append(worry0)
        else:
            monkey3.append(worry0)

    items3 += len(monkey3)
    while monkey3:
        thing = monkey3.pop(0)
        worry0 = thing + 3
        worry0 = int(worry0/3)
        if worry0 % 17 == 0:
            monkey0.append(worry0)
        else:
            monkey1.append(worry0)

    round += 1


print(items0)
print(items1)
print(items2)
print(items3)
print('#######')

############################## PART 1 ##############################

monkey0 = [83, 88, 96, 79, 86, 88, 70]
items0 = 0
monkey1 = [59, 63, 98, 85, 68, 72]
items1 = 0
monkey2 = [90, 79, 97, 52, 90, 94, 71, 70]
items2 = 0
monkey3 = [97, 55, 62]
items3 = 0
monkey4 = [74, 54, 94, 76]
items4 = 0
monkey5 = [58]
items5 = 0
monkey6 = [66, 63]
items6 = 0
monkey7 = [56, 56, 90, 96, 68]
items7 = 0


round = 0

while round < 20:
    items0 += len(monkey0)
    while monkey0:
        thing = monkey0.pop(0)
        worry0 = thing * 5
        worry0 = int(worry0/3)
        if worry0 % 11 == 0:
            monkey2.append(worry0)
        else:
            monkey3.append(worry0)

    items1 += len(monkey1)
    while monkey1:
        thing = monkey1.pop(0)
        worry0 = thing * 11
        worry0 = int(worry0/3)
        if worry0 % 5 == 0:
            monkey4.append(worry0)
        else:
            monkey0.append(worry0)

    items2 += len(monkey2)
    while monkey2:
        thing = monkey2.pop(0)
        worry0 = thing + 2
        worry0 = int(worry0/3)
        if worry0 % 19 == 0:
            monkey5.append(worry0)
        else:
            monkey6.append(worry0)

    items3 += len(monkey3)
    while monkey3:
        thing = monkey3.pop(0)
        worry0 = thing + 5
        worry0 = int(worry0 / 3)
        if worry0 % 13 == 0:
            monkey2.append(worry0)
        else:
            monkey6.append(worry0)

    items4 += len(monkey4)
    while monkey4:
        thing = monkey4.pop(0)
        worry0 = thing * thing
        worry0 = int(worry0/3)
        if worry0 % 7 == 0:
            monkey0.append(worry0)
        else:
            monkey3.append(worry0)

    items5 += len(monkey5)
    while monkey5:
        thing = monkey5.pop(0)
        worry0 = thing + 4
        worry0 = int(worry0 / 3)
        if worry0 % 17 == 0:
            monkey7.append(worry0)
        else:
            monkey1.append(worry0)

    items6 += len(monkey6)
    while monkey6:
        thing = monkey6.pop(0)
        worry0 = thing + 6
        worry0 = int(worry0 / 3)
        if worry0 % 2 == 0:
            monkey7.append(worry0)
        else:
            monkey5.append(worry0)

    items7 += len(monkey7)
    while monkey7:
        thing = monkey7.pop(0)
        worry0 = thing + 7
        worry0 = int(worry0 / 3)
        if worry0 % 3 == 0:
            monkey4.append(worry0)
        else:
            monkey1.append(worry0)

    round += 1


print(items0)
print(items1)
print(items2)
print(items3)
print(items4)
print(items5)
print(items6)
print(items7)






