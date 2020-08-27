def cor_sinal(cor):
    if cor.upper() == 'V':
        return f'Siga'
    elif cor.upper() == 'A':
        return f'Atenção'
    elif cor.upper() == 'E':
        return f'Pare'

def main():
    c = str(input('''Qual a cor do semaforo?
    V - verde
    A - amarelo
    E - vermelho: '''))

    fazer = cor_sinal(c)

    print(fazer)

if __name__ == '__main__':
    main()