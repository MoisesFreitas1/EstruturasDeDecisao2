nome=input("Nome: ")
disciplina = input("Disciplina: ")
nota = [None]*4
nota[0] = float(input("1a Nota: "))
nota[1] = float(input("2a Nota: "))
nota[2] = float(input("3a Nota: "))
nota[3] = float(input("4a Nota: "))
somaNota = 0.0
for i in range(0,4):
    somaNota = nota[i]+somaNota
Media = somaNota/4
if Media < 5:
    situacao = "Reprovado"
if Media < 7 and Media >= 5:
    situacao = "Exame Final"
if Media >= 7:
    situacao = "Aprovado"
print("\nNome: ",nome)
print("Disciplina: ",disciplina)
print("Media: ",Media)
print("",situacao)
                
