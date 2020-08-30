def alfabeto(l):
    vogal = 'a e i o u'
    consoante = 'b c d f g h j k l m n p q r s t v x z y w' 
    if l.lower() in vogal :
        return "Vogal"
    elif l.lower() in consoante:
        return "Consoante"

    if l in ('0 1 2 3 4 5 6 7 8 9'):
        return "Número"
    else:
        return "Simbolo"
    
def  main():
    l = input("Diga a letra: ")

    print(alfabeto(l))

if __name__== "__main__":
    main()