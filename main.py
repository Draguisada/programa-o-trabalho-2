
import random
from os import system

# Criar a Board 9x9
#Criar com números aleatórios -> Verificar quais dão problema -> remover eles -> Board Randomizada!
def criarBoard(lado=9, altura=9):
    listaGrande = []
    for _um in range(altura): # Cria cada linha
        listaGrande.append([])
        for _ in range(lado): # Cria cada conteúdo na linha (0)
            # listaGrande[_um].append(random.randrange(1,9))
            listaGrande[_um].append(0)
    return listaGrande


#######################

def printBoard(listaGrande):
    print("Você pode reescrever valores se achou que errou!")
    print("0 para apagar um valor")
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
                valor += " "+f"{cadaItem}" + " "
            else:
                valor += "   "
        out += f"{linha+1} " + "┃" + f"{valor[quadrante1]}" + "┃" + f"{"".join(valor[quadrante2])}" + "┃" + f"{"".join(valor[quadrante3])}" + "┃" + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫"
    out += '\n'

    #Linha 2

    for linha in range(3, 6):
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += " "+f"{cadaItem}" + " "
            else:
                valor += "   "
        out += f"{linha+1} " + "┃" + f"{valor[quadrante1]}" + "┃" + f"{"".join(valor[quadrante2])}" + "┃" + f"{"".join(valor[quadrante3])}" + "┃" + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫"
    out += '\n'

    #Linha 3

    for linha in range(6, 9):
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += " "+f"{cadaItem}" + " "
            else:
                valor += "   "
        out += f"{linha+1} " + "┃" + f"{valor[quadrante1]}" + "┃" + f"{"".join(valor[quadrante2])}" + "┃" + f"{"".join(valor[quadrante3])}" + "┃" + '\n'
    out += "  " +"┗" + ("━"*9 + "┻")*2 + "━"*9 + "┛"
    print(out)



def checkLinha(listaGrande, posLetra, posNumero, valor, feedback=0) -> bool:
    ###
    #Checar linha VERICAL
    for checarLinha in range(8):
        if listaGrande[checarLinha][posLetra] == valor:
            if feedback == 1: print("X - Valor já em coluna") 
            return False
    
    # Checar Coluna
    if valor in listaGrande[posNumero]:
        if feedback == 1: print("X - Valor já em linha")
        return False
        
    #Fazendo qual é o quadrante na linha do valor jogado
    if posLetra < 3:
        quadrante = quadrante1
    elif 3 < posLetra <= 6:
        quadrante = quadrante2
    else:
        quadrante = quadrante3
    
    # Quadrante na coluna
    if posNumero < 3:
        quadrantenslide = 0
    elif 3 <= posNumero < 6:
        quadrantenslide = 3
    else:
        quadrantenslide = 6

    #Verifica todos os valores no quadrante que o jogador que feedback
    for quadranteVertical in range(0+quadrantenslide, 3+quadrantenslide):
        if valor in listaGrande[quadranteVertical][quadrante]:
            if feedback == 1: print("X - Valor já em quadrante")
            return False

    return True

def criarValores(listaGrande: list, dificuldade: int, offset=random.randint(0,8)):
    offset -= 1
    
    # Pegar primeiro+criar uma lista de 123456789 com um offset no bloco
    for quadra in range(1, 10): #Fazer com cada quadrante
        offset+=1 if offset < 8 else -8
        posicao = -1
        valorAtual = 0

        # Pegando o quadrante atual para fazer as decisões
        if quadra <= 3:
            quadrante = 0
        elif 3 < quadra <= 6:
            quadrante = 3
        else: 
            quadrante = 6

        ### Fazer as linhas que o programa deve chegar per local
        if quadra == 1 or quadra == 4 or quadra == 7:
            linha = range(0, 3)
        elif quadra == 2 or quadra == 5 or quadra == 8:
            linha = range(3, 6) 
        else: 
            linha = range(6, 9)
            
        ####
        offsetCalculoInverso = offset
        criarValoresValor = 9-offsetCalculoInverso
        for linhaAgora in linha:
            if not criarValoresValor == 9:
                
                while criarValoresValor < 9:
                    posicao += 1
                    offsetCalculoInverso -= 1
                    if posicao == 3: 
                        posicao = -1
                        break
                    criarValoresValor += 1
                    listaGrande[linhaAgora][posicao+quadrante] = criarValoresValor

            if criarValoresValor == 9:
                if posicao+1 == 3:
                    posicao = -1
                    continue
                posicao += 1
                while True:
                    
                    valorAtual +=1                    

                    listaGrande[linhaAgora][posicao+quadrante] = valorAtual

                    if posicao+1 == 3:
                            posicao = -1
                            break

                    posicao += 1
                    # Fazer sistema ao contrário slk
                

                
                



####### Criar uma predefinição de quadrante pra ter uma divisão entre as linhas
quadrante1 = slice(0,3)
quadrante2 = slice(3,6)
quadrante3 = slice(6,9)
#######
# [Numero da linha] [Quadrante]
#######



# O Jogo
listaGrande = criarBoard()



criarValores(listaGrande, 10)


###Testes
# listaGrande[1][1] = 2
# listaGrande[6][1] = 3
####
printBoard(listaGrande)
jogar = 1
while jogar == 1:

    ### Ir para o final, ainda pra teste
    ### Achei erro que não sei corrigir. Se a pessoa pode reescrever (porque ela por errar) quer dizer que ela pode reescrever valores já colocados ali, e não sei como verificar sem usar uma gambiarra enorme e no fim não funcionar. Ix
    
    pos_valor = input("LETRA, NUMERO da casa e o valor ('casa':A1 'valor':2)" + '\n').upper().split()
    

    while pos_valor[0][0].upper() not in 'ABCDEFGHI' or pos_valor[0][1] not in '123456789':
        pos_valor[0] = input("Posição inválida")
    while not -1 < int(pos_valor[1]) <= 9:
        pos_valor[1] = input("Valor inválido")
    

    # Deixar valores em sua forma final
    posLetra = ord(pos_valor[0][0].upper()) - ord('A')
    posNumero = int(pos_valor[0][1]) - 1
    valor = int(pos_valor[1])

    
    if valor == 0 or checkLinha(listaGrande, posLetra, posNumero, valor, 1):
        system('cls')
        listaGrande[posNumero][posLetra] = valor
        printBoard(listaGrande)





    naoacabar = 0
    for linha in listaGrande:
        if 0 in linha:
            naoacabar = 1
            break
    if naoacabar == 0:
        jogar = 0
        break

input("O jogo acabou! Você ganhou!")