import pygame

WIDTH, HEIGHT = 400, 400
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
restartimage = pygame.image.load('./restartImage.png')
restartimage = pygame.transform.scale(restartimage, (50, 50))
restartRect = pygame.Rect(337.5, 25, 75, 75)
player = 1
init = False
playing = True

class Block(pygame.sprite.Sprite):
  def __init__(self, sx, sy):
    pygame.sprite.Sprite.__init__(self)
    self.rect = pygame.Rect([sx, sy, 75, 75])
    self.type = "empty"

block_group = pygame.sprite.Group()

array = [[0 for x in range(3)] for y in range(3)]


def checkWin():
  row1 = array[0][0] + array[0][1] + array[0][2]
  row2 = array[1][0] + array[1][1] + array[1][2]
  row3 = array[2][0] + array[2][1] + array[2][2]
  col1 = array[0][0] + array[1][0] + array[2][0]
  col2 = array[0][1] + array[1][1] + array[2][1]
  col3 = array[0][2] + array[1][2] + array[2][2]
  diag1 = array[0][0] + array[1][1] + array[2][2]
  diag2 = array[0][2] + array[1][1] + array[2][0]
  check = [row1, row2, row3, col1, col2, col3, diag1, diag2]
  for i in check:
      if i == 3 or i == -3:
          return True
  return False

def checkDraw():
  draw = True
  for i in range(3):
    for j in range(3):
      if(array[i][j] == 0):
        draw = False
  return draw

def draw():
  global player
  global restartimage
  pygame.draw.rect(screen, (66, 245, 176), (0, 0, 400, 400))
  pygame.draw.rect(screen, (20, 189, 172), (155, 55, 7.5, 240))
  pygame.draw.rect(screen, (20, 189, 172), (237.5, 55, 7.5, 240))
  pygame.draw.rect(screen, (20, 189, 172), (80, 130, 240, 7.5))
  pygame.draw.rect(screen, (20, 189, 172), (80, 212.5, 240, 7.5))
  myfont = pygame.font.SysFont("consolas", 25)
  for block in block_group:
    if (block.type == "circle"):
      pygame.draw.circle(screen, (255, 255, 255), (block.rect.x + 37.5, block.rect.y + 37.5), 35, 10)
    if (block.type == "cross"):
      pygame.draw.line(screen, (0, 0, 0), (block.rect.x + 5, block.rect.y + 5),
                        (block.rect.x + 70, block.rect.y + 70), 10)
      pygame.draw.line(screen, (0, 0, 0), (block.rect.x + 70, block.rect.y + 5),
                        (block.rect.x + 5, block.rect.y + 70), 10)
  if(checkWin()):
    playerText = "Player " + str(player) + " won" 
  elif(checkDraw()):
    playerText = "Draw"
  else:
    playerText = "Player " + str(player) + "'s turn"

  playerLabel = myfont.render(playerText, True, (59, 65, 66))
  gameLabel = myfont.render("Tic Tac Toe", True, (59, 65, 66))
  screen.blit(playerLabel, (200-(playerLabel.get_rect().width/2), 310))
  screen.blit(gameLabel, (125.5, 12.5))
  screen.blit(restartimage, (337.5, 25))


def update():
  global player
  global playing
  global restartimage
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
      if restartRect.collidepoint(pygame.mouse.get_pos()):
        restart()
        return
      if playing == True:
        for block in block_group:
          if block.rect.collidepoint(pygame.mouse.get_pos()):
            if array[block.i][block.j] == 0:
              if player == 1:
                block.type = "circle"
                array[block.i][block.j] = 1
              else:
                block.type = "cross"
                array[block.i][block.j] = -1
                
              if checkWin() or checkDraw():
                playing = False
                return
              if player == 1:
                player = 2
              else:
                player = 1


def createBlocks():
  for i in range(0, 3):
    for j in range(0, 3):
      cell = Block(80 + 82.5 * i, 55 + 82.5 * j)
      cell.i = i
      cell.j = j
      block_group.add(cell)

def restart():
  global player
  global init
  global playing 
  for i in range(3):
    for j in range(3):
      array[i][j] = 0
  player = 1
  block_group.empty()
  init = False
  playing = True

while True:
  if (init == False):
    init = True
    createBlocks()
  update()
  draw()
  pygame.display.update()
