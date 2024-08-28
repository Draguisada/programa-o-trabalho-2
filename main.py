
import random

# Criar a Board 9x9
#Criar com números aleatórios -> Verificar quais dão problema -> remover eles -> Board Randomizada!
def criarBoard():
    listaGrande = []
    for _um in range(9):
        listaGrande.append([])
        for _dois in range(9):
            listaGrande[_um].append(random.randrange(1,9))
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

def qualLinha(letra):
    if letra == A

def checkLinha(listaGrande, pos_valor):
    #Checar linha VERICAL
    for valorVertical in range(0,9):
        pass


#######
quadrante1 = slice(0,3)
quadrante2 = slice(3,6)
quadrante3 = slice(6,9)
#######
# [Numero da linha] [Quadrante]
#######

#jogo em si

listaGrande = criarBoard()
printBoard(listaGrande)
pos = input("LETRA, NUMERO da casa e o valor").split()
while pos[0][0].upper() not in 'ABCDEFGHI' or pos[0][1] not in '123456789':
    pos[0] = input("Posição inválida")
while not 0 < int(pos[1]) < 9:
    pos[1] = input("Valor inválido")

print(pos)










#Posições

