def mais_alto(n):
    nome = []
    altura =[]
    

    for i in range(n):
        nome.append(input("Nome do atleta: "))    
    for i in range(n):
        altura.append(float(input("Altura do atleta: ")))
    
    m_alto = altura.index(max(altura))
    print(nome[m_alto])
    print(altura[m_alto])

z
    media = sum(alturas)/len(alturas)


def main():
    mais_alto(3)


if __name__ == '__main__':
    main()
    