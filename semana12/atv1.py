#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvxwyz"

#a chave secreta é 3
chave = int(input("Qual a chave?: "))

letra = input("Por favor, entre com uma letra para criptografar: ")

#encontre a posição da letra em alfabeto
#exemplo: 'a' está na posição 0, 'e' esta na  posição 4

posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a posição da letra criptografada
novaPosicao = (posicao + chave) %26 #%26 significa 'volte para 0 quando chegar em 26'

#a letra criptografada está no alfabeto na nova posição
letraCriptografada = alfabeto[novaPosicao]

print("Sua letra criptografada é ", letraCriptografada)
