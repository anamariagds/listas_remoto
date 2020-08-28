def vogal(l):
    if l in 'a A e E i I o O u U':
        return True
    else:
        return False

def main():
    letra = str(input())

    teste = vogal(letra)

    print(teste)

if __name__ == '__main__':
    main()
