from random import *

executa = True

adjetivos = adjetivos = ['maravilhosa', 'acima da média', 'excelente']
hobbies = ['andar de bicicleta', 'programar', 'fazer chá']

print("Gerador de cumprimentos")

nome = input("Qual é o seu nome?: ")
print('''  
Menu
    c = obter cumprimento
    a = adicionar hobby
    d = remover hobby
    p = imprimir hobbies
    q = sair
''')
while executa == True:
    menuChoice = input("\n>_").lower()

    if menuChoice == 'c':
        print("Aqui está o seu cumprimento", nome, ":")
        print(nome, "Você é", choice(adjetivos), "em", choice(hobbies))
        print("De nada!")
        #'a' para adicionar hobby
    elif menuChoice == 'a':
        itemToAdd = input("Adicione o hobby: ")
       
        if itemToAdd in hobbies:
            print("Esse hobby já está na lista!")
        else:
            hobbies.append(itemToAdd)


        #'d' remove hobby
    elif menuChoice =='d':
        itemToDelete =input("Insira o hobby a ser removido: ")
       #só remove se existir na lista
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
        else:
            print("O hobby não está na lista!") 
    
    elif menuChoice =='p':
        print(hobbies)
    elif menuChoice =='q':
        executa = False
    else:
        print("Insira opção válida!")