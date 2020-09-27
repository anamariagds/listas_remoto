def tempo(pt):
    lebre = 0
    t = 0

    while True:
        t +=1
        pt += 1
        lebre += 10
        if pt<=lebre:
            return t
            break

def main():
    tartaruga = int(input("Qual a vantagem da tartaruga? "))
    if tartaruga >=0:
        tm =tempo(tartaruga)
        print(tm)

if __name__=='__main__':
    main()

