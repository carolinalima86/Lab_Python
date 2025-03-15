import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = '' .join(random.choice(caracteres) for _  in range(tamanho))
    return senha
try:
    tamanho_senha = int(input("digite o tamaho da senha desejada"))
    nova_senha = gerar_senha(tamanho_senha)
    print(f"sua senha gerada é: {nova_senha}")
except ValueError:
    print("Por favor, insira um número válido.")