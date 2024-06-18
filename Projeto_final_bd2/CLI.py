class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class ProdutoCLI(SimpleCLI):
    def __init__(self, produto_model):
        super().__init__()
        self.produto_model = produto_model
        self.add_command("create", self.create_produto)
        self.add_command("read", self.read_produto)
        self.add_command("update", self.update_produto)
        self.add_command("delete", self.delete_produto)

    def create_produto(self):
        nome = input("Enter the product name: ")
        descricao = input("Enter the product description: ")
        preco = float(input("Enter the product price: "))
        estoque = int(input("Enter the product stock: "))
        self.produto_model.create_produto(nome, descricao, preco, estoque)

    def read_produto(self):
        id = input("Enter the product id: ")
        produto = self.produto_model.read_produto_by_id(id)
        if produto:
            print(f"Name: {produto['nome']}")
            print(f"Description: {produto['descricao']}")
            print(f"Price: {produto['preco']}")
            print(f"Stock: {produto['estoque']}")

    def update_produto(self):
        id = input("Enter the product id: ")
        nome = input("Enter the new product name: ")
        descricao = input("Enter the new product description: ")
        preco = float(input("Enter the new product price: "))
        estoque = int(input("Enter the new product stock: "))
        self.produto_model.update_produto(id, nome, descricao, preco, estoque)

    def delete_produto(self):
        id = input("Enter the product id: ")
        self.produto_model.delete_produto(id)

    def run(self):
        print("Welcome to the product CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()


class PedidoCLI(SimpleCLI):
    def __init__(self, pedido_model):
        super().__init__()
        self.pedido_model = pedido_model
        self.add_command("create", self.create_pedido)
        self.add_command("read", self.read_pedido)
        self.add_command("update", self.update_pedido)
        self.add_command("delete", self.delete_pedido)

    def create_pedido(self):
        cliente_id = int(input("Enter the client id: "))
        data_compra = input("Enter the purchase date: ")
        produtos = []
        while True:
            descricao = input("Enter the product description: ")
            quantidade = int(input("Enter the product quantity: "))
            preco = float(input("Enter the product price: "))
            produtos.append({"descricao": descricao, "quantidade": quantidade, "preco": preco})
            more = input("Add another product? (y/n): ")
            if more.lower() != 'y':
                break
        self.pedido_model.create_pedido(cliente_id, data_compra, produtos)

    def read_pedido(self):
        id = input("Enter the order id: ")
        pedido = self.pedido_model.read_pedido_by_id(id)
        if pedido:
            print(f"Client ID: {pedido['cliente_id']}")
            print(f"Purchase Date: {pedido['data_compra']}")
            for produto in pedido['produtos']:
                print(
                    f"  Product: {produto['descricao']}, Quantity: {produto['quantidade']}, Price: {produto['preco']}")

    def update_pedido(self):
        id = input("Enter the order id: ")
        cliente_id = int(input("Enter the new client id: "))
        data_compra = input("Enter the new purchase date: ")
        produtos = []
        while True:
            descricao = input("Enter the new product description: ")
            quantidade = int(input("Enter the new product quantity: "))
            preco = float(input("Enter the new product price: "))
            produtos.append({"descricao": descricao, "quantidade": quantidade, "preco": preco})
            more = input("Add another product? (y/n): ")
            if more.lower() != 'y':
                break
        self.pedido_model.update_pedido(id, cliente_id, data_compra, produtos)

    def delete_pedido(self):
        id = input("Enter the order id: ")
        self.pedido_model.delete_pedido(id)

    def run(self):
        print("Welcome to the order CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
