numeros = [0, 0, 0, 0, 0]

for i in range(5):
    numeros[i] = int(input("Número  %d: " %(i + 1)))

while True:
    escolhido = int(input("Que posição você quer mostrar? (0 para sair)"))
    if escolhido == 0:
        break
    print("Você escolheu o número %d" % numeros[escolhido-1])