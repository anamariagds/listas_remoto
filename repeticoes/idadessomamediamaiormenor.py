def idades():
    soma = 0
    c = 0
    maior = 0
    menor = 0

    while True:
        idade = int(input("Digite a idade "))
        soma += idade
        c +=1
        if idade == 0:
            c -=1
            break

        if c == 1:
            maior = idade
            menor = idade
        else:
            if idade > maior:
                maior = idade
            if idade < menor:
                menor = idade
    return c, soma, maior, menor 

def main():
    people, sm, mx, mn = idades()
    
    media_idade = 0
    if sm >0:
        media_idade = sm/people

        print(f'{people} pessoas informaram a idade')
        print(f'A idade média do grupo é {media_idade:.2f} anos')

    if mx != 0 and mn != 0:
        print(f'A maior idade informada foi {mx} anos e a menor foi {mn} anos')



if __name__=='__main__':
    main()