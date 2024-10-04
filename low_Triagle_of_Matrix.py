mat = []

print("Input the size of the matrix: ")
size = int(input())

print("Input elements in the matrix: ")
for i in range(0,size):
    a = []
    for j in range(0,size):
        inp = int(input("Elements- " + str([i]) + " , " + str([j]) + " : "))
        a.append(inp) 
    mat.append(a)   

print("The matrix is: \n", mat) 
print("------------------------------------------")

print("Setting zero in lower triangular matrix: ")
for i in range(0,size):
    for j in range(0,size):
        if i > j:
            mat[i][j] = 0
            
print(mat)
