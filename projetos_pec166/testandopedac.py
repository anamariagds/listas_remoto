
score = 0
def q1(marcou):
    if marcou.lower() == 'a':
        global score
        score = score+1
        return f'Certa!'
    elif marcou.lower() == 'b':
        return f'Pense um pouco'
    elif marcou.lower() == 'c':
        return f'Estude mais!'   
    else:
        return f'Você não escolheu uma alternativa válida.' 
        
def main():
    print(''' Que nome leva o movimento em que a Terra gira ao redor de sim mesma, ou seja, ao redor do seu próprio eixo?

       a- Rotação
       b - Translação
       c - Precessão
     ''')
    rspt = str(input())
    r = q1(rspt)
    print(r)

if __name__=='__main__':
    main()