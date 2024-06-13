from database import Database
from writeAJson import writeAJson
from produto import ProdutoModel
from pedido import PedidoModel
from CLI import ProdutoCLI, PedidoCLI

db_produto = Database(database="loja_online", collection="produtos")
produtoModel = ProdutoModel(database=db_produto)

db_pedido = Database(database="loja_online", collection="pedidos")
pedidoModel = PedidoModel(database=db_pedido)

produtoCLI = ProdutoCLI(produtoModel)
pedidoCLI = PedidoCLI(pedidoModel)

print("Bem-vindo ao sistema de gerenciamento de loja online!")
while True:
    print("Escolha uma opção: produto, pedido, quit")
    opcao = input("Digite sua opção: ")
    if opcao == "produto":
        produtoCLI.run()
    elif opcao == "pedido":
        pedidoCLI.run()
    elif opcao == "quit":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")