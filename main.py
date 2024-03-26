from database import Database
from livro_model import LivroModel


def main():

    # Conectando ao banco de dados MongoDB
    db = Database(database='exRelatorio_5', collection='livros')
    livro_model = LivroModel(database=db)

    while True:
        print("\n===== MENU =====")
        print("1. Criar livro")
        print("2. Ler livro por ID")
        print("3. Atualizar livro")
        print("4. Deletar livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano de publicação do livro: "))
            preco = float(input("Digite o valor do livro: "))
            livro_model.create_livro(titulo, autor, ano, preco)
        elif escolha == "2":
            id_livro = input("Digite o ID do livro: ")
            livro_model.read_livro(id_livro)
        elif escolha == "3":
            id_livro = input("Digite o ID do livro que deseja atualizar: ")
            titulo = input("Digite o novo título do livro: ")
            autor = input("Digite o novo autor do livro: ")
            ano = int(input("Digite o novo ano de publicação do livro: "))
            preco = float(input("Digite o novo ano de publicação do livro: "))
            livro_model.update_livro(id_livro, titulo, autor, ano, preco)
        elif escolha == "4":
            id_livro = input("Digite o ID do livro que deseja deletar: ")
            livro_model.delete_livro(id_livro)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()