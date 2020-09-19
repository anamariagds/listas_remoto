def conceito(n):
    if n>= 8.5:
        print("A")
    elif n >=7.5:
        print("B")
    elif n >=5.0:
        print("C")
    elif n >=4:
        print("D")
    elif n>=0:
        print("E")
    
def main():
    nota = float(input("Informe a nota do aluno: "))

    aluno = conceito(nota)

if __name__=='__main__':
    main()


