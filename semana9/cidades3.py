def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


cidades = carrega_cidades()

dia = 0
mes_pop = ()

m = int(input("Mês de aniversário: "))
popl = int(input("População: "))
mes_pop = (m, popl)

#acessa elemento 1 na tupla que corresponde ao mês
if mes_pop[0] == 1:
    mes = 'Janeiro'
elif mes_pop[0] == 2:
    mes = 'Fevereiro'
elif mes_pop[0] == 3:
    mes = 'Março'
elif mes_pop[0] == 4:
    mes = 'abril'
elif mes_pop[0] == 5:
    mes = 'Maio'
elif mes_pop[0] == 6:
    mes = 'Junho'

elif mes_pop[0] == 7:
    mes = 'Julho'

elif mes_pop[0] == 8:
    mes = 'Agosto'

elif mes_pop[0] == 9:
    mes = 'Setembro'

elif mes_pop[0] == 10:
    mes = 'Outubro'

elif mes_pop[0] == 11:
    mes = 'Novembro'

elif mes_pop[0] == 12:
    mes = 'Dezembro'

print(f'CIDADES COM MAIS DE {popl} HABITANTES E ANIVERSÁRIO EM {mes.upper()}:')  
#percorre a lista cidadede e verifica cada tupla nela. Cada tupla corresponde a uma cidade com informações da mesma.
for tupla in cidades:
    #acessa o mes da cidade no indice 4 em cada tupla, se for o mesmo mês informado vai para o proximo if
    if tupla[4] == mes_pop[0]:
        #aqui ele vai no indice 5 de cada tupla que corresponde a população. Se for maior que a informada segue pro print
        if tupla[5] > mes_pop[1]:            
            print(f'{tupla[2]}({tupla[0]}) tem {tupla[5]} habitantes e faz aniversário em {tupla[3]} de {mes.lower()}.')

def main():
    carrega_cidades()

if __name__=='__main__':
    main()           