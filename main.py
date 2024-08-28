
import random

# Criar a Board 9x9
#Criar com números aleatórios -> Verificar quais dão problema -> remover eles -> Board Randomizada!
def criarBoard():
    listaGrande = []
    for _um in range(9):
        listaGrande.append([])
        for _dois in range(9):
            # listaGrande[_um].append(random.randrange(1,9))
            listaGrande[_um].append(0)
            
    return listaGrande

#######################

def printBoard(listaGrande):
    # ┏ ━ ┃ ┣ ┫ ┻ ┳ ╋ ┓ ┗ ┛
    alfabeto = 'ABCDEFGHI'
    out = "  "
    # Imprimir letras
    for espaco in range(9):
        multi = 3 if espaco % 3 == 0 and espaco != 0 else 2
        out += " "*multi + alfabeto[espaco]
    # Tabela em si
    out += '\n'
    out += "  " +"┏" + ("━"*9 + "┳")*2 + "━"*9 + "┓"
    out += '\n'
    for linha in range(3):
        out += f"{linha+1} " + "┃" + f"{listaGrande[linha][quadrante1]}" + "┃" + f"{listaGrande[linha][quadrante2]}" + "┃" + f"{listaGrande[linha][quadrante3]}" + "┃" + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫"
    out += '\n'
    for linha in range(3, 6):
        out += f"{linha+1} " + "┃" + f"{listaGrande[linha][quadrante1]}" + "┃" + f"{listaGrande[linha][quadrante2]}" + "┃" + f"{listaGrande[linha][quadrante3]}" + "┃" + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫"
    out += '\n'
    for linha in range(6, 9):
        out += f"{linha+1} " + "┃" + f"{listaGrande[linha][quadrante1]}" + "┃" + f"{listaGrande[linha][quadrante2]}" + "┃" + f"{listaGrande[linha][quadrante3]}" + "┃" + '\n'
    out += "  " +"┗" + ("━"*9 + "┻")*2 + "━"*9 + "┛"
    print(out)


def checkLinha(listaGrande, posLetra, posNumero, valor) -> bool:
    ###
    #Checar linha VERICAL
    for valorVertical in range(9):
        if not valorVertical == posNumero:
            if listaGrande[valorVertical][posLetra] == valor:
                return False

    for valorColuna in range(9):
        if not valorColuna == posLetra:
            if listaGrande[posNumero][valorColuna] == valor:
                return False

    if posLetra < 3:
        quadrante = quadrante1
        quadrantenslide = list(range(0,3))
    elif 3 < posLetra < 6:
        quadrante = quadrante2
        quadrantenslide = list(range(3,6))
    else:
        quadrante = quadrante3
        quadrantenslide = list(range(6,9))
    
    for quadranteVertical in quadrantenslide:
        for casas in listaGrande[quadranteVertical][quadrante]:
            if casas == valor:
                return False
    
    return True

def criarValores(listaGrande, dificuldade):
    iteracao = 0
    while iteracao < dificuldade:
        pos1 = random.randrange(1, 8)
        pos2 = random.randrange(1, 8)
        valor = random.randrange(1, 9)
        if listaGrande[pos1][pos2] == 0:
            while not checkLinha(listaGrande, pos1, pos2, valor):
                    pos1 = random.randrange(1, 8)
                    pos2 = random.randrange(1, 8)
                    valor = random.randrange(1, 9)
            listaGrande[pos1][pos2] = valor
            iteracao += 1

####### Criar uma predefinição de quadrante pra ter uma divisão entre as linhas
quadrante1 = slice(0,3)
quadrante2 = slice(3,6)
quadrante3 = slice(6,9)
#######
# [Numero da linha] [Quadrante]
#######



jogar = 1

#jogo em si

listaGrande = criarBoard()

criarValores(listaGrande, 30)


###Testes
listaGrande[2][2] = 2
####
while jogar == 1:

    ### Ir para o final, ainda pra teste
    printBoard(listaGrande)
    ###
    pos_valor = input("LETRA, NUMERO da casa e o valor ('casa':A1 'valor':2)" + '\n').upper().split()
    while pos_valor[0][0].upper() not in 'ABCDEFGHI' or pos_valor[0][1] not in '123456789':
        pos_valor[0] = input("Posição inválida")
    while not 0 < int(pos_valor[0][1]) < 9 or pos_valor[0][1] == None:
        pos_valor[1] = input("Valor inválido")
    
    posLetra = ord(pos_valor[0][0]) - ord('A')
    posNumero = int(pos_valor[0][1]) - 1
    valor = int(pos_valor[1])

    if checkLinha(listaGrande, posLetra, posNumero, valor):
        listaGrande[posNumero][posLetra] = valor





    for range in range(9):
        if not 0 in listaGrande[range]:
            jogar = 0
            break
print("O jogo acabou!")