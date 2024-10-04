#To determine the given matrix is sparse matrix or not !
mat = []
print("Input the number of rows in the matrix: ")
rows = int(input())
print("Input the number of columns in the matrix: ")
cols = int(input()) 

print("--------------------------------------------")
print("Input the elements in the matrix: ")
size = rows * cols
for x in range(0,rows):
    a = []
    for y in range(0,cols):
        inp = int(input("Elements- " + str([x]) + "," + str([y]) + ": ")) 
        a.append(inp) 
    mat.append(a)  
print("--------------------------------------------")
print("The matrix is: ", mat)      

cnt = 0
for i in range(0,rows):
    for j in range(0,cols):
        if mat[i][j] == 0:
            cnt += 1

print("--------------------------------------------")
if cnt > (0.66)*size: #Algorithm according to IIT-G lecture
    print("The given matrix is sparse matrix.")
else:
    print("The given matrix is not a sparse matrix.")   

print("--------------------------------------------")
print("There are " + str(cnt) + " number of zeroes in the matrix.")    