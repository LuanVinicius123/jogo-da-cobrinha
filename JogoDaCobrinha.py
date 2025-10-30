import random
import pygame
from pygame.locals import *
 

WINDOWS_WIDTH=600
WINDOWS_HEIGHT=600
POS_INICIAL_X= WINDOWS_HEIGHT/2
POS_INICIAL_Y=WINDOWS_WIDTH/2
BLOCK=10
direcao=K_UP
velocidade=10
pontos=0
pygame.font.init()
fonte=pygame.font.SysFont('arial',35,True,True) 

def colisao(x,y):
 return x==y
 

def verifica_margens(pos):
 if 0<=pos[0]<WINDOWS_WIDTH and 0<=pos[1]<WINDOWS_HEIGHT:
  return False
 else: 
  return True
def game_over():
 pygame.quit()
 quit()
obstaculo_pos=[]
def pos_aleatoria():
 x=random.randint(0,WINDOWS_HEIGHT)
 y=random.randint(0,WINDOWS_WIDTH)
 if (x,y) in obstaculo_pos:
  pos_aleatoria()
 return x//BLOCK*BLOCK,y//BLOCK*BLOCK

pygame.init()
window=pygame.display.set_mode((WINDOWS_HEIGHT,WINDOWS_WIDTH))
pygame.display.set_caption('Jogo da Cobrinha')
cobra_pos=[(POS_INICIAL_X,POS_INICIAL_Y),(POS_INICIAL_X + BLOCK,POS_INICIAL_Y),(POS_INICIAL_X +2 * BLOCK,POS_INICIAL_Y)]
cobra_surface=pygame.Surface((BLOCK,BLOCK))
maca_pos=pos_aleatoria()
maca_surface=pygame.Surface((BLOCK,BLOCK))
maca_surface.fill((255,0,0))
obstaculo_pos=[]
obstaculo_surface=pygame.Surface((BLOCK,BLOCK))
obstaculo_surface.fill((0,0,0))



while True:
 window.fill((68,189,50))
 pygame.time.Clock().tick(velocidade)
 mensagem=f'Pontos: {pontos}'
 texto=fonte.render(mensagem,True,(255,255,255))

 for evento in pygame.event.get():
  if evento.type==QUIT:
    pygame.quit()
    quit()
  elif evento.type==KEYDOWN:
    if evento.key in  [K_UP,K_DOWN,K_RIGHT,K_LEFT]:
     if evento.key==K_UP and direcao==K_DOWN:
      continue
     elif evento.key==K_DOWN and direcao==K_UP:
      continue
     elif evento.key==K_LEFT and direcao==K_RIGHT:
      continue
     elif evento.key==K_RIGHT and direcao==K_LEFT:
      continue
     else :
      direcao=evento.key 
 
 window.blit(maca_surface,maca_pos)
 if colisao(cobra_pos[0],maca_pos):
   cobra_pos.append((-10,-10))
   maca_pos=pos_aleatoria()
   obstaculo_pos.append(pos_aleatoria())
   pontos+=1
   velocidade=velocidade+(pontos*1.03)   
 for pos in obstaculo_pos:
  if colisao(cobra_pos[0],pos):
   game_over()
  window.blit(obstaculo_surface,pos)

 for pos in cobra_pos:
  
  window.blit(cobra_surface,pos) 
  
 for item in range(len(cobra_pos)-1,0,-1):
  if colisao(cobra_pos[0],cobra_pos[item]):
   game_over()
  cobra_pos[item]=cobra_pos[item-1]
 
  
 if verifica_margens(cobra_pos[0]):
   game_over()
  
   
 if direcao==K_RIGHT:
   cobra_pos[0]= cobra_pos[0][0]+BLOCK,cobra_pos[0][1] 
 elif direcao==K_LEFT:
   cobra_pos[0]= cobra_pos[0][0]-BLOCK,cobra_pos[0][1] 
 elif direcao==K_DOWN: 
   cobra_pos[0]= cobra_pos[0][0],cobra_pos[0][1]+BLOCK 
 elif direcao==K_UP:
   cobra_pos[0]= cobra_pos[0][0],cobra_pos[0][1]-BLOCK 
     

 window.blit(texto,(420,30))
 pygame.display.update()  
 

   
