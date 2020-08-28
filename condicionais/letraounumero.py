def alfabeto(l):
    if l in (0,9):
        return True
    else:
        return False    

def  main():
    l = input("Diga a letra: ")

    print(alfabeto(l))

if __name__== "__main__":
    main()

