
import random

# Criar a Board 9x9
#Criar com números aleatórios -> Verificar quais dão problema -> remover eles -> Board Randomizada!
def criarBoard(lado=9, altura=9):
    listaGrande = []
    for _um in range(altura):
        listaGrande.append([])
        for _ in range(lado):
            # listaGrande[_um].append(random.randrange(1,9))
            listaGrande[_um].append(0)
    return listaGrande


#######################

def printBoard(listaGrande):
    quadrante1 = slice(0,3*3)
    quadrante2 = slice(3*3,6*3)
    quadrante3 = slice(6*3,9*3)
    # ┏ ━ ┃ ┣ ┫ ┻ ┳ ╋ ┓ ┗ ┛
    #https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal/21786287#21786287
    #\x1b[estilo;cor(30-38);background(40-48)
    CRED = ""
    CEND = ""
    # CRED = '\x1b[1;31;40m'
    # CEND = '\x1b[0m'
    alfabeto = 'ABCDEFGHI'
    out = "  "
 
    # Imprimir letras
    for espaco in range(9):
        multi = 3 if espaco % 3 == 0 and espaco != 0 else 2
        out += " "*multi + alfabeto[espaco]
    # Tabela em si + Numeros do lado
    out += '\n'
    out += "  " + CRED + "┏" + ("━"*9 + "┳")*2 + "━"*9 + "┓" + CEND
    out += '\n'

    # Linha 1

    for linha in range(3):
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += "⠀"+f"{cadaItem}" + "⠀"
            else:
                valor += "⠀⠀⠀"
        out += f"{linha+1} " + "┃" + f"{valor[quadrante1]}" + "┃" + f"{"".join(valor[quadrante2])}" + "┃" + f"{"".join(valor[quadrante3])}" + "┃" + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫"
    out += '\n'

    #Linha 2

    for linha in range(3, 6):
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += "⠀"+f"{cadaItem}" + "⠀"
            else:
                valor += "⠀⠀⠀"
        out += f"{linha+1} " + "┃" + f"{valor[quadrante1]}" + "┃" + f"{"".join(valor[quadrante2])}" + "┃" + f"{"".join(valor[quadrante3])}" + "┃" + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫"
    out += '\n'

    #Linha 3

    for linha in range(6, 9):
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += "⠀"+f"{cadaItem}" + "⠀"
            else:
                valor += "⠀⠀⠀"
        out += f"{linha+1} " + "┃" + f"{valor[quadrante1]}" + "┃" + f"{"".join(valor[quadrante2])}" + "┃" + f"{"".join(valor[quadrante3])}" + "┃" + '\n'
    out += "  " +"┗" + ("━"*9 + "┻")*2 + "━"*9 + "┛"
    print(out)



def checkLinha(listaGrande, posLetra, posNumero, valor, jogar=0) -> bool:
    ###
    #Checar linha VERICAL
    for checarLinha in range(8):
        if listaGrande[checarLinha][posLetra] == valor:
            if jogar == 1: print("X - Valor já em coluna") 
            return False
    
    # Checar Coluna
    for cadaValor in listaGrande[posNumero]:
        if cadaValor  == valor:
            if jogar == 1: print("X - Valor já em linha")
            return False
        
    #Fazendo qual é o quadrante do valor jogado
    if posLetra < 3:
        quadrante = quadrante1
        quadrantenslide = 0
    elif 3 < posLetra < 6:
        quadrante = quadrante2
        quadrantenslide = 3
    else:
        quadrante = quadrante3
        quadrantenslide = 6
    #Verifica todos os valores no quadrante que o jogador que jogar
    for quadranteVertical in range(0+quadrantenslide, 3+quadrantenslide):
        #Pequena optimização para não contar as casas que não tenham valores
        if not sum(listaGrande[quadranteVertical][quadrante]) == 0:
            for casas in listaGrande[quadranteVertical][quadrante]:
                if casas == valor:
                    if jogar == 1: print("X - Valor já em quadrante")
                    return False
    
    return True

def criarValores(listaGrande, dificuldade):
    iteracao = 0
    while iteracao < dificuldade:
        #Pegar Posições e valores randômicos

        # REESCREVER TUDO! 123456789 -> 012345678 para todos e dai vai tirando uns ae

        pos1 = random.randrange(8)
        pos2 = random.randrange(8)
        valor = random.randrange(1, 9)
        # Se essa posição não ter valor:
        if listaGrande[pos1][pos2] == 0:
            while not checkLinha(listaGrande, pos2, pos1, valor, 0): # Enquanto o valor não poder ser colocado, ele vai fazer denovo os valores
                    # Acho que isso não vai dar certo, no final tudo vai pra ->->->-> dai vai descendo
                    for pos1 in range(0, 8, random.randrange(1,2)):
                        if listaGrande[pos1][pos2] == 0:
                            if checkLinha(listaGrande, pos2, pos1, valor, 0):
                                break
                        
                    for pos2 in range(0, 8, random.randrange(1,2)):
                        if listaGrande[pos1][pos2] == 0:
                            if checkLinha(listaGrande, pos2, pos1, valor, 0):
                                break
                        
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



# O Jogo
listaGrande = criarBoard()



criarValores(listaGrande, 80)


###Testes
# listaGrande[1][1] = 2
# listaGrande[6][1] = 3
####
printBoard(listaGrande)
jogar = 1
while jogar == 1:

    ### Ir para o final, ainda pra teste
    ### Achei erro que não sei corrigir. Se a pessoa pode reescrever (porque ela por errar) quer dizer que ela pode reescrever valores já colocados ali, e não sei como verificar sem usar uma gambiarra enorme e no fim não funcionar. Ix
    print("Você pode reescrever valores se achou que errou!")
    pos_valor = input("LETRA, NUMERO da casa e o valor ('casa':A1 'valor':2)" + '\n').upper().split()
    

    while pos_valor[0][0].upper() not in 'ABCDEFGHI' and pos_valor[0][1] not in '123456789' and pos_valor[0] != None:
        pos_valor[0] = input("Posição inválida")
    while not 0 < int(pos_valor[1]) <= 9:
        pos_valor[1] = input("Valor inválido")
    

    # Deixar valores em sua forma final
    posLetra = ord(pos_valor[0][0]) - ord('A')
    posNumero = int(pos_valor[0][1]) - 1
    valor = int(pos_valor[1])

    if checkLinha(listaGrande, posLetra, posNumero, valor, 1):
        listaGrande[posNumero][posLetra] = valor
        printBoard(listaGrande)





    # Isso ta errado, nem funciona, mas quero ter um jeito de acabar o jogo.
    if 0 in listaGrande:
        jogar = 0
        break
print("O jogo acabou!")