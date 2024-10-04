mat = []
print("NOTE: This program is only applicale to calculate the determinant of 3 x 3 matrix !")
print("Input the elements of 3 x 3 the matrix: ")
size = 3
for i in range(0,size):
    a = []
    for j in range(0,size):
        inp = int(input("Elements- " + str([i]) + "," +str([j]) + " : "))
        a.append(inp) 
    mat.append(a)  

print("The matrix is: \n", mat) 

det = 0
det = ((mat[0][0]) * ((mat[1][1] * mat[2][2]) - (mat[2][1] * mat[1][2]))) - ((mat[0][1]) * ((mat[1][0] * mat[2][2]) - (mat[2][0] * mat[1][2]))) + ((mat[0][2]) * ((mat[1][0] * mat[2][1]) - (mat[2][0] * mat[1][1])))

print("The determinant of the matrix is:", det)
