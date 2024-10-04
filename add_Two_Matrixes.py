mat_1 = []
mat_2 = []
res_mat = []

print("Input the size of the square matrix (less than 5): ")
size = int(input())

print("Input elements in the first matrix: ")
for i in range(size):
    a = []
    for j in range(size):
        inp = int(input("Element - " + str([i]) + "," + str([j]) + " : "))
        a.append(inp) 
    mat_1.append(a) 
print("---------------------------------------")

print("Input elements in the second matrix: ")
for i in range(size):
    b = []
    for j in range(size):
        inp = int(input("Elements - " + str([i]) + "," + str([j]) + " : ")) 
        b.append(inp) 
    mat_2.append(b)   
print("---------------------------------------")    

print("Matrix 1: ", mat_1)
print("Matrix 2: ", mat_2) 

for i in range(0,size):
    c = []
    for j in range(0,size):
       cal  = mat_1[i][j] + mat_2[i][j]
       c.append(cal) 
    res_mat.append(c)   

print("---------------------------------------")
print("The Addition of two matrices is: \n", res_mat)
print("The result is in the row-wise manner !")