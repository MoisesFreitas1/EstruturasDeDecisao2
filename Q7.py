num1 = [0,0,0]
num1[0] = float(input("1o. número: "))
num1[1] = float(input("2o. número: "))
num1[2] = float(input("3o. número: "))
aux = 0
for i in range(0,3):
    for j in range(0,3):
        if num1[i]<num1[j]:
            aux = num1[i]
            num1[i] = num1[j]
            num1[j] = aux
print(num1[0]," ",num1[1]," ",num1[2])

