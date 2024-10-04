arr1 = []
arr2 = []
print("Input the number of elements to be stored in the array: ")
num = int(input())
print("Input " + str(num) + " number in the array: ")
i = 0
while i < num:
    inp = int(input("Element " + str(i) + ": "))
    i += 1
    arr1.append(inp) 
print("The elements stored in the first array is: ", arr1)

for i in arr1:
    arr2 = arr1
print("The elements stored in the second array is: ", arr2)    