def dicionario():
    texto = {
        "rs": "risos",
        "tbm": "também"
    }
    #Imprime dicionário completo
    print("Dicionário=", texto)
    #imprime apenas o conteúdo relacionado à chave "rs"
    print("\nrs =", texto["rs"])
    #texto que pede a entrada do usuário
    key = input("\nO que você gostaria de converter? : ")
    print(key, "=", texto[key])

def main():
    dicionario()

if __name__=='__main__':
    main()