
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


def checkLinha(listaGrande, pos_valor, valor=0) -> bool:
    posLetra = ord(pos_valor[0][0]) - ord('A')
    posNumero = int(pos_valor[0][1]) - 1
    valor = int(pos_valor[1])
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
    elif 3 < posLetra < 6:
        quadrante = quadrante2
    else:
        quadrante = quadrante3
    
    for quadranteVertical in range(posNumero//3, (posNumero//3)+3):
        for casas in listaGrande[quadranteVertical][quadrante]:
            if casas == valor:
                return False
    
    return True


#######
quadrante1 = slice(0,3)
quadrante2 = slice(3,6)
quadrante3 = slice(6,9)
#######
# [Numero da linha] [Quadrante]
#######

#jogo em si

listaGrande = criarBoard()
###Testes
listaGrande[2][2] = 2
####
while True:
    printBoard(listaGrande)
    pos_valor = input("LETRA, NUMERO da casa e o valor").upper().split()
    while pos_valor[0][0] not in 'ABCDEFGHI' or pos[0][1] not in '123456789':
        pos_valor[0] = input("Posição inválida")
    while not 0 < int(pos_valor[1]) < 9:
        pos_valor[1] = input("Valor inválido")
    
    posLetra = ord(pos_valor[0][0]) - ord('A')
    posNumero = int(pos_valor[0][1]) - 1
    valor = int(pos_valor[1])
    if checkLinha(listaGrande, pos_valor):
        pass # AQUI




verdade = checkLinha(listaGrande, pos)
print(pos)
print(verdade)










#Posições

