import pygame 
import numpy as np

pygame.init()

alf = ['a','b','c','d','e','f','g','h']
vert = [0, 120, 240, 360, 480, 600, 720, 840]
horz = [840, 720, 600, 480, 360, 240, 120, 0]

#Funcao que retorna os pixels de cada casa
def pixel(column,row):

    for i in alf:
        if i == column:
            return(alf.index(i)*120, (8 - row)*120)

#Funcao oposta a de cima 
def inverse_pixel(v,h):
    for i in horz:
        if h == i:
            for j in vert:
                if v == j:
                    return '%s%g'%(alf[vert.index(j)],horz.index(i)+1)

def ChessBoard(self,pawn,rook,bishop,queen,king,knight):
        return pawn+rook+bishop+queen+king+knight

#Classe peças 
class Piece():
    def __init__(self,color,column,row,image):
        self.image = pygame.image.load(image)
        #Esse atributo retorna o pixel da respectiva casa
        self.position = pixel(column,row)
        self.column = column 
        self.row = row
        self.color = color

    def get_color(self): return self.color
    def get_position(self): return self.position

    #Esse metodo retorna casa da peça (em notação) 
    def square(self):
        return inverse_pixel(self.position[0],self.position[1])

    #Esse metodo move a peça
    def move(self, column,row):
        self.position =  pixel(column,row)
        self.row = row
 
#Classe Peão da super class Piece 
class Pawn(Piece):
    def __init__(self,color,column,row):
        self.p = pixel(column,row)
        if color == 'white':
            super().__init__(color,column,row,'Imagens/pawn_branco.png')
        if color == 'black':
            super().__init__(color,column,row,'Imagens/pawn_preto.png')

    def movement(self):
        movements = []

        if super().get_color() == 'white': 
            free = inverse_pixel(self.p[0], self.p[1]-120)
            for i in chessboard:
                if i.square() != free:
                    break
                else: movements.append(free)

        return print(movements)

        #if super().get_color() == 'white': 
        #    movements.append(free)

#Classe rook da super class Piece 
class Rook(Piece):
    def __init__(self,color,column,row):
        if color == 'white':
            super().__init__(color,column,row,'Imagens/rook_branca.png')
        if color == 'black':
            super().__init__(color,column,row,'Imagens/rook_preta.png')

class Knight(Piece):
    def __init__(self,color,column,row):
        if color == 'white':
            super().__init__(color,column,row,'Imagens/knight_branco.png')
        if color == 'black':
            super().__init__(color,column,row,'Imagens/knight_preto.png')

class Bishop(Piece):
    def __init__(self,color,column,row):
        if color == 'white':
            super().__init__(color,column,row,'Imagens/bishop_branco.png')
        if color == 'black':
            super().__init__(color,column,row,'Imagens/bishop_preto.png')

class Queen(Piece):
    def __init__(self,color,column,row):
        if color == 'white':
            super().__init__(color,column,row,'Imagens/queen_branca.png')
        if color == 'black':
            super().__init__(color,column,row,'Imagens/queen_preta.png')

class King(Piece):
    def __init__(self,color,column,row):
        if color == 'white':
            super().__init__(color,column,row,'Imagens/king_branco.png')
        if color == 'black':
            super().__init__(color,column,row,'Imagens/king_preto.png')

#Armazenando os Objetos (Peças) em um array
pawn = []; bishop = []; queen = []
rook = []; knight = []; king = []

for i in range(8):
    pawn.append(Pawn('white',alf[i],2)) 
    pawn.append(Pawn('black',alf[i],7))
    if i == 0 or i == 7:
        rook.append(Rook('white',alf[i],1)) 
        rook.append(Rook('black',alf[i],8))
    if i == 1 or i == 6:
        knight.append(Knight('white',alf[i],1)) 
        knight.append(Knight('black',alf[i],8))
    if i == 2 or i == 5:
        bishop.append(Bishop('white',alf[i],1))
        bishop.append(Bishop('black',alf[i],8))
    if i == 3:
        queen.append(Queen('white',alf[i],1))
        queen.append(Queen('black',alf[i],8))
    if i == 4:
        king.append(King('white',alf[i],1))
        king.append(King('black',alf[i],8))

#Vetor chesboard possui todos peças(objetos) que estão no tabuleriro
chessboard = pawn+rook+bishop+queen+king+knight

#Chessboard

#def chessBoard(Piece):
#    Piece.
#    #WhitePiece
##    np.zeros((16))  

#Função que preenche o tabluleiro
def tab_inicial():
    for i in range(16):
        gameDisplay.blit(pawn[i].image, pawn[i].position)
        if i < 4:
            gameDisplay.blit(rook[i].image, rook[i].position)
            gameDisplay.blit(knight[i].image, knight[i].position)
            gameDisplay.blit(bishop[i].image, bishop[i].position)
        if i < 2:
            gameDisplay.blit(queen[i].image, queen[i].position)
            gameDisplay.blit(king[i].image, king[i].position)

#Criar uma janela
gameDisplay = pygame.display.set_mode((960,960))

#Mudar nome
#pygame.display.set_caption('A bit Racey')


black = (0,0,0)
white = (255,255,255)

tab = pygame.image.load('Imagens/tab.jpg')

#def piece(x,y):
#    gameDisplay.blit(reiB, move('a',1))

#FPS
clock = pygame.time.Clock()

crashed = False

gameDisplay.fill(black)

#Quem está no jogo
#in_game  = [pawn1B,pawn2B,pawn3B,pawn4B,pawn5B,pawn6B,pawn7B,pawn8B]

flag = 0
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                print("Hey, you pressed the key, '0'!")
                print(pawn[2].square())
                pawn[0].move('a',4)
                gameDisplay.blit(tab, (0, 0))
                tab_inicial()

    if flag == 0 : 
        gameDisplay.blit(tab, (0, 0))
        tab_inicial()

    pygame.display.update()
    clock.tick(60)
    flag += 1


pygame.quit()
quit()
