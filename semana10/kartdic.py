from operator import itemgetter
def tempos():
    tempo=[]
    for i in range(3):
        tempo.append(float(input(f'Tempo volta {i+1} de {3}: ')))
    return tempo

def media_tmp_volta(corrida):
    media={}
    for k, v in corrida.items():
        md = sum(v)/len(v)
        media[k]=round(md, 2)
    return media

def tempo_total(corrida):
    total={}
    for k, v in corrida.items():
        soma = sum(v)
        total[k]=soma
    return total
    
def main():
    corrida= dict()
    for c in range(2):
        nome = input("Jogador: ")
        volta = tempos()
        corrida[nome]= volta
    media={}
    medias =media_tmp_volta(corrida)
    #print(tempo_total(corrida))

    ordem_melhor=[]
    ordem_melhor = sorted(medias.items(), key=itemgetter(1))

    for i in range(len(ordem_melhor)):
        print(f'{ordem_melhor[i][0]}: {ordem_melhor[i][1]}')

    
if __name__=='__main__':
    main()