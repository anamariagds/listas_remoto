def com_reais(n):
    reais = []
    for i in range(n):
        x = float(input("Digite um número real "))
        reais.append(x)
    print(reais)

def notas_media(n):
    notas = []
    media = 0
    if n == 0:
        print(f'SEM NOTAS')
    else:
        for i in range(n):
            notas.append(float(input("Notas: ")))
        return sum(notas)/len(notas)
        print(notas)
def letras(n):
    letras = []
    consoante= []
    vog = 0
    for i in range(n):
        let = input()
        letras.append(let)
    for v in letras:
        if v.upper() in 'AEIOU':
            vog +=1
        elif v.upper() in 'BCDFGHJKLMNPQRSTVXYZW':
            consoante.append(v)
    print(vog)
    print(consoante)
                    
def main():
    n = int(input("Tamanho da lista: "))
    com_reais(n)
    notas_media(n)
    letras(n)

if __name__ == '__main__':
    main()