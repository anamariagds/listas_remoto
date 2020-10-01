def recebe_numeros(n):
    lista1 = []
    mult = 1
    for i in range(n):
        lista1.append(int(input(f'Digite o número {i+1} de {n}: ')))
        mult *=lista1[i]
        soma = sum(lista1)
    print(lista1)
    return soma, mult

def main():
    soma, mult =recebe_numeros(10)
    print(f'A soma dos números é {soma} e a mutiplicação é {mult}')
    
if __name__ == '__main__':
    main()