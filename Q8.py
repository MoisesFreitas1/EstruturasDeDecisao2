print("ax2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = (b*b) - (4*a*c)
if delta >= 0:
    x1 = ((-1)*b + delta**(1/2))/(2*a)
    x2 = ((-1)*b - delta**(1/2))/(2*a)
    print("Raizes\nx1 = ",x1,"\nx2 = ",x2)
else:
    print("A equacao nao possui raizes reais!")
