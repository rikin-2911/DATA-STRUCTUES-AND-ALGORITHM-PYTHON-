arr = []
odd_arr = []
even_arr = []
print("Input the number of elements to be stored in the array: ")
num = int(input())
print("Input " + str(num) + " elements in the array: ")
i = 0 
while i < num:
    inp = int(input("Elements " + str(i) + " : "))
    i += 1
    arr.append(inp) 

print("The elements in the array are: ", arr)

arr.sort()
for i in range(0, len(arr)):
    if arr[i] % 2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])    

print("The even elements in the array are: ", even_arr)
print("The odd elements in the array are: ", odd_arr)
