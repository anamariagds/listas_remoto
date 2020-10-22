def mostra(planetas):
    op= input('Informe o Planeta: ').lower()
    if op in planetas.keys():
        plnt = planetas[op]
        print(f'{op} está a {plnt} Km do Sol  ')

def main():
    #distancia relativa ao sol em km
    planet = {
        'marte': '227.940.000',
        'mercúrio': '57.910.000',
        'vênus': '108.200.000',
        'saturno': '1.429.400.000',
        'jupter': '778.330.000',
        'Terra': '149.600.000',
        'urano': '2.870.990.000',
        'netuno': '4.504.300.000'
    }
    mostra(planet)


if __name__=='__main__':
    main()