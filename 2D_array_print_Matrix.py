arr = []
print("Input elements in the 3 x 3 matrix: ")
i = 0
j = 0
for i in range(0,3):
    a = []
    for j in range(0,3):
        inp = int(input("Element - "+ str([i]) +" , " + str([j]) + ": " ))
        a.append(inp) 
    arr.append(a)

print("--------------------------------")
print("The 3 x 3 matrix is: ", arr)
