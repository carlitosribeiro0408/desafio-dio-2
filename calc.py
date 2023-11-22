def nivel(level):
    rank={
        1:"Ferro",
        2:"Bronze",
        3:"Prata",
        4:"Ouro",
        5:"Diamante",
        6:"Lendário",
        7:"Imortal"
    }
    print(f"e está no nivel {rank.get(level)}")

def ratio(win, loss):
    return win - loss

w = int(input("Digite o número de vitórias:"))
l = int(input("Digite o número de derrotas:"))

saldo = ratio(w,l)

if saldo < 10:
    print("O herói tem de saldo", saldo, end=" ")
    nivel(1)
elif saldo > 10 < 20:
    print("O herói tem de saldo", saldo, end=" ")
    nivel(2)
elif saldo > 20 < 50:
    print("O herói tem de saldo", saldo, end=" ")
    nivel(3)
elif saldo > 50 < 80:
    print("O herói tem de saldo", saldo, end=" ")
    nivel(4)
elif saldo > 80 < 90:
    print("O herói tem de saldo", saldo, end=" ")
    nivel(5)
elif saldo > 90 < 100:
    print("O herói tem de saldo", saldo, end=" ")
    nivel(6)
elif saldo >= 101:
    print("O herói tem de saldo", saldo, end=" ")
    nivel(7)