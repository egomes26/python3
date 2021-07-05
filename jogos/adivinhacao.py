print("*********************************")
print("Bem vindo ao Jogo de adivinhação")
print("*********************************")

numero_secreto =42

chute = int(input("Digite seu numero: "))

print("Você digitou ", chute)

if(numero_secreto == chute):
    print("Acertou Miseravi")
else:
    print("Errrrrrou")

print("End Game")