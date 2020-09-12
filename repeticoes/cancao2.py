def bugs(n,m):
    for i in range(n,m+1):
        print(f'{i} bugs no software, pegue um deles e conserte...')
        print("Tecle " + '"Ctrl+F5"')
    
    print("Vamos fazer mais um café!")

def main():
    bugs(99,250)

if __name__=='__main__':
    main()