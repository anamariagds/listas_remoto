def menore_q(nome, idade, altura):
    med =round(sum(altura)/len(altura), 2)
    p =0
    
    for p in range(len(idade)):
            if idade[p]> 13 and altura[p]< med:
                print(nome[p])
def main():
    nome =[]
    idade=[]
    altura=[]

    for i in range(30):
        nome.append(input("Nome do aluno: "))
        idade.append(int(input("Idade do respectivo: ")))
        altura.append(float(input("E sua altura: "))) 
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    menore_q(nome, idade, altura)

if __name__=='__main__':
    main()  
 