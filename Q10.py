indice = float(input("Indice de Poluicao (mg/m3): "))
if indice<0.3:
    print("Indice de poluicao aceitavel")
if indice >= 0.3 and indice<0.4:
    print("O grupo 1 deve parar")
if indice >=0.4 and indice<0.5:
    print("Os grupos 1 e 2 devem parar")
if indice>0.5:
    print("Os tres grupos devem parar")