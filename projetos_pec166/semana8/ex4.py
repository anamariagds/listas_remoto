from random import *

executa = True

adjetivos = adjetivos = ['maravilhosa', 'acima da média', 'excelente']
hobbies = ['andar de bicicleta', 'programar', 'fazer chá']

print("Gerador de cumprimentos")

nome = input("Qual é o seu nome?: ")
print('''  
Menu
    c = obter cumprimento
    q = sair
''')
while executa == True:

    menuChoice = input("\n>_").lower()

    ##'c' para um cumprimento
    if menuChoice == 'c':

        print("Aqui está o seu cumprimento", nome , ":")

        print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
        print("De nada!")

    #obtem um item aleatório de ambas as listas e adiciona-os ao cumprimento
    elif menuChoice == 'q':
        executa = False
    else:
        print("Escolha uma opção válida!")
