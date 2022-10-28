import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print()


def carrega_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pedir_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao = posicao + 1


def imprime_mensagem_vencedor():
    print("Você ganhou! Não foi enforcado! ")
    print("           ")
    print("   (^.^)   ")
    print("     |     ")
    print("   \ | /   ")
    print("    \|/    ")
    print("     |     ")
    print("    / \    ")
    print("   /   \   ")
    print("           ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu! Foi enforcado... ")
    print("A palavra era: {}".format(palavra_secreta))
    print("           ")
    print("   (x.x)   ")
    print("     |     ")
    print("   \ | /   ")
    print("    \|/    ")
    print("     |     ")
    print("    / \    ")
    print("   /   \   ")
    print("           ")


def desenha_forca(erros):
    print("    _______   ")
    print("  |/      |   ")

    if erros == 1:
        print("  |      (_)  ")
        print("  |           ")
        print("  |           ")
        print("  |           ")

    if erros == 2:
        print("  |      (_)  ")
        print("  |      \    ")
        print("  |           ")
        print("  |           ")

    if erros == 3:
        print("  |      (_)  ")
        print("  |      \|   ")
        print("  |           ")
        print("  |           ")

    if erros == 4:
        print("  |      (_)  ")
        print("  |      \|/  ")
        print("  |           ")
        print("  |           ")

    if erros == 5:
        print("  |      (_)  ")
        print("  |      \|/  ")
        print("  |       |   ")
        print("  |           ")

    if erros == 6:
        print("  |      (_)  ")
        print("  |      \|/  ")
        print("  |       |   ")
        print("  |      /    ")

    if erros == 7:
        print("  |      (_)  ")
        print("  |      \|/  ")
        print("  |       |   ")
        print("  |      / \  ")

    print("  |           ")
    print("__|__         ")
    print()


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    letras_faltando = len(letras_acertadas)
    print("Quantidade de letras na palavra:", letras_faltando)
    print()

    while not enforcou and not acertou:
        chute = pedir_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count("_"))
            if letras_faltando == "0":
                print("Parabéns, você acertou a palavra secreta! {}".format(palavra_secreta.upper()))
        else:
            erros += 1
            print(letras_acertadas)
            print("Ainda faltam acertar {} letras.".format(letras_acertadas.count("_")))
            print("Ops, você errou! Faltam {} tentativas.".format(7 - erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


if __name__ == '__main__':
    jogar()
