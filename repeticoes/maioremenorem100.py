def maior(n):
    maior = 0
    for i in range(n):
        dgt = int(input(f'Digite o {i+1}º número: '))
        if dgt>maior:
            maior = dgt
    return maior
            
def main():  
  
    mx = maior(100)
    print(f'O maior número digitado foi {mx}')

  

if __name__=='__main__':
    main()