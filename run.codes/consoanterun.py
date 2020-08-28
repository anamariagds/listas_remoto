def consoante(l):
    if l.lower() in 'bcdfghjklmnpqrstvxzwy':
        return True
    else:
        return False    

def  main():
    l = str(input())

    print(consoante(l))

if __name__== "__main__":
    main()

