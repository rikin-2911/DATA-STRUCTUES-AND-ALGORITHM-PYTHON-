arr = []
print("Input the number of elements to store in the array: ")
num = int(input())
print("Input " + str(num) + " number of elements in the array: ")
i = 0
while i < num:
    inp = input("Element: ")
    i += 1
    arr.append(inp)
print("The array is: ")
print(arr)
print("The reversed array is: ")

#For reversing an array used arr[::-1] method
print(arr[::-1])
