L1 = float(input("Lado 1: "))
L2 = float(input("Lado 2: "))
L3 = float(input("Lado 3: "))

modL2L3 = abs(L2-L3)
modL1L3 = abs(L1-L3)
modL1L2 = abs(L1-L2)

sumL2L3 = L2+L3
sumL1L3 = L1+L3
sumL1L2 = L1+L2

if modL2L3<L1 and L1<sumL2L3 and modL1L3<L2 and L2<sumL1L3 and modL1L2<L3 and L3<sumL1L2:
    if L1 == L2 and L2==L3:
        print("Triangulo equilatero")
    else:
        if L1 == L2 or L2 == L3 or L1==L3:
            print("Triangulo isoceles")
    if L1!=L2 and L2!=L3 and L1!=L3:
            print("Triangulo escaleno")
else:
    print("Não é triângulo")