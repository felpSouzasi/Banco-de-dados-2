import redis
from datetime import datetime, timedelta

# Conexão com o Redis
redis_conn = redis.Redis(
    host="redis-17807.c8.us-east-1-2.ec2.redns.redis-cloud.com", port=17807,
    username="default",
    password="Rj0G9Z376Tkqg1PHnltqXFyRk5SowoCS",
    decode_responses=True
)

def questao_1(users):
    for user in users:
        user_key = f"user:{user['id']}"
        redis_conn.hset(user_key, mapping=user)

def consultar_usuarios():
    user_keys = redis_conn.keys("user:*")
    users = []
    for key in user_keys:
        if ":interests" not in key and ":viewed" not in key:
            users.append(redis_conn.hgetall(key))
    return users

def mostrar_usuarios():
    users = consultar_usuarios()
    for user in users:
        print(f"ID: {user['id']}, Nome: {user['nome']}, Email: {user['email']}")

# Teste
def test_questao_1():
    users = [
        {"id":'1', "nome":"Serafim Amarantes", "email":"samarantes@g.com"},
        {"id":'2', "nome":"Tamara Borges", "email":"tam_borges@g.com"},
        {"id":'3', "nome":"Ubiratã Carvalho", "email":"bira@g.com"},
        {"id":'4', "nome":"Valéria Damasco", "email":"valeria_damasco@g.com"}
    ]
    questao_1(users)
    #mostrar_usuarios()

test_questao_1()


#questão 2
def questao_2(interests):
    for interest in interests:
        user_id = interest["usuario"]
        user_key = f"user:{user_id}:interests"
        for item in interest["interesses"]:
            for k, v in item.items():
                redis_conn.zadd(user_key, {k: v})

def consultar_interesses():
    user_keys = redis_conn.keys("user:*:interests")
    interests = {}
    for key in user_keys:
        user_id = key.split(":")[1]
        interests[user_id] = redis_conn.zrange(key, 0, -1, withscores=True)
    return interests

def mostrar_interesses():
    interesses = consultar_interesses()
    for user_id, interests in interesses.items():
        print(f"Usuário ID: {user_id}")
        for interest, score in interests:
            print(f"  Interesse: {interest}, Score: {score}")

# Teste
def test_questao_2():
    interests = [
        {"usuario":1, "interesses": [{"futebol":0.855}, {"pagode":0.765}, {"engraçado":0.732}, {"cerveja":0.622}, {"estética":0.519}]},
        {"usuario":2, "interesses": [{"estética":0.765}, {"jiujitsu":0.921}, {"luta":0.884}, {"academia":0.541}, {"maquiagem":0.658}]},
        {"usuario":3, "interesses": [{"tecnologia":0.999}, {"hardware":0.865}, {"games":0.745}, {"culinária":0.658}, {"servers":0.54}]},
        {"usuario":4, "interesses": [{"neurociências":0.865}, {"comportamento":0.844}, {"skinner":0.854}, {"laboratório":0.354}, {"pesquisa":0.428}]}
    ]
    questao_2(interests)
    #mostrar_interesses()

test_questao_2()


#Questão 3
def questao_3(posts):
    now = datetime.now()
    five_hours_ago = now - timedelta(hours=5)
    for post in posts:
        post_time = datetime.strptime(post['data_hora'], '%Y-%m-%d %H:%M:%S')
        if post_time > five_hours_ago:
            post_key = f"post:{post['id']}"
            redis_conn.hset(post_key, mapping=post)

def consultar_posts():
    post_keys = redis_conn.keys("post:*")
    posts = []
    for key in post_keys:
        posts.append(redis_conn.hgetall(key))
    return posts

def mostrar_posts():
    posts = consultar_posts()
    for post in posts:
        print(f"ID: {post['id']}, Autor: {post['autor']}, Data/Hora: {post['data_hora']}, Conteúdo: {post['conteudo']}, Palavras-chave: {post['palavras_chave']}")

# Teste
def test_questao_3():
    posts = [
        {"id": '345', "autor":"news_fc@g.com", "data_hora": "2024-06-10 19:51:03", "conteudo": "Se liga nessa lista de jogadores que vão mudar de time no próximo mês!", "palavras_chave": "brasileirao, futebol, cartola, esporte" },
        {"id": '348', "autor":"gastro_pub@g.com", "data_hora": "2024-06-10 19:55:13", "conteudo": "Aprenda uma receita rápida de onion rings super crocantes.", "palavras_chave": "onion rings, receita, gastronomia, cerveja, culinária" },
        {"id": '349', "autor":"make_with_tina@g.com", "data_hora": "2024-06-10 19:56:44", "conteudo": "A dica de hoje envolve os novos delineadores da linha Rare Beauty", "palavras_chave": "maquiagem, estética, beleza, delineador" },
        {"id": '350', "autor":"samarantes@g.com", "data_hora": "2024-06-10 19:56:48", "conteudo": "Eu quando acho a chuteira que perdi na última pelada...", "palavras_chave": "pelada, futebol, cerveja, parceiros" },
        {"id": '351', "autor":"portal9@g.com", "data_hora": "2024-06-10 19:57:02", "conteudo": "No último mês pesquisadores testaram três novos medicamentos para ajudar aumentar o foco.", "palavras_chave": "neurociências, tecnologia, foco, medicamento" },
        {"id": '352', "autor":"meme_e_cia@g.com", "data_hora": "2024-06-10 19:58:33", "conteudo": "Você prefere compartilhar a nossa página agora ou daqui cinco minutos?", "palavras_chave": "entretenimento, engraçado, viral, meme" },
        {"id": '353', "autor":"rnd_hub@g.com", "data_hora": "2024-06-10 19:59:59", "conteudo": "A polêmica pesquisa de V. Damasco sobre ciência do comportamente acaba de ser publicada.", "palavras_chave": "comportamento, ciência, pesquisa, damasco" }
    ]
    questao_3(posts)
    #mostrar_posts()

test_questao_3()

#questão 4
def questao_4(user_id):
    user_interests_key = f"user:{user_id}:interests"
    user_interests = dict(redis_conn.zrange(user_interests_key, 0, -1, withscores=True))
    post_keys = redis_conn.keys("post:*")
    scored_posts = []

    for post_key in post_keys:
        post = redis_conn.hgetall(post_key)
        post_keywords = post['palavras_chave'].split(", ")
        post_score = sum(user_interests.get(keyword, 0) for keyword in post_keywords)
        scored_posts.append((post['conteudo'], post_score))

    scored_posts.sort(key=lambda x: x[1], reverse=True)
    return [post for post, score in scored_posts]


def mostrar_posts_interessantes(user_id):
    posts_interessantes = questao_4(user_id)
    for post in posts_interessantes:
        print(post)


# Teste
def test_questao_4():
    user_id = 3
    output = [
        "No último mês pesquisadores testaram três novos medicamentos para ajudar aumentar o foco.",
        "Aprenda uma receita rápida de onion rings super crocantes.",
        "Se liga nessa lista de jogadores que vão mudar de time no próximo mês!",
        "A dica de hoje envolve os novos delineadores da linha Rare Beauty",
        "Eu quando acho a chuteira que perdi na última pelada...",
        "Você prefere compartilhar a nossa página agora ou daqui cinco minutos?",
        "A polêmica pesquisa de V. Damasco sobre ciência do comportamente acaba de ser publicada."
    ]
    #mostrar_posts_interessantes(user_id)

test_questao_4()


#questão 5
def questao_5(user_views, user_id):
    for view in user_views:
        user_key = f"user:{view['usuario']}:viewed"
        for post_id in view['visualizado']:
            redis_conn.sadd(user_key, post_id)


def consultar_posts_nao_vistos(user_id):
    viewed_key = f"user:{user_id}:viewed"
    all_posts = redis_conn.keys("post:*")
    unseen_posts = []

    for post_key in all_posts:
        post_id = post_key.split(":")[1]
        if not redis_conn.sismember(viewed_key, post_id):
            post = redis_conn.hgetall(post_key)
            unseen_posts.append(post['conteudo'])

    return unseen_posts


def mostrar_posts_nao_vistos(user_id):
    posts_nao_vistos = consultar_posts_nao_vistos(user_id)
    for post in posts_nao_vistos:
        print(post)


# Teste
def test_questao_5():
    user_views = [
        {"usuario": 1, "visualizado": [345, 350, 353]},
        {"usuario": 2, "visualizado": [348, 351, 352]},
        {"usuario": 3, "visualizado": [349, 351, 353]},
        {"usuario": 4, "visualizado": [345, 348, 352]}
    ]

    output = [
        "Aprenda uma receita rápida de onion rings supoer crocantes.",
        "A dica de hoje envolve os novos delineadores da linha Rare Beauty",
        "Eu quando acho a chuteira que perdi na última pelada..."
    ]
    
    questao_5(user_views, user_id=1)
    mostrar_posts_nao_vistos(user_id=1)


test_questao_5()
