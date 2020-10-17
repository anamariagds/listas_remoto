def agenda(n):
    agenda = {}    

    for i in range(n):

        nome = input("Nome da pessoa: ").strip()
        cidade = input("Cidade que mora: ").strip()
        estado = input("Estado: ").strip()
        fone = input("Telefone: ").strip()

        agenda[i] = nome, cidade, estado, fone      
        
    for nome, cidade, estado, fone in agenda.values():
        esta = f'{cidade}({estado})'
        print("{:24} {:29} {}".format(nome, esta, fone))

    
    
def main():
    n = int(input("Quantas pessoas vai adicionar?: "))
    agenda(n)

if __name__=='__main__':
    main()



    
    