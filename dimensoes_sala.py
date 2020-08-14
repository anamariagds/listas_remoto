altura = int(input("Informe a altura da sala em m: "))
compr = int(input("Informe o comprimento da sala em m: "))
largura = int(input("e a largura da sala em m: "))

area_piso= largura*compr
volume_sala= largura*compr*altura
area_das_paredes = 2 * altura * largura + 2 * altura * compr

print("O piso da sala tem", area_piso,"m²","O volume da sala é",volume_sala,"m³ e as paredes tem",area_das_paredes,"m²" )