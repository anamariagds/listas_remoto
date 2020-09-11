def sequencia(inicio, fim, step):
    seq =''
    for c in range(inicio, fim, step):
        seq += str(c)+ ',' +' '
        if c == 990:
            seq += str(1000) + '.'
            
    return seq.strip()    
def main():
    s = sequencia(10, 1000,10)
    print(s)

if __name__=='__main__':
    main()