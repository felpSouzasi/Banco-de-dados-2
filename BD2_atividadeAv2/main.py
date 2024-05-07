#CRIANDO OS NÓS

#CREATE(:Pessoa:Engenheiro{nome:"Felipe", idade:"20", sexo:"masculino"})
#CREATE(:Pessoa:Nutricionista{nome:"Livia", idade:"17", sexo:"feminino"})
#CREATE(:Pessoa:DoLar{nome:"Luzia", idade:"70", sexo:"feminino"})
#CREATE(:Pessoa:Professora{nome:"Célia Maura", idade:"50", sexo:"feminino"})
#CREATE(:Pessoa:Contadora{nome:"Suellen", idade:"40", sexo:"feminino"})
#CREATE(:Pessoa:Contadora{nome:"Tamiris", idade:"30", sexo:"feminino"})
#CREATE(:Pessoa:Professora{nome:"Tallyne", idade:"27", sexo:"feminino"})
#CREATE(:Pessoa:Vendendor{nome:"Thiago", idade:"30", sexo:"masculino"})
#CREATE(:Pessoa:Estudante{nome:"Arthur", idade:"2", sexo:"masculino"})
#CREATE(:Pessoa:Engenheiro{nome:"Arlindo", idade:"75", sexo:"masculino"})
#CREATE(:Pessoa:estudante{nome:"Lais", idade:"12", sexo:"feminino"})


#CRIANDO OS RELACIONAMENTOS

#MATCH (c:Pessoa{nome:"Célia Maura"}), (l:Pessoa{nome:"Luzia"})
#CREATE (c)-[:FILHO_DE]->(l)

#MATCH (c:Pessoa{nome:"Célia Maura"}), (a:Pessoa{nome:"Arlindo"})
#CREATE (c)-[:FILHO_DE]->(a)

#MATCH (s:Pessoa{nome:"Suellen"}), (l:Pessoa{nome:"Luzia"})
#CREATE (s)-[:FILHO_DE]->(l)

#MATCH (s:Pessoa{nome:"Suellen"}), (a:Pessoa{nome:"Arlindo"})
#CREATE (s)-[:FILHO_DE]->(a)

#MATCH (t:Pessoa{nome:"Tamiris"}), (c:Pessoa{nome:"Célia Maura"})
#CREATE (t)-[:FILHO_DE]->(c)

#MATCH (t2:Pessoa{nome:"Tallyne"}), (c:Pessoa{nome:"Célia Maura"})
#CREATE (t2)-[:FILHO_DE]->(c)

#MATCH (f:Pessoa{nome:"Felipe"}), (c:Pessoa{nome:"Célia Maura"})
#CREATE (f)-[:FILHO_DE]->(c)

#MATCH (l1:Pessoa{nome:"Lais"}), (s:Pessoa{nome:"Suellen"})
#CREATE (l1)-[:FILHO_DE]->(s)

#MATCH (art:Pessoa{nome:"Arthur"}), (t2:Pessoa{nome:"Tallyne"})
#CREATE (art)-[:FILHO_DE]->(t2)

#MATCH (art:Pessoa{nome:"Arthur"}), (t3:Pessoa{nome:"Thiago"})
#CREATE (art)-[:FILHO_DE]->(t3)

#MATCH (t2:Pessoa{nome:"Tallyne"}), (t3:Pessoa{nome:"Thiago"})
#CREATE (t2)-[:CASADO_COM]->(t3)

#MATCH (f:Pessoa{nome:"Felipe"}), (l1:Pessoa{nome:"Lais"})
#CREATE (f)-[:PRIMO_DE]->(l1)

#MATCH (t:Pessoa{nome:"Tamiris"}), (l1:Pessoa{nome:"Lais"})
#CREATE (t)-[:PRIMO_DE]->(l1)

#MATCH (t:Pessoa{nome:"Tallyne"}), (l1:Pessoa{nome:"Lais"})
#CREATE (t)-[:PRIMO_DE]->(l1)

#MATCH (l:Pessoa{nome:"Lais"}), (f:Pessoa{nome:"Felipe"})
#CREATE (l)-[:PRIMO_DE]->(f)

#MATCH (l:Pessoa{nome:"Lais"}), (t:Pessoa{nome:"Tamiris"})
#CREATE (l)-[:PRIMO_DE]->(t)

#MATCH (l:Pessoa{nome:"Lais"}), (t:Pessoa{nome:"Tallyne"})
#CREATE (l)-[:PRIMO_DE]->(t)

#MATCH (a:Pessoa {nome: "Felipe"}), (b:Pessoa {nome: "Livia"})
#CREATE (a)-[r:NAMORA_COM {desde: 2023}]->(b)}]->(b)

#CÓDIGO PARA AS QUERIES
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

#Fulano de tal é filho de quem?
def filho_de_quem(tx, nomeFilho):
    query = """
    MATCH (p1:Pessoa {nome: $nomeFilho}) -[:FILHO_DE]-> (p2:Pessoa)
    RETURN p1.nome
    """
    result = tx.run(
        query,
        nomeFilho = nomeFilho
    )
    try:
        return [(record["p.nome"]) for record in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

#beltrano de tal namora com quem desde quando?
def namora_com_quem_desde_quando(tx, nomeP, code, test_data):
    query = """
        MATCH (p1:Pessoa {nome: $nomeP}) -[r:NAMORADO_DE]-> (p2:Pessoa)
        RETURN p2.nome, r.desde
    """
    result = tx.run(
        query,
        test_data = test_data,
        code = code
    )
    try:
        return [(record["p2.nome"], record["r.desde"]) for record in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise

    #Quem da família é Engenheiro?
def quem_eh_engenheiro(tx, code, test_data):
    query = """
    MATCH (p:Pessoa:Engenheiro)
    RETURN p.nome
    """
    result = tx.run(
    query,
        test_data = test_data,
        code = code
    )
    try:
        return [(record["p.nome"]) for record in result]

    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
        raise


uri = "neo4j+s://fcc401c3.databases.neo4j.io"
user = "neo4j"
password = "xTPw5uAhCIv2O7sDhx-dJ2Gk1lWpk44YKkYksl01t7I"

driver = GraphDatabase.driver(uri, auth=(user, password))

code = 2
teste_data = "Createing a new node..."

with driver.session() as session:
    print("Beltrano de tal é filho de quem?")
    print(filho_de_quem(session, "Felipe"))

    print("Sicrana de tal namora com quem desde quando?")
    print(namora_com_quem_desde_quando(session, "Livia"))

    print("Quem da família é Engenheiro?")
    print(quem_e_engenheiro(session))

driver.close()