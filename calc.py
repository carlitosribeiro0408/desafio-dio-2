def nivel(level):
    ranks = {
        1: "Ferro",
        2: "Bronze",
        3: "Prata",
        4: "Ouro",
        5: "Diamante",
        6: "Lendário",
        7: "Imortal"
    }
    return ranks.get(level)

def ratio(win, loss):
    return win - loss

# Obter entradas do usuário com validação
try:
    w = int(input("Digite o número de vitórias: "))
    l = int(input("Digite o número de derrotas: "))
except ValueError:
    print("Por favor, insira números inteiros válidos para vitórias e derrotas.")
    exit()

saldo = ratio(w, l)

# Simplificar condições
if saldo < 10:
    level = 1
elif 10 <= saldo < 20:
    level = 2
elif 20 <= saldo < 50:
    level = 3
elif 50 <= saldo < 80:
    level = 4
elif 80 <= saldo < 90:
    level = 5
elif 90 <= saldo < 100:
    level = 6
else:
    level = 7

# Mensagem de saída formatada
print(f"O herói tem um saldo de {saldo} e está no nível {nivel(level)}.")