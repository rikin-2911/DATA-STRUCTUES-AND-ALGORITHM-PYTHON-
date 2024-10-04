arr = []
print("Input the number of elements to be stored in the array: ")
num = int(input())
print("Input " + str(num) + " number in the array: ")
i = 0
while i < num:
    inp = int(input("Element " + str(i) + ": "))
    i += 1
    arr.append(inp) 

print("The numbers in the array are: ", arr)
print("The frequency of all elements in the array is: ")
arr.sort()
frq = 0
for i in range(1,len(arr)):
    if arr[i] == arr[i - 1]:
        frq += 2
        print(str(arr[i]) + " occurs " + str(frq)+ " times")
    else:
        frq = 1
        print(str(arr[i]) + " occurs " + str(frq)+ " times")

#code is in construction stage !!