print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto= 42
chute_str= input("digite o seu número: ")

print('você digitou', chute_str)

chute = int(chute_str)

if (numero_secreto == chute) :
    print('você acertou!')
else:
    print('você errou')


