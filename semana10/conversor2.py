def dicionario():
    texto = {
        "rs": "risos",
        "tbm": "também",
        "vc": "você",
        "pq": "porque",
        "vlw": "valeu"
    }
    #obtém a frase para tradução
    sentence = input("Insira uma frase: ").lower()

    #divide a frase em uma lista de palavras
    palavraTOlista = sentence.split()

    transformaFrase = ""

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




def main():
    dicionario()

if __name__=='__main__':
    main()