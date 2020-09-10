def melhor_de(n):
    melhor_nota = 0
    melhor_aluno =''

    for k in range(n):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Informe a respectiva nota: "))

        if nota > melhor_nota:
            melhor_aluno = nome
            melhor_nota = nota
    return melhor_aluno, melhor_nota

def main():
    nome, nota = melhor_de(10)
    print(f'O melhor aluno é {nome}')
    print(f'Nota:{nota:.2f}')

if __name__=='__main__':
    main()
