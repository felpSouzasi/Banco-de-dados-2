from game import Game
def create_player(game):
    name = input("Qual é o nome do jogador? ")
    player_id = input("Qual é o ID do jogador? ")
    game.create_player(name, player_id)
    print("Jogador criado com sucesso!")


def update_player(game):
    player_id = input("Qual é o ID do jogador que você quer atualizar? ")
    new_name = input("Qual é o novo nome do jogador? ")
    game.update_player(player_id, new_name)
    print("Jogador atualizado com sucesso!")


def delete_player(game):
    player_id = input("Qual é o ID do jogador que você quer excluir? ")
    game.delete_player(player_id)
    print("Jogador excluído com sucesso!")


def create_match(game):
    match_id = input("Qual é o ID da partida? ")
    players = input("Quais são os IDs dos jogadores participantes? Separe por vírgula: ").split(',')
    result = input("Qual foi o resultado da partida? ")
    game.create_match(match_id, players, result)
    print("Partida criada com sucesso!")


def get_player_matches(game):
    player_id = input("Qual é o ID do jogador? ")
    player_matches = game.get_player_matches(player_id)
    print(f"Histórico de partidas do jogador {player_id}:")
    for match_id, result in player_matches:
        print(f"Partida ID: {match_id}, Resultado: {result}")


def get_match_info(game):
    match_id = input("Qual é o ID da partida? ")
    match_info = game.get_match_info(match_id)
    print("Informações da partida:")
    print("ID da partida:", match_info["match_id"])
    print("Resultado:", match_info["result"])
    print("Jogadores:")
    for player_id, name in match_info["players"]:
        print(f"Jogador ID: {player_id}, Nome: {name}")




def get_all_players(game):
    players = game.get_all_players()
    print("Lista de todos os jogadores:")
    for player_id, name in players:
        print(f"ID do jogador: {player_id}, Nome do jogador: {name}")

    uri = "neo4j+s://978fb6b1.databases.neo4j.io"
    user = "neo4j"
    password = "EjBUDywuCAuJGbWdXoKh_cu0VoLFwXVnahvI_X99WtM"
    game = Game(uri, user, password)

    while True:
        print("\nMenu:")
        print("1. Criar jogador")
        print("2. Atualizar jogador")
        print("3. Excluir jogador")
        print("4. Criar partida")
        print("5. Histórico de partidas de um jogador")
        print("6. Informações sobre uma partida")
        print("7. Listar todos os jogadores")
        print("8. Sair")

        choice = input("Escolha uma opção: ")

        # Menu de opções
        if choice == "1":
            create_player()  # Criar jogador
        elif choice == "2":
            update_player()  # Atualizar jogador
        elif choice == "3":
            delete_player()  # Excluir jogador
        elif choice == "4":
            create_match()  # Criar partida
        elif choice == "5":
            get_player_matches()  # Obter histórico de partidas de um jogador
        elif choice == "6":
            get_match_info()  # Obter informações sobre uma partida específica
        elif choice == "7":
            get_all_players()  # Obter todos os jogadores
        elif choice == "8":
            exit()  # Sair do programa
        else:
            print("Opção inválida. Tente novamente.")

    game.db.close()
