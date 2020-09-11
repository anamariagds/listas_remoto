def media_dos_cem(n): 
    soma = 0   
    for i in range(n):
        alg = int(input("Digite um número: "))
        soma += alg
    media = soma/n
        
    return media
            

    

def main():
    media = media_dos_cem(100)
    print(f'A média dos cem números digitados é {media:.2f}')
    

if __name__=='__main__':
    main()