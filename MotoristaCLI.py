from MotoristaDAO import MotoristaDAO


class MotoristaCLI:
    def __init__(self, dao: MotoristaDAO):
        self.dao = dao

    def menu(self):
        print("1. Create Motorista")
        print("2. Read Motorista")
        print("3. Update Motorista")
        print("4. Delete Motorista")
        print("0. Exit")

    def create_motorista(self):
        # Lógica para criar um novo motorista
        pass

    def read_motorista(self):
        # Lógica para ler os detalhes de um motorista
        pass

    def update_motorista(self):
        # Lógica para atualizar os detalhes de um motorista
        pass

    def delete_motorista(self):
        # Lógica para deletar um motorista
        pass

    def run(self):
        # Lógica para executar o programa
        pass
