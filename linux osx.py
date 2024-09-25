# Importando comandos
import random # Para a randomização e a diversidade dos jogos
from os import system # Limpar o terminal para não ficar poluido visualmente.

# Criar a Board 9x9
def criarBoard(lado=9, altura=9):
    listaGrande = []
    for _um in range(altura): # Cria cada linha
        listaGrande.append([])
        for _ in range(lado): # Cria cada conteúdo na linha (0)
            listaGrande[_um].append(0) # Cria um 9x9 com 0 em todos os locais
    return listaGrande

def printTitle():
    # Printar o título do jogo, pois ele é usado mais que uma vez no código.
    print('┏' + '━'*53 + '┓')
    print('┃ ███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗ ┃')
    print('┃ ██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║ ┃')
    print('┃ ███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║ ┃')
    print('┃ ╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║ ┃')
    print('┃ ███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝ ┃')
    print('┃ ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ┃')
    print('┗' + '━'*53 + '┛')

# Printar a Board
def printBoard(listaGrande, prefix='\x1b[0m'):
    printTitle()
    print("Você pode reescrever valores se achou que errou!")
    print("0 para apagar um valor")
    # Divide o tabuleiro em slices
    quadrante1 = slice(0,3*3)
    quadrante2 = slice(3*3,6*3)
    quadrante3 = slice(6*3,9*3)
    # ┏ ━ ┃ ┣ ┫ ┻ ┳ ╋ ┓ ┗ ┛ <- Borda do tabuleiro para bonito
    #https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal/21786287#21786287
    # /\ Post no StackOverflow que achei para a mudança de cor no terminal sem precisar importar nenhuma library
    #\x1b[estilo;cor(30-38);background(40-48)
    posfix = '\x1b[0m' # Colocar um valor no final de [0m para dizer que acabou a customização
    # a função "printBoard()" tem o parámetro de prefix, complementar ao posfix.
    # O Prefix vai ser inserido na frente de todos os valores para qualquer mudança de cor, estilo ou cor de fundo.
    # O normal do prefixo é [0m, dizendo que não tem alteração
    # CRED = '\x1b[1;31;40m' <- exemplo de um texto vermelho
    alfabeto = 'ABCDEFGHI' # Alfabeto para imprimir por iteração
    out = "  "
 
    # Imprimir letras
    for espaco in range(9):
        multi = 3 if espaco % 3 == 0 and espaco != 0 else 2
        out += " "*multi + alfabeto[espaco]
    # Tabela em si + Numeros do lado
    out += '\n'
    out += "  "  + "┏" + ("━"*9 + "┳")*2 + "━"*9 + "┓" # Parte de cima
    out += '\n'

    # Linha 1

    for linha in range(3): # Pra cada linha, ele vai pegar o valor no tabuleiro.
        # Se o valor for 0, no tabuleiro vai printar um espaço " ", assim, deixando mais fácil de ver espaços vazios.
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += " "+f"{cadaItem}" + " "
            else:
                valor += "   " # Usando o sistema do ( Prefix - Numero1 - Numero2 - Numero3 - Posfix ) para definir uma cor.
                # Aqui também é usado o 'quadrante', para ver melhor os valores de cada lugar, sem ser manual toda linha
        out += f"{linha+1} " + "┃" + prefix + f"{valor[quadrante1]}" + posfix + "┃" + prefix +f"{''.join(valor[quadrante2])}"+ posfix + "┃" + prefix + f"{''.join(valor[quadrante3])}"+ posfix + "┃"  + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫" # acabando a linha colocando as barreiras
    out += '\n' # Acabando com uma quebra de linha para a próxima linha

    #Linha 2 - Se repete o sistema acima, apenas mudando os números

    for linha in range(3, 6):
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += " "+f"{cadaItem}" + " "
            else:
                valor += "   "
        out += f"{linha+1} " + "┃" + prefix + f"{valor[quadrante1]}" + posfix + "┃" + prefix +f"{''.join(valor[quadrante2])}"+ posfix + "┃" + prefix + f"{''.join(valor[quadrante3])}"+ posfix + "┃"  + '\n'
    out += "  " +"┣" + ("━"*9 + "╋")*2 + "━"*9 + "┫"
    out +=  '\n'

    #Linha 3

    for linha in range(6, 9):
        valor = ""
        for cadaItem in listaGrande[linha]:
            if  cadaItem != 0:
                valor += " "+f"{cadaItem}" + " "
            else:
                valor += "   "
        out += f"{linha+1} " + "┃" + prefix + f"{valor[quadrante1]}" + posfix + "┃" + prefix +f"{''.join(valor[quadrante2])}"+ posfix + "┃" + prefix + f"{''.join(valor[quadrante3])}"+ posfix + "┃"  + '\n'
    out += "  " +"┗" + ("━"*9 + "┻")*2 + "━"*9 + "┛"
    print(out)

def checkLinha(listaGrande, posLetra, posNumero, valor, feedback=0) -> bool:
    ###
    #Checar linha VERICAL
    for checarLinha in range(8):
        if listaGrande[checarLinha][posLetra] == valor:
            # O feedback é usado para que, se eu quiser verificar em um """Backend""" ele não printe algo para o jogador
            if feedback == 1: print("X - Valor já em coluna") 
            return False # Se verificar que existe um valor na Vertical, ele já quebra o código e retorna que não é possível fazer o movimento
    
    # Checar Coluna
    if valor in listaGrande[posNumero]:
        if feedback == 1: print("X - Valor já em linha")
        return False # Se verificar que existe um valor na Coluna, ele já quebra o código e retorna que não é possível fazer o movimento
        
    #Pegando qual é o quadrante na linha do valor jogado (Horizontal)
    if posLetra < 3:
        quadrante = quadrante1
    elif 3 <= posLetra < 6:
        quadrante = quadrante2
    else:
        quadrante = quadrante3
    
    # Quadrante na coluna (Vertical)
    if posNumero < 3:
        quadrantenslide = 0
    elif 3 <= posNumero < 6:
        quadrantenslide = 3
    else:
        quadrantenslide = 6

    #Verifica todos os valores no quadrante 
    for quadranteVertical in range(0+quadrantenslide, 3+quadrantenslide): # Iterando por 3 valores no slice Horizontal do tabuleiro linha1 -> linha2 -> Linha3
        if valor in listaGrande[quadranteVertical][quadrante]: # Se na linha ter o valor que o jogador quer jogar, ele retorna falso, falando que não é possível fazer o movimento
            if feedback == 1: print("X - Valor já em quadrante") # Feedback para o jogador
            return False

    return True # Se passar por todos os requisitos, ele retorna Verdadeiro, confirmando que está tudo certo.

def criarValores(listaGrande: list, offset=random.randint(0,8)):
    # O offset é o quão pra frente a contagem dos números do tabuleiro irá iniciar
    # Criando um offset aleatório como opicional.
    offset -= 1 # Diminuindo 1 para não ter conflito depois
    
    # Em cada quadrante, ele vai pegar o offset, e começar um valor por lá.
    for quadra in range(1, 10): #Fazer com cada quadrante
        offset+=1 if offset < 8 else -8 # Resetando o offset se exceder o limite
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
        # Iniciando o valor do offset.
        # Se o valor irá começar depois de tantos quadrados, tem que existir valores antes.
        # Esse valor antes é o dobro do offset contando ao contrário. Ex: se o offset for 2, então 2*2 = 4. O valor deve ser 2 valores atrás do que deve começar
        # Se começar na casa 2, então volta 4 valores, Indo para o 8. Então 8 e 9 precisa colocar antes de contar do 1 até o 7 (ou 9-offset)
        # Mas para não ter que fazer tudo isso, apenas usando 9-offset já resolve
        offsetCalculoInverso = offset
        criarValoresValor = 9-offsetCalculoInverso
        for linhaAgora in linha:
            if not criarValoresValor == 9:
                # cria um valor final para a quadra, mas ao contrário. Começando pelo fim e indo para o começo
                # Se a quadra irá acabar no 7, então aqui começa a imprimir o 8 e 9, dai começa o 1 até o 7

                # Tabuleiro sem essa função:
                # 0 0 1
                # 2 3 4
                # 5 6 7

                # Tabuleiro com essa função:
                # 8 9 1
                # 2 3 4
                # 5 6 7

                while criarValoresValor < 9:
                    posicao += 1
                    offsetCalculoInverso -= 1
                    if posicao == 3: 
                        posicao = -1
                        break
                    criarValoresValor += 1
                    listaGrande[linhaAgora][posicao+quadrante] = criarValoresValor

                    # Resultado =
                    # 8 9 0
                    # 0 0 0
                    # 0 0 0

            if criarValoresValor == 9:
                if posicao+1 == 3:
                    posicao = -1
                    continue
                posicao += 1
                # Se os valores finais já forem feitos, então começa a contagem normal
                while True:
                    
                    valorAtual +=1                    
                    # Começa da ultima posição do cálculo final, e vai contando do 1 até o valor final (Até aonde puder)
                    listaGrande[linhaAgora][posicao+quadrante] = valorAtual

                    if posicao+1 == 3:
                            posicao = -1
                            break

                    posicao += 1

def excluirValores(board, dificuldade: int):
    # Exclui valores no tabuleiro dependendo da dificuldade
    # A dificuldade é apenas o nome. Essa função irá excluir valores igual á dificuldade
    # dificuldade = 10, 10 numeros excluidos da lista.
    i = 0
    quadrado = -1 # Começando uma iteração randomizada, não usei for-loop para a randomização
    linha = 0
    while i < dificuldade:

        quadrado += random.randrange(1, 3) # Adiciona um valor de 1 até 3, para não excluir em linha reta
        linha += random.randrange(0,3) if dificuldade <= 40 else 0 # Se a dificuldade for muito baixa, ela nunca iria sair das primeiras linhas, então essa linha faz que, se o valor for menor que a metade do tabuleiro, ele começe a randomizar o valor das linhas também.


        if quadrado > 8: # Se o valor do quadrado excedeu o limite, volta 8 e adiciona 1 linha
            quadrado -= 8
            linha += 1

        if linha > 8: # Se a linha excedeu o limite, volta a 0
            linha -= 8

        if board[linha][quadrado] != 0: # Verificando se o local que quero colocar é válido (Tem um número para excluir, impossibilitanto ele excluir números já excluidos)
            board[linha][quadrado] = 0 # Exclui o número
        else:
            i -= 1 # Se não conseguir excluir, ele vai diminuir 1, fazendo a iteração ter +1 passo
        
        i+=1 # SEMPRE adicionando 1 a iteração. (Por isso o i -=1 se o valor já for excluido)


# Criar uma predefinição de quadrante pra ter uma divisão entre as linhas
quadrante1 = slice(0,3)
quadrante2 = slice(3,6)
quadrante3 = slice(6,9)

# O Jogo
listaGrande = criarBoard() # Criar o tabuleiro do jogo
menu = 1 # Definindo Menu como 1 para ter o Loop principal do jogo


while menu == 1:
    # Printando o título "Sudoku" com alguns efeitos bonitos para o jogador
    printTitle()
    print('---------> Selecione a dificuldade do jogo <----------')
    print('┏' + '━'*3 + '┓' + ' '*15, end='')
    print('┏' + '━'*3 + '┓' + ' '*15, end='')
    print('┏' + '━'*3 + '┓' + ' '*15)
    print('┃ A ┃', end='')
    print(' Fácil' + ' '*9, end="")
    print('┃ B ┃', end='')
    print(' Médio' + ' '*9, end="")
    print('┃ C ┃', end='')
    print(' Difícil')
    print('┗' + '━'*3 + '┛' + ' '*15, end='')
    print('┗' + '━'*3 + '┛' + ' '*15, end='')
    print('┗' + '━'*3 + '┛' + ' '*15)
    # Printa os valores bonitos para o jogador saber a dificuldade que ele quer escolher
    selectDificuldade = input("").lower()

    dificuldade = 0 # Iniciando a variável Dificuldade para uso futuro
    # facil = 10
    # medio = 40
    # dificil = 60

    while dificuldade == 0: # Começar um loop para verificar a dificuldade que o jogador selecionou
        # Se o valor que o jogador digitou for um número, esse número vai ser a dificuldade do jogo
        if selectDificuldade.isdigit():
            dificuldade = int(selectDificuldade)
            if dificuldade < 1: dificuldade = 1
        else: # Se não ele vai verificar com 3 tipos diferentes de jeitos que o jogador poderia ter escrito para selecionar a dificuldade
            # Sendo "A" o valor na caixa. "facil" sendo o nome da dificuldade, ou só 'f' a letra inicial da dificuldade
            if selectDificuldade == "a" or selectDificuldade == "facil" or selectDificuldade == 'f':
                dificuldade = 10
            elif selectDificuldade == "b" or selectDificuldade == "medio" or selectDificuldade == 'm':
                dificuldade = 40
            elif selectDificuldade == "c" or selectDificuldade == "dificil" or selectDificuldade == 'd':
                dificuldade = 60
            
            if dificuldade == 0: # No final de  tudo, se a dificuldade continuar sendo 0, significa que ela não foi alterada, e que o jogador colocou um valor inválido
                # Então só vai pedir denovo o valor e repetir a operação toda.
                selectDificuldade = input("Nenhum valor válido. tente novamente").lower()

    # Cria todos os valores do tabuleiro
    criarValores(listaGrande)
    # E exclui dependendo da dificuldade. Se o valor for 10 (Fácil), irá excluir 10 digitos
    excluirValores(listaGrande, dificuldade)
    # Limpar o terminal para limpar tudo antes de começar o jogo
    system('clear')
    printBoard(listaGrande) # Printar o Tabuleiro
    jogar = 1 # Definindo a variável Jogar para começar o Loop de jogo

    while jogar == 1:

        ### Achei erro que não sei corrigir. Se a pessoa pode reescrever (porque ela por errar) quer dizer que ela pode reescrever valores já colocados ali, e não sei como verificar sem usar uma gambiarra enorme e no fim não funcionar. Ix    
        pos_valor = input("LETRA, NUMERO da casa e o valor ('casa':A1 'valor':2)" + '\n').upper().split()
        # Pegar o input do jogador dividindo em uma lista para melhor filtração dos valores
        
        # Verificando se o valor que o jogador colocou é válido
        while pos_valor[0][0].upper() not in 'ABCDEFGHI' or pos_valor[0][1] not in '123456789':
            pos_valor[0] = input("Posição inválida")
        while not -1 < int(pos_valor[1]) <= 9:
            pos_valor[1] = input("Valor inválido")
        

        # Deixar valores em sua forma final
        posLetra = ord(pos_valor[0][0].upper()) - ord('A') # Deixando a letra como INT para mais fácil utilização
        posNumero = int(pos_valor[0][1]) - 1 # Ajustando o valor do número para que o python possa entender (Já que começa no 0 e não no 1)
        valor = int(pos_valor[1]) # O valor que o usuário quer colocar no local da jogada

        
        if valor == 0 or checkLinha(listaGrande, posLetra, posNumero, valor, 1): # Verificando se a jogada é possível
            system('clear') # Limpando o terminal
            listaGrande[posNumero][posLetra] = valor # Atualizando o valor
            printBoard(listaGrande) # Printando o tabuleiro denovo


        # Verificar se o jogo acabou
        naoacabar = False 
        for linha in listaGrande:
            if 0 in linha:
                # Ele vai passar por todas linhas, e se ALGUMA linha sequer ter o valor 0, ele vai atualizar o naoacabar, colocando como verdadeiro
                # E quebrando o loop, dizendo que ainda tem 0's no tabuleiro, então o jogo não acabou
                naoacabar = True
                break
        # Se não achar nenhum 0, ele acaba o loop 'jogo'
        if naoacabar == False:
            jogar = 0
            break

    system('clear')
    printBoard(listaGrande, '\x1b[1;32;1m') # a função "printBoard()" tem um parámetro opcional para colocar um prefixo de cor no texto. Quando alguém ganha, o texto fica todo verde! Melhor documentação na função
    print("O jogo acabou! Você ganhou!")
    select = input("Deseja continuar jogando ou acabar? (c/a)").lower() # Verificando se o jogador que continuar ou acabar o jogo
    if select == 'a':
        menu = 0
        break

