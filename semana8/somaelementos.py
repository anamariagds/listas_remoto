def soma_elemento(n):
    l1 = []
    l2 = []
    l3 = []

    for k in range(n):
        l1.append(int(input()))
        
    for k in range(n):
        l2.append(int(input()))

    for i in range(n):
        l3.append(l1[i]+l2[i])
    print(l1)
    print(l2)
    print(l3)


def main():
    soma_elemento(4)

if __name__=='__main__':
    main()