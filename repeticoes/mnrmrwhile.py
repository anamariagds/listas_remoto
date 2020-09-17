def maior_e_menor(cont):
    maior = 0
    menor = 0
    
    while True:
        num = int(input("Digite um número: "))     
        cont +=1
    
        if num == 0: break

        if cont ==1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

    return maior, menor
           
def main():
    cont = 0       
    mx, mnr = maior_e_menor(cont)

    if mx != 0 and mnr != 0:
        print(f'O maior número digitado foi {mx} e o menor foi {mnr}')
       
if __name__ == '__main__':
    main()