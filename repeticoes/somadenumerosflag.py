def soma_numeros():
    soma = 0
    while True:
        nm = int(input("Digite um número: "))
        soma += nm
        if nm == 0: break
    return soma

def main():
    s = soma_numeros()
    print("A soma dos números que você digitou é : ", s)


if __name__ == '__main__':
    main()