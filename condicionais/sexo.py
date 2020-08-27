def tratamento(gen):
    if gen == 'M':
        return 'Ilmo senhor'
    else gen == 'F':
        return 'Ilma senhora'


def main():
    #Entrada de dados
    nome = input("Informe seu nome:\n")
    sexo = input("F- feminino ou M-masculino\n")
    
    diga = tratamento(sexo)
    
    print('{diga} {nome}')

if __name__== '__main__':
    main()
