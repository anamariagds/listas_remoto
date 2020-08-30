def alfabeto(l):
    if l.lower() in 'a e i o u' :
        return "Vogal"
    elif l.lower() in 'b c d f g h j k l m n p q r s t v x z y w':
        return "Consoante"

    if l in '0 1 2 3 4 5 6 7 8 9':
        return "Número"
    else:
        return "Simbolo"
    
def  main():
    l = str(input())

    simbolo = alfabeto(l)

    print(simbolo)

if __name__== "__main__":
    main()