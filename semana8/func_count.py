def conta(l, el):
    t=0
#valores de p no (0, len-1)
    for p in range(len(l)):
        #se na posição p(atual) o valor for esse soma 1
        if l[p]==el:
            t+=1
    print(f'Esse número aparece {t} vezes.')

def main():
    l=[]
    while True:
        n = int(input('Elementos da lista: '))
        l.append(n)
        if n ==0:
            l.pop()
            break
    el = int(input("Qual número verificar?: "))
    print(l)
    print(el)   

    conta(l, el)
if __name__=='__main__':
    main()