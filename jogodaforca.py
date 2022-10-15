import random

países = ['brasil','argentina','alemanha','espanha','china','inglaterra','cuba']
marcas = ['nike','adidas','gucci','puma','renner','oakley']
comidas = ['banana','arroz','carne','pipoca','salada','biscoito']
jogadores = ['ronaldinho','neymar','messi','ibrahimovic','benzema','calleri','ribamar','dembele','cavani','mbappe']
animais = ['cachorro','tartaruga','ornitorrinco','papaguaio','orangotango']


print('-' * 100)
print('Bem vindo ao jogo da forca! Você terá 4 chances para tentar acertar novamente caso erre a letra.')
print('Ao fim do jogo,se vencer irá ganhar um card de 50 riot points do Leo!')
escolha = input('Escolha um tema que deseja jogar (países,marcas,comidas,jogadores ou animais): ')

if escolha == 'países':

    palavra = random.choice(países)
    tentativas = 0
    chances = 4
    letras_escolhidas = []
    caracteres = ['_'] * len(palavra)
    print(caracteres)

    while tentativas < chances and caracteres != palavra:
        letra = input('Qual letra você deseja tentar? ')
        while letra in letras_escolhidas:
            print('Você escolheu uma letra já selecionada antes, oh cabeção.\n')
            letra = input('Qual letra você deseja tentar? ')

        letras_escolhidas.append(letra)

        if letra in palavra:
            print('Ai sim, acertasse.')
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    caracteres[i] = letra
        else:
            print('Errou otário.')
            tentativas += 1

        print('Você ainda tem {} chances.'.format(chances - tentativas))
        print('Estado atual da palavra: {}.'.format(caracteres))
        print('Letras já escolhidas: {}.'.format(letras_escolhidas))
    if tentativas == chances:
        print('Perdeu otário.')
    else:
        print('Parabéns,ganhou os riots points de Leo, ai sim.')

    print('A palavra era:', palavra)





elif escolha == 'marcas':

    palavra = random.choice(marcas)
    tentativas = 0
    chances = 4
    letras_escolhidas = []
    caracteres = ['_'] * len(palavra)
    print(caracteres)

    while tentativas < chances and ''.join(caracteres) != palavra:
        letra = input('Qual letra você deseja tentar? ')
        while letra in letras_escolhidas:
            print('Você escolheu uma letra já selecionada antes, oh cabeção.\n')
            letra = input('Qual letra você deseja tentar? ')

        letras_escolhidas.append(letra)

        if letra in palavra:
            print('Ai sim, acertasse.')
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    caracteres[i] = letra
        else:
            print('Errou otário.')
            tentativas += 1

        print('Você ainda tem {} chances.'.format(chances - tentativas))
        print('Estado atual da palavra: {}.'.format(caracteres))
        print('Letras já escolhidas: {}.'.format(letras_escolhidas))
    if tentativas == chances:
        print('Perdeu otário.')
    else:
        print('Parabéns,ganhou os riots points de Leo, ai sim.')

    print('A palavra era:', palavra)



elif escolha == 'comidas':

    palavra = random.choice(comidas)
    tentativas = 0
    chances = 4
    letras_escolhidas = []
    caracteres = ['_'] * len(palavra)
    print(caracteres)

    while tentativas < chances and ''.join(caracteres) != palavra:
        letra = input('Qual letra você deseja tentar? ')
        while letra in letras_escolhidas:
            print('Você escolheu uma letra já selecionada antes, oh cabeção.\n')
            letra = input('Qual letra você deseja tentar? ')

        letras_escolhidas.append(letra)

        if letra in palavra:
            print('Ai sim, acertasse.')
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    caracteres[i] = letra
        else:
            print('Errou otário.')
            tentativas += 1

        print('Você ainda tem {} chances.'.format(chances - tentativas))
        print('Estado atual da palavra: {}.'.format(caracteres))
        print('Letras já escolhidas: {}.'.format(letras_escolhidas))
    if tentativas == chances:
        print('Perdeu otário.')
    else:
        print('Parabéns,ganhou os riots points de Leo, ai sim.')

    print('A palavra era:', palavra)



elif escolha == 'jogadores':

    palavra = random.choice(jogadores)
    tentativas = 0
    chances = 4
    letras_escolhidas = []
    caracteres = ['_'] * len(palavra)
    print(caracteres)

    while tentativas < chances and caracteres != palavra:
        letra = input('Qual letra você deseja tentar? ')
        while letra in letras_escolhidas:
            print('Você escolheu uma letra já selecionada antes, oh cabeção.\n')
            letra = input('Qual letra você deseja tentar? ')

        letras_escolhidas.append(letra)

        if letra in palavra:
            print('Ai sim, acertasse.')
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    caracteres[i] = letra
        else:
            print('Errou otário.')
            tentativas += 1

        print('Você ainda tem {} chances.'.format(chances - tentativas))
        print('Estado atual da palavra: {}.'.format(caracteres))
        print('Letras já escolhidas: {}.'.format(letras_escolhidas))
    if tentativas == chances:
        print('Perdeu otário.')
    else:
        print('Parabéns,ganhou os riots points de Leo, ai sim.')

    print('A palavra era:', palavra)


elif escolha == 'animais':

    palavra = random.choice(animais)
    tentativas = 0
    chances = 4
    letras_escolhidas = []
    caracteres = ['_'] * len(palavra)
    print(caracteres)

    while tentativas < chances and ''.join(caracteres) != palavra:
        letra = input('Qual letra você deseja tentar? ')
        while letra in letras_escolhidas:
            print('Você escolheu uma letra já selecionada antes, oh cabeção.\n')
            letra = input('Qual letra você deseja tentar? ')

        letras_escolhidas.append(letra)

        if letra in palavra:
            print('Ai sim, acertasse.')
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    caracteres[i] = letra
        else:
            print('Errou otário.')
            tentativas += 1

        print('Você ainda tem {} chances.'.format(chances - tentativas))
        print('Estado atual da palavra: {}.'.format(caracteres))
        print('Letras já escolhidas: {}.'.format(letras_escolhidas))
    if tentativas == chances:
        print('Perdeu otário.')
    else:
        print('Parabéns,ganhou os riots points de Leo, ai sim.')

    print('A palavra era:', palavra)



else:
    print('Erro.Você não escolheu nenhuma das alternativas.')

