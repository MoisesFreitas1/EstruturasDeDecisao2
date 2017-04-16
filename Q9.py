num1 = [0,0]
num1[0] = float(input("1o. número: "))
num1[1] = float(input("2o. número: "))
aux = 0
for i in range(0,2):
    for j in range(0,2):
        if num1[i]<num1[j]:
            aux = num1[i]
            num1[i] = num1[j]
            num1[j] = aux
sub = num1[1] - num1[0]
print("Subtracao: ",sub)
