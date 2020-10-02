from random import *

executa = True

nomefemea = ['Dora', 'Amora', "Belinha", 'Mel']
nomemacho = ['Rafael', 'Dante', 'Bilie', 'Bob']

print("Escolha de nome para animal")

print("xxxxxxxxxxxxxxxxxxxxxxx")

print('''
Menu:
    a - Ver o nome
    b - Ver listas
    c - Adicionar nomes na lista
    s - Sair


''')
while executa == True:
    menu= input("\n>_").lower()[0]
    #escolhe nome na lista atual
    if menu == 'a':
        n = int(input("Quantos nomes você precisa?"))
        for i in range(n):
            print("m se macho, f se femea: ")
            eh = input()[0]
            if eh.lower() == 'f':
                print("O nome para seu pet é:", choice(nomefemea))
            elif eh.lower() =='m':
                print("O nome para seu pet é:", choice(nomemacho))
    # Ver lista:
    elif menu =='b':
        print(nomefemea)
        print(nomemacho)
    #adicionar nome na lista
    elif menu =='c':
        ql = int(input("1- para nome de femea. 2- nome de pet macho"))
        if ql == 1:
            nomeAdd = input("Adicione o nome: ")
            if nomeAdd in nomefemea:
                print("Esse nome já está na lista!")
            else:
                nomefemea.append(nomeAdd)
        
        if ql == 2:
            nomeAdd = input("Adicione o nome: ")
            if nomeAdd in nomemacho:
                print("Esse nome já está na lista!")
            else:
                nomemacho.append(nomeAdd)
    #finalizar programa
    elif menu =='s':
        executa = False
    else:
        print("Insira opção válida!")



