Nome = input("Nome: ")
SalarioAnual = float(input("Salario Anual: R$"))

if SalarioAnual<=10000:
    print(Nome,"\nSalario Anual: R$",SalarioAnual,"\nIsento de Imposto de Renda")
if SalarioAnual>10000 and SalarioAnual<=15000:
    Desconto = SalarioAnual*0.05
    SalarioLiquido = SalarioAnual - Desconto
    print(Nome,"\nSalario Anual: ",SalarioAnual,"\nDesconto de 5%: R$",Desconto,"\nSalario Liquido: R$",SalarioLiquido)
if SalarioAnual>15000 and SalarioAnual<=20000:
    Desconto = SalarioAnual*0.10
    SalarioLiquido = SalarioAnual - Desconto
    print(Nome,"\nSalario Anual: ",SalarioAnual,"\nDesconto de 10%: R$",Desconto,"\nSalario Liquido: R$",SalarioLiquido)
if SalarioAnual>20000 and SalarioAnual<=25000:
    Desconto = SalarioAnual*0.15
    SalarioLiquido = SalarioAnual - Desconto
    print(Nome,"\nSalario Anual: ",SalarioAnual,"\nDesconto de 15%: R$",Desconto,"\nSalario Liquido: R$",SalarioLiquido)
if SalarioAnual>25000:
    Desconto = SalarioAnual*0.2
    SalarioLiquido = SalarioAnual - Desconto
    print(Nome,"\nSalario Anual: ",SalarioAnual,"\nDesconto de 20%: R$",Desconto,"\nSalario Liquido: R$",SalarioLiquido)