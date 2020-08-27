def quiz(resposta):
    if resposta.upper() == 'VARIAVEL':
        return f' :) '
    else:
        return f' :( '

def main():
    print(f'Em python, como se chama uma "caixa" usada para armazenar dados?\n')
    r = str(input())

    placar = quiz(r)
    print(f'{placar}')

if __name__ == '__main__':
    main()

print("Obrigada por jogar!!!")