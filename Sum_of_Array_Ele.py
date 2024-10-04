arr = []
print("Input the number of elements to be stored in the array: ")
num = int(input())
print("Input " + str(num) + " number of elements in array: ")
i = 0
while i < num:
    inp = int(input("Element " + str(i) + " :" ))
    i += 1
    arr.append(inp)  
print("The elements in the array are: ", arr)
print(arr)

sum = 0
for i in arr:
    sum += i
print("The sum of the array is: ", sum)
