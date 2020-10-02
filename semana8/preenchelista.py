def prenche0(n):
    lista = []
#preenchendo lista com 0, mostra seu tamanho
    for i in range(n):
        lista.append(0)
    print(lista)

#preenche com valores de 1 a n
def de1a_n(n):
    lista= []
    for i in range(n):
        lista.append(i+1)
    print(lista)
#recebe elementos do usuario
def usuariopreenche(n):
    lista = []
    for i in range(n):
        lista.append(int(input(f'Informe o {i+1} inteiro: ')))
    print(lista)
#preenche e inverte
def preencheinverso(n):
    lista = []
    for i in range(n):
        x = int(input(f'Número {i+1}: '))
        lista.insert(i,x)
    lista.reverse()
    print(lista)

def main():
    #define tamanho da lista cada n um elemento dela
    n = int(input("O tamanho da lista: "))
    #chamada de funções
    prenche0(n)
    de1a_n(n)
    usuariopreenche(n)
    preencheinverso(n)

if __name__=='__main__':
    main()
