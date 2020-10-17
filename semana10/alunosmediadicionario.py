def media(dicionario):
    media =0  
    while True:
        chave = input("Informe a matrícula do aluno: ").strip()
        if chave =='':
            break
        if chave in dicionario.keys():
            for nome, n1, n2 in dicionario.values():
                nome, n1, n2 = dicionario[chave]
                media = (n1+n2)/2
        print(f'{nome}: {media:.2f}')    

def main():
    dic_notas= {}
    while True:
        matricula = input("Matricula do aluno: ").strip()
        if matricula == '':
            break
        nome = input("Nome do aluno: ").strip()
        nota1 = float(input("Nota: "))
        nota2 = float(input("Nota: "))

        dic_notas[matricula]=nome, nota1,nota2
    print(dic_notas)

    media(dic_notas)

if __name__=='__main__':
    main()