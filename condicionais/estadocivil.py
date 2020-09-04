def caracteres_n(nome,ec):
    qtd = len(nome)
    if ec.upper() == 'C':
        conj = str(input("Informe o nome do seu ou sua parceiro(a): "))
        qnt = len(nome + conj)
    return qtd

def main():
    nm = str(input("Informe seu nome: "))
    ec = str(input("Informe seu estado cilvil: C- casado(a), S-Solteiro(a): "))
    
    
    letras = caracteres_n(nm, ec)
    print(letras)

    
if __name__=='__main__':
    main()