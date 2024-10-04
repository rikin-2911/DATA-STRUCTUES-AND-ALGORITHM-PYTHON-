arr1 = []

print("Input the number of elements to be stored in the array: ")
num = int(input())
print("Input " + str(num) + " elements in the array: ")
i = 0
while i < num:
    inp = int(input("Element " + str(i) + ": "))
    i += 1
    arr1.append(inp)

print("All elements in the array are: ", arr1)
arr1.sort()
print("All unique elements in the array are: ")
for i in range(1, len(arr1)):
    d = 0
    for j in range(0, i):
        if arr1[i] == arr1[j]:
            d = 1
            break
    if d == 0:
        print(arr1[i])   

# code is not properly completed!!            