#uma lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#capture a mensagem do usuário
mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

#esta variável armazena a mensagem criptografada
mensagemCriptografada= ""

#capture a chave secreta
chave = int(input("Por favor, entre a chave: "))

#percorra cada caracter na mensagem
for char in mensagem:
    if char in alfabeto:
        #encontre a posição de caracter em alfabeto
        #por exemplo, 'a' está na posição 0, 'e' está na posição 4, etc.
        posicao = alfabeto.find(char)

        #some a chave secreta para encontara a nova posição do caracter criptogafado
        novaPosicao = (posicao + chave) %26

        #acrescente a letra descriptografada à mensagem 
        #a letra criptografada está em alfabeto na novaPosicao
        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
    else:

        #alguns caracteres(por exemplo '?') não estão no alfabeto
        #então simplesmente adicone a letra criptografada à mensagem
        mensagemCriptografada = mensagemCriptografada + char

print("sua mensagem criptografda é: ", mensagemCriptografada)