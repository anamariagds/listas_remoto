def conceito(n):
    if n>= 8.5:
        print("A")
    elif n >=7.0:
        print("B")
    elif n >=5.0:
        print("C")
    elif n >=4:
        print("D")
    elif n>=0:
        print("E")
    
def main():
    nota = float(input("Informe a nota do Aluno: "))
    while (nota < 0) or (nota >10):
        print("Nota inválida.")
        nota = float(input("Informe a nota do Aluno: "))
       
    aluno = conceito(nota)

if __name__=='__main__':
    main()


