def tratamento(mn):
    if mn == 1:
        return 'Ilmo Sr. senhor' 
    elif mn == 2:
        return 'Ilma Sra. senhora'
    else:
        return f'Escolha uma opção válida,'

def main():
    #Entrada de dados
    nome = str(input("Informe seu nome: "))

    sexo = int(input("1 - maculino ou 2 - feminino: "))
    
    diga = tratamento(sexo)
    
    print(f'{diga} {nome}.')

if __name__== '__main__':
    main()
