def alfabeto(l):
    letra = 'a e i o u b c d f g h j k l m n p q r s t v x z y w' 
    if l.lower() in letra:
        return True

    if l in ('0 1 2 3 4 5 6 7 8 9'):
        return True
    else:
        return False
    
def  main():
    l = input()

    print(alfabeto(l))

if __name__== "__main__":
    main()

