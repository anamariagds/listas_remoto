def bugs(n,m,p):
    for i in range(n,m+1,p):
        print(f'{i} bugs no software, pegue sete deles e conserte...')
        print("Tecle " + '"Ctrl+F5"')
    
    print("Vamos fazer mais um café!")

def main():
    bugs(99,250,7)

if __name__=='__main__':
    main()