doors = [False] * 100
for i in range(100):
    for j in range(i, 100, i+1):
        doors[j] = not doors[j]

print("The following doors are open: ", end="")
for index, value in enumerate(doors):
    if value == True:
        if index == len(doors) - 1:
            print (index + 1)
        else:
            print (index + 1 , end=", ")
