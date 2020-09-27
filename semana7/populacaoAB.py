# -*- coding: utf-8 -*-
def maior_populacao():
    t = 0
    pop_A = float(input("População A: "))
    pop_B = float(input("População B: "))

    maior = pop_A
    menor = pop_B

    if pop_B > maior:
        maior = pop_B
    if pop_A<menor:
        menor = pop_A

    while maior>menor:
        t +=1
        maior *=1.02
        menor *=1.03
        
        if menor > maior:
            print(t)
            break
        
def main():
    maior_populacao()
    

if __name__=='__main__':
    main()