# Função para adicionar uma pessoa a lista
def adicionar_pessoa(lista,nome,idade,profissão):
    pessoa = {"nome":nome,"idade":idade,"profissão":profissão}
    lista.append(pessoa)

# Função para mostrar as pessoas da lista

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade:{pessoa['idade']}, Profissão:{pessoa['profissão']}")

# Lista para armazenar pessoas
pessoas = []

# Adicionar pessoas em uma lista
adicionar_pessoa(pessoas,"Ana",25,"Engenheira")
adicionar_pessoa(pessoas,"Bruno",30,"Professor")
adicionar_pessoa(pessoas,"Carla",22,"Médico")


# Exibir a lista de pessoas
exibir_pessoas(pessoas)