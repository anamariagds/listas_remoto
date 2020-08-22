def mostrahora(s):
    hr = s //3600
    s = s % 3600
    mnts = s // 60
    sg = s % 60
    return f'{hr}:{mnts}:{sg}'

def main():
    seg = int(input())
    duracao = mostrahora(seg)

    print(duracao)

if __name__== '__main__':
    main()