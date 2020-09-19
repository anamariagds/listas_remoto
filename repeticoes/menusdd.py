def menu():
    while True:
        op = int(input(
        ''' OPÇÕES:
1-Saudações
2- Bronca
3- Felicitações
0-Fim
        '''))

        if op == 1:
            print("Olá. Como vai?")
        elif op == 2:
            print("Vamos estudar mais.")
        elif op == 3:
            print("Meus Parabéns!")
        
        if op == 0:
            print("Fim de serviço.")
            break
        if op != 1 and op != 2 and op !=3 and op !=0:
            print("Opção inválida.")
    
def main():
    menu()

if __name__=='__main__':
    main() 
