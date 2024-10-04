arr = []
print("Input the number of elements to be stored in the array: ")
num = int(input())
print("Input " + str(num) + " number of elements in the array: ")
i = 0
while i < num:
    inp = int(input("Elements " + str(i) + " : "))
    i += 1
    arr.append(inp) 
print("The elements in the array are: ", arr)

arr.sort()
min = float(99999999)        #The algorithm for this code
max = float(-99999999)
for i in range(0,len(arr)):
    if arr[i] < min:
        min = arr[i]
         
    if arr[i] > max:
        max = arr[i]
         
print("The minimum number in the array is: ", min)
print("The maximum number in the array is: ", max)
