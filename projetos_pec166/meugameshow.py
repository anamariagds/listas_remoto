from random import *
def porta():
    score = 0
    jogando = True

    while jogando == True:
    
        ponto = randint(1,10)
        score += ponto

        print("Seu próximo número é", ponto)
        print("Sua pontuação agora é", score)
        print("\nVocê gostaria de somar mais um número? (s/n)")

        resposta = input().lower()[0]

        if resposta =='n':
            jogando = False
    if score == 21:
        print(f'Parabéns!')
    
def main():
    print(''' 
Vinte e um!
========
Tente fazer exatamente 21 pontos!''')
    porta()


if __name__=='__main__':
    main()