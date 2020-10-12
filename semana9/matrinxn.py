def maior(m):
    mx = m[0][0]
    pmx = ()
    
    for i in range(len(m)):
        for j in range(len(m[i])):      
            if m[i][j] >mx:
                pmx = i,j
                mx = m[i][j]
            elif mx == m[0][0]:
                pmx = 0,0
               
    print(pmx)  
    
def menor(m):
    mnr = m[0][0]
    pm = ()
    for i in range(len(m)):
        for j in range(len(m[i])):      
            if m[i][j] < mnr:
                pm = i,j
                mnr = m[i][j]
            elif mnr == m[0][0]:
                pm = 0,0    
            
    print(pm)

def main():
    linhas = colunas = int(input("Tamanho: "))
    m = []
     #para o tamanho da n de linhas cria uma lista vazia
    for linn in range(linhas):
        linha = []
        #para o tamanho n de colunas, a
        #  linha vazia recebe os valores informados pelo usuario a cada ciclo de nlinhas
        for col in range(colunas):
            x = int(input("valores: "))
            linha.append(x)
         #a matriz m recebe a linha no fim de cada ciclo de nlinhas
        m.append(linha)
    print(m)
    maior(m)
    menor(m)

if __name__=='__main__':
    main()