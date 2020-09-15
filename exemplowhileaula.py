#repetição com teste no início
from random import randrange, seed
seed()
def tem_saude_e_dinheiro():
    return bool(randrange(10))

def main():
    while tem_saude_e_dinheiro():
        print("Aproveite a vida!")
    print("Não tem mais saúde e dinheiro :( ")

if __name__=='__main__':
    main()