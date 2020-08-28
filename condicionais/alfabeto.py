def alfabeto(l):
    if l.lower() in 'aeioubcdfghjklmnpqrstvxzwy':
        return True
    else:
        return False    

def  main():
    l = str(input("Diga a letra: "))

    print(alfabeto(l))

if __name__== "__main__":
    main()



