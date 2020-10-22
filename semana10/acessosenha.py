def verifica(dados):
    tent= 0
    while tent <3:
        tent +=1
        nome= input('Usuário ').lower()
        senha= input('password ').lower()
        
        if nome in dados and senha == dados[nome]:
            print('Bem Vinda, Programadora!')
            break
        else:
            print(f'Senha ou usuario inválido.')

def main():
    dados= {
        'ana maria': 'floresatomicas',
        'rui': 'fluminense',
        'cat': 'peixe'
    }

    verifica(dados)

if __name__ == '__main__':
    main()