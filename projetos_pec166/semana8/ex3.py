from random import *

print("Gerador de cumprimentos")

adjetivos = ['maravilhosa', 'acima da média', 'excelente', 'íncrivel', 'competente']
hobbies = ['andar de bicicleta', 'programar', 'fazer chá', 'em leitura', 'cantar']

nome = input("Qual é o seu nome?: ")
print("Aqui está o seu cumprimento", nome , ":")

#obtém item aleatório de ambas as listas e adiionaós ao cumprimento

print( nome, "você é", choice(adjetivos), "em", choice(hobbies),"!")
print("De nada!")