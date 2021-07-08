print("*********************************")
print("Bem vindo ao Jogo de adivinhação")
print("*********************************")

numero_secreto =42
total_de_tentativas = 3
rodada = 1


while (rodada <=total_de_tentativas):

    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute = int(input("Digite seu numero: "))

    print("Você digitou ", chute)

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if acertou:
        print("Acertou Miseravi")
    else:
        if chute_maior:
            print("Errrrrrou! chute maior que numero secreto!")
        elif chute_menor:
            print("Errrrrrou! chute menor que numero secreto!")

    rodada += 1

print("End Game")