"""Exibe relatório de crianças por atividade. 

imprimir a lista de crianças agrupadas por sala que frequentas cada uma das atividades.
"""

__Version__ = "0.1.0"


print("-" * 50)


print("Lista escolar")
print("")

sala1 = ["Dudu","Heitor","Rodrigo","Joaquim","Lizis","Melissa"]
sala2 = ["Miguel", "Victor","Saulo","Pietra","Yasmin","João"]


aula_ingles=["Dudu","Heitor","Miguel","Victor"]

aula_jiujitsu={"Rodrigo0", "Joaquim","Lizis","Melissa","Miguel", "Saulo","Pietra","João","Yasmin"}


aula_de_ingles1= []
aula_de_ingles2= []


aula_jiujitsu1=[]
aula_jiujitsu2=[]

for aluno in aula_ingles:
  if aluno in sala1:
    aula_de_ingles1.append(aluno)
  elif aluno in sala2:
    aula_de_ingles2.append(aluno)
    
    for aluno in aula_jiujitsu:
      if aluno in sala1:
        aula_jiujitsu1.append(aluno)
      elif aluno in sala2:
        aula_jiujitsu2.append(aluno)  


print("Ingles sala1", aula_de_ingles1)
print("Ingles sala2", aula_de_ingles2)

print("")

print("Jiu-jitsu sala 1", aula_jiujitsu1)
print("Jiu-jitsu sala 2 ", aula_jiujitsu2)

print("")
print("#" * 180)