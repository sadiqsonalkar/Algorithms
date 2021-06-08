a =[[5, 6],
   [7, 8]]
print("a = ", a)
 
b =[[4, 6],
    [9, 8]]
print("b = ", b)
 
c =[[0, 0],
    [0, 0]]
 
for i in range(len(a)):
    print("i = ", i)
    for j in range(len(b)):
        print("j = ", j)
        for k in range(len(c)):
            print("k = ", k)
            c[i][j] = a[i][k]*b[k][j]+c[i][j]
            
for result in c :
    print(result)
