arr = []
print("Input the number of elements to be stored in the array: ")
num = int(input())
print("Input " + str(num) + " elements in the array: ")
i = 0
while i < num:
    inp = int(input("Element " + str(i) + ": "))
    i += 1
    arr.append(inp) 

arr.sort()
frq = 0
for j in range(1,len(arr)):
    if arr[j] == arr[j - 1]:
        frq += 1
print("Total number of duplicate elements found is: ", frq)        