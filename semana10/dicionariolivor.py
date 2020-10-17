def catalogo_book():
    dicionario ={}
    matricula =100

    while True:
        matricula += 1
        titulo = str(input("Título do livro: ")).strip()
        if titulo == '':
            break
        else:
            isbn = input("Registro ISBN: ").strip()
            autor = input("Autor: ").strip()
            preco = float(input("Preço do livro: "))

            dicionario[matricula]= titulo, isbn, autor, preco

    for i in dicionario:
        titulo, isbn, autor, preco = dicionario[i]
        print(f'Código: {i}')
        print(f'Título: {titulo}')
        print(f'ISBN: {isbn}')
        print(f'Autor: {autor}')
        print(f'Preço: {preco:.2f}')

def main():
    catalogo_book()


if __name__=='__main__':
    main()


 