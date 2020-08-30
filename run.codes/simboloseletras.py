def alfabeto(l):
    vogal = 'a e i o u'
    consoante = 'b c d f g h j k l m n p q r s t v x z y w' 
    if l.lower() in vogal :
        return f'vogal'
    elif l.lower() in consoante:
        return f'consoante'  
    elif l.isdigit():
        return f'número'
    else:
        return f'símbolo' 
    
def  main():
    l = input()

    eleeh = alfabeto(l)

    print(eleeh)

if __name__== "__main__":
    main()