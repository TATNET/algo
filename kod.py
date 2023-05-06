spis = []
i = input('введите чего-нибудь (stop):')
while i != 'stop':
    if i in spis:
        print('это уже есть')
    else:
        spis.append(i)

    i = input('введите чего-нибудь (stop):')

print(spis)
input()