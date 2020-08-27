score = 0
def q1(marcou):
    if marcou.lower() == 'a':
        global score
        score = score+1
        return f'correta'
    elif marcou.lower() == 'b':
        return f'errada'
    elif marcou.lower() == 'c':
        return f'errada'   
    else:
        return f'escolha não válida.' 

def q2(escolha):
    if escolha.lower() == 'a':
        return f'errada'
    elif escolha.lower() == 'b':
        return f'errada'
    elif escolha.lower() == 'c':
        global score
        score = score+1
        return f'correta'
    else:
        return f'escolha não válida.'

def q3(marcou):
    if marcou.lower() == 'a':
        return f'errada'
    elif marcou.lower() == 'b':
        global score
        score = score+1
        return f'correta'
    elif marcou.lower() == 'c':
        return f'errada'
    else:
        return f'escolha não válida.'

def q4(escolha):
    if escolha.lower() == 'a':
        return f'errada'
    elif escolha.lower() == 'b':
        return f'errada'
    elif escolha.lower() == 'c':
        global score
        score = score +1
        return f'correta'
    else:
        return f'escolha não válida.'

def mensagem(score):
    if score == 4:
        return f'Muito bem!!!'
    else:
        return f'Tente mais uma vez!'

def main():
    #questão 1
    print(''' Que nome leva o movimento em que a Terra gira ao redor de sim mesma, ou seja, ao redor do seu próprio eixo?

       a- Rotação
       b - Translação
       c - Precessão
     ''')
    #entrada
    rspt = str(input())
    #chamada da função
    r1 = q1(rspt)
    #saída
    print(r1)
    
    #questão e 2
    print('''Esse movimento é realizado aproximadamente em um período de _____?
    a - 24 horas, 0 minutos e 12 segundos.
    b - 365 dias.
    c - 23 horas, 56 minutos e 24 segundos.
    
     ''')
    #entrada da resposta
    m = str(input())
    #chamada da função
    r2 = q2(m)
    #saída
    print(r2)
    #questão 3
    print(''' Qual o movimento que a Terra realiza em torno do Sol?
    a - Rotação
    b - Translação
    c - Precessão
     ''')
    #entrada da resposta
    n = str(input())
    #chamada da função
    r3 = q3(n)
    #saída
    print(r3)

    #questão 4
    print(''' O movimento que a Terra realiza em torno do sol tem que forma?
    a - Circular
    b - Oval
    c - Elipse
     ''')
    #entrada da resposta
    p = str(input())
    #chamada da função
    r4 = q4(p)
    #saída
    print(r4)

    #saída de dados do score
    print(f'\nSua pontuação no quiz foi: {score} pontos\n')
    print(mensagem(score))
   
   
if __name__=='__main__':
    main()


