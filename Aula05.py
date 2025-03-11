# Crie um programa registra as notas da turma

def registrar_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
            if entrada.lower() == 'fim':
                break
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota Inválida. digite um valor ente 0 e 10.")
        except ValueError:
            print("Entrada Inválida. Por favor digite um número ou 'fim'.")

            if notas:
                media = sum(notas) / len(notas)
                print(f"\nA Média da turma: {media:2f}")
                print(f"total de notas registradas: {len(notas)}")
            else:
                print("Nenhuma nota válida")
registrar_notas()