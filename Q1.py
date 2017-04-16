num1=int(input("Digite um numero: \n"))
num2=int(input("Digite outro: \n"))

if num1>num2:
    print("%d e maior" %num1)
else:
    if num1==num2:
        print("Os numeros sao iguais")
    else:
        if num2>num1:
            print("%d e maior" %num2)
