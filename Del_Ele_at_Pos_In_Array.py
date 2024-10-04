arr = []
print("Input the size of the array: ")
size = int(input())
print("Input " + str(size) + " elements in the array: ")
i = 0
while i < size:
    inp = int(input("Elements " + str(i) + " : "))
    i += 1
    arr.append(inp) 

print("The elements in the array are: ", arr)

print("Input the position where to delete: ")
inp2 = int(input())
for i in range(0,len(arr)):
    if i == inp2:
        arr.pop(i)  

print("The new array is: ", arr)