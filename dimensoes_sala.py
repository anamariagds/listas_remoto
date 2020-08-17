def piso(altura, compr, largura):
    area_piso = largura*compr   
    volume_sala = largura*compr*altura
    area_das_paredes = 2 * altura* largura + 2 * altura * compr
    return area_piso,volume_sala, area_das_paredes

def main():
    altura = int(input("Informe a altura da sala em m: "))
    compr = int(input("Informe o comprimento da sala em m: "))
    largura = int(input("e a largura da sala em m: "))
    
    a = piso(altura,compr,largura)

    print(f'A área do piso, volume da sala e area das paredes são respectivamente {a}' )

if __name__ == '__main__':
    main()