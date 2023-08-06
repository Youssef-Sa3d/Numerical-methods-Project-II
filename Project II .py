

print("-------------------------------------------------------------- \n")
inter = float(input("interpolate = "))
deg = int(input("Degree = "))
print("--------------------------------------------------------------")

x = []
fx = []
arr = [x , fx]


for i in range(deg + 1):
    x.append(float(input("x = ")))
    fx.append(float(input("f(x) = ")))

for i in range(deg):
    arr.append([])




k = 0

for i in range (2 , len(arr)):
    
    if len(arr[i]) == 1 :
        break
    
    for j in range (1 , len(arr[i-1])) :
        arr[i].append( ( arr[i-1][j] - arr[i-1][j-1] ) / ( arr[0][j+k] - arr[0][j-1] ) )
    k = k + 1
    

for i in range (len(arr)):
    print(arr[i])
    

print("-------------------------------------------------------------- \n")


p  = 0
suii = 1
for i in range(deg):
    p = p + ( arr[i+1][0] * suii )
    suii = suii * (inter - arr[0][i])
    
print("P = " , p)




