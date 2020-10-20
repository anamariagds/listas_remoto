from unicodedata import normalize
#FUNÇAÕ QUE REMOVE ACENTUAÇÃO, MAS NÃO ESPAÇOS E OUTROS CARACTERES
#RETORNA TEXTO SEM ACENTO EM NOVA VARIÁVEL
def remover_acento(txt):
    s = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    return s     

#CONTA AS OCORENCIAS DO CARACTER E DEVOLVE EM DICIONARIO COMO CHAVE E A REPETIÇÃO COM RESPECTIVO VALOR    
def conta_ocorrencias(s):
    ocorrencias = {}
    for c in s:
        if c in ocorrencias:
                ocorrencias[c] = ocorrencias[c] + 1
        else:
                ocorrencias[c] = 1
    return ocorrencias

#REMOVE CARACTERES COMO ESPAÇO DO DICIONÁRIO PARA NÃO CONTAR
#PARA ISSO ELE ADD EM OUTRO DICIONÁRIO PARA NÃ APONTAR ERRO QUANDO REMOVER A CHAVE DO ORIGINAL
#E RETORNA O ORIGINAL SEM ESSES VALORES
def remove_esp(qntdd):
    espaco= {}
    for k,v in qntdd.items():
        if k in (' '',''!''.'';''('')'':''/''-''_''<''>'):
            espaco[k]=v
        
    for crt in espaco:
        if crt in espaco.keys():
            if crt in qntdd.keys():
                del qntdd[crt]        
    return qntdd
            
def main():
    #RECEBE UM TEXTO PELO TECLADO E PÕE EM CAIXA ALTA E ADD CARACTER ESPAÇO(.STRIP())
    txt = input("Texto: ").upper().strip()
    #chama função para remover acentuação, passando texto como paramêtro e salva em outra variável
    s_txt =remover_acento(txt)
    #chama função que conta a repetição das letras passando o texto novo sem acento
    #função que devolve dicionário onde a letra é a chave e as vx que aparece no texto é o valor
    qntdd = conta_ocorrencias(s_txt)
    
    #chama função que remove espaço pois a que remove acento não remove espaços e alguns caracteres
    #passa o dicionário anterior como parametro, imprime o valor retornado, só letras!
    print(remove_esp(qntdd))
    
if __name__=='__main__':
    main()
