from Query import Database, Query1, Query2
from Teacher_Crud import TeacherCRUD

db = Database("neo4j+s://da93d59a.databases.neo4j.io", "neo4j", "gKikx_RRR--0dyDWRcYrFhAXdBaeq7RxH0vfNZesF5c")
db.drop_all()

q1_db = Query1(db)
q2_db = Query2(db)
teacher_Crud = TeacherCRUD(db)

#Questão 1
#Buscando pelo professor que o nome seja “Renzo” e retornando o ano de nascimento e o CPF.
print(q1_db.Renzo())

#Buscando pelos professores que o nome comece com a letra “M” e retornando o nome e o CPF.
print(q1_db.initialM())

#Buscando pelos nomes de todas as cidades e as retornando.
print(q1_db.cities())

#Buscando pelas escolas onde o numero seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.
print(q1_db.school())


#Questão 2
#Encontrando o ano de nascimento do professor mais jovem e do professor mais velho.
print(q2_db.profJovemeVelho())

#Encontrando a média aritmética para os habitantes de todas as cidades.
print(q2_db.media())

#Encontrando a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A” .
print(q2_db.CEP())

#Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.
print(q2_db.caracteres())


#Questão 3
#Criando um Professor
teacher_Crud.create("Chris Lima", 1956, "189.052.396-66")

#Pesquisando o professor
result = teacher_Crud.read("Chris Lima")
print("Professor encontrado:")
print(result)

#Alterando o CPF do professor
teacher_Crud.update("Chris Lima", "162.052.777-77")

db.close()