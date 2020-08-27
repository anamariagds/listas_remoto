def tratamento(mn):
    if mn == 1:
        return 'Ilmo Sr.' 
    elif mn == 2:
        return 'Ilma Sra.'
   

def main():
    #Entrada de dados
    nome = str(input())

    sexo = int(input())
    
    diga = tratamento(sexo)
    
    print(f'{diga} {nome}')

    
if __name__== '__main__':
    main()
