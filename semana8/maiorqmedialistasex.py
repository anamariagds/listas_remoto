def ler_notas(n):
    notas = []
    for i in range(n):
        notas.append(float(input(f'Nota {i+1} de {n}: ')))
    return notas


def media(notas):
    return sum(notas)/len(notas)

def maiores_que(media, notas):
    maiores = []
    for nota in notas:
        if nota > media: maiores.append(nota)
    return maiores

def main():
    notas = ler_notas(7)
    m = media(notas)
    print(maiores_que(m, notas))

if __name__== '__main__':
    main()