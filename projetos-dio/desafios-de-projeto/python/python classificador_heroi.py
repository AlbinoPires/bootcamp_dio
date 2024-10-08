# Trazendo uma abordagem em python sobre o mesmo desafio

def classificar_heroi(nome, xp):
    if xp < 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    # Saída proposta para o desafio
    print(f"O Herói de nome {nome} está no nível de {nivel}")


# Função para classificar vários heróis
def classificar_varios_herois():
    numero_de_herois = int(input("Quantos heróis deseja classificar? "))

    for i in range(numero_de_herois):
        nome = input(f"Digite o nome do herói {i + 1}: ")
        xp = int(input(f"Digite a experiência (XP) do herói {nome}: "))
        classificar_heroi(nome, xp)


# Chama a função para classificar vários heróis
classificar_varios_herois()

