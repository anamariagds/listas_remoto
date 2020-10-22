def menu():
    print("trdtr de exprss")
    print("="*13)
    print("Menu: ")
    print('''
    c = converter uma frase
    p = imprimir dicionário
    a = adicionar uma palavra
    d = remover uma palavra 
    q = sair 
    ''')

def convertetxt(texto):
    sentence = input("Insira uma frase: ").lower()
    transformaFrase = ""
    #remove pontuação
    for char in '?!.,':
        sentence = sentence.replace(char,'')
    palavraTOlista = sentence.split()

    #passa por cada palavra da lista
    for palavra in palavraTOlista:

        #adiciona a palavra traduzida caso ela exista no dicionário
        if palavra in texto:
            transformaFrase += texto[palavra] + " "

        #mantém a palavra original caso não exista tradução
        else:
            transformaFrase += palavra + " "
    
    print("==>")
    print(transformaFrase)



def addDicionario(texto):
    txtToAdd = input("Insere a expressão a ser adicionada ao dicionário: ")
    signfcd = input("O que ela quer dizer? : ")
    
    texto[txtToAdd]= signfcd

def deleteitem(texto):
    txtTOdelete = input("Expressão pra remover: ")
    #remove a expressão, se ela pertencer ao dicionário se não nada acontece
    if txtTOdelete in texto.keys():
        del texto[txtTOdelete]
    else:
        pass

def main():
    texto = {
        "rs" : "risos",
        "tbm" : "também",
        "vc" : "você",
        "pq" : "porque"
    }
    running = True

    menu()

    #repete até que o usuário digite 'q' para sair
    while running == True:
        escolhaMenu = input(">_").lower()

        #c para converter
        if escolhaMenu == 'c':
            convertetxt(texto)
        
        #p para imprimir
        elif escolhaMenu == 'p':
            print(texto)
        #a para adicionar 
        elif escolhaMenu == 'a':
            addDicionario(texto)
        
        #d para remover
        elif escolhaMenu == 'd':
            deleteitem(texto)
        #q para sair
        elif escolhaMenu == 'q':
            running = False
        else:
            print("Escolha inválida")
        

if __name__=='__main__':
    main()