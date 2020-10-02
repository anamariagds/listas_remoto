#preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4
#(quatro) casas decimais.
def com_reais(n):
    reais = []
    for i in range(n):
        reais.append(float(input("Número: ")))
      
    reais.reverse()    
    print(reais)
#preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1
#uma) casa decimal. Se n = 0, imprima “SEM NOTAS”.
def notas_media(n):
    notas = []
    media = 0
    for i in range(n):
        notas.append(float(input(f'Nota {i+1}: ')))
        media = sum(notas)/len(notas)
    print(notas)
    if n ==0:
        print("SEM NOTAS")
    else:
        print(f'{media:.1f}')

#preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as
#consoantes. Dica: certifique-se de ler apenas um caractere com input()[0]
def letras(n):
    letras = []
    consoante= []
    vog = 0
    for i in range(n):
        let = input("Digite uma letra: ")[0]
        letras.append(let)
    for v in letras:
        if v.upper() in 'AEIOU':
            vog +=1
        elif v.upper() in 'BCDFGHJKLMNPQRSTVXYZW':
            consoante.append(v)
    print(vog)
    print(consoante)
                    
def main():
    n = int(input("Tamanho da Lista: "))
    com_reais(n)
    notas_media(n)
    letras(n)

if __name__=='__main__':
    main()