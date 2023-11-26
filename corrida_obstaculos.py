import pygame, os, random, time

ob1 = 0 #variavel controla obstaculos
ob2 = 0 #variavel controla obstaculos
larguraJanela = 640
alturaJanela = 400

#fonte------------------------------
pygame.font.init()
fontePontuacao = pygame.font.SysFont('arial',25, bold=True, italic=True)

#importacao da imagens-----------------
imagemPersonagem = [
  pygame.image.load(os.path.join('imagens', 'papainoel.png')),
  pygame.image.load(os.path.join('imagens', 'papainoelDeitado.png'))
]

imagemObstaculos = [
  pygame.image.load(os.path.join('imagens','obs1.png')),
  pygame.image.load(os.path.join('imagens','obs2.png'))
]

#pygame.transform.scale2x(dobra o tamanho da imagem)
imagemChao = pygame.transform.scale2x( pygame.image.load(os.path.join('imagens','chao.))png')))
imagemFundo = pygame.image.load(os.path.join('imagens','bg.png'))
imagemFundoPontos = pygame.image.load(os.path.join('imagens','fundoPontos.png'))

#criar classes-=----------------------------------------------------
class PapaiNoel:
  imagens = imagemPersonagem #lista imagemPersonagem
  noChao = False  #true ta no cao e false ta pulando

  def __init__(self, posx, posy):
     self.posx = posx
     self.posy = posy
     self.velocidadePersonagem = 0  #controla a velocidade do papai noel
     self.tempoJogo = 0
     self.imagem = self.imagens(0)

  def pular(self):
     if self.posy >= 240: #pular
      self.velocidadePersonagem = -11 #para baixo ->positivo, para cima -> negativo
      self.tempoJogo = 0

  
  def movimento(self):
    self.tempoJogo += 1
    aceleracao = 3
    deslocamentoPersonagem = self.velocidadePersonagem * self.tempoJogo \
                                                + (self.tempoJogo**2)/2
    
    if deslocamentoPersonagem > 11: #pra baixo( maior o num, maior a veloc da queda)
      deslocamentoPersonagem = 11
    elif deslocamentoPersonagem < 0:
      deslocamentoPersonagem -= 10 #pra cima(maior o num,sera ,maior o salto)

    self.posy +=  deslocamentoPersonagem

    if self.imagens.index(self.imagem) == 0:#se index fo (0) papai noel em pé
      if self.posy > 240:
        self.posy = 240
        self.noChao = True
    elif self.imagens.index(self.imagem) == 1:
      if self.posy > 260:
        self.posy = 260
        self.noChao = True
  

  def desenhar_personagem(self, janela):
    centroImagem = self.imagem.get_rect(topleft=(self.posx, self.posy)).center
    envoltorio = self.imagem.get_rect(center = centroImagem)
    janela.blit(self.imagem, envoltorio.topleft)

  def superficiePersonagem(self):
    return pygame.mask.from_surface(self.imagem)

#finalizando primeira classe==============================================
    
class Obstaculo:
  velocidadeObstaculo = 10
  proxObstaculo = 0


  def __init__(self, posx):
    self.posx = posx
    self.alturaObstaculo = 0
    self.posicaoObstaculoBaixo = 0
    self.posicaoObstaculoAlto = 0
    self.obstaculoCima = pygame.transform.flip(imagemObstaculos[0], False, True)#flip gira a imagem
    self.obstaculoBaixo = imagemObstaculos[1]
    self.passouObstaculo = False
    self.escolher_obstaculo()
#Inicio funcao que escolhe o proximo obstaculo do jogo-------------------------------------------
  def escolher_obstaculo(self):
    global ob1, ob2
    self.proxObstaculo =random.randint(1,2)
    if self.proxObstaculo == 1:
      ob2 = 0
      ob1 += 1
      if ob1 <= 3:
        self.alturaObstaculo = 260
        self.posicaoObstaculoBaixo = self.alturaObstaculo
      else:
        self.alturaObstaculo = 55
        self.posicaoObstaculoAlto = self.alturaObstaculo - self.obstaculoBaixo.get_height()
        self.proxObstaculo = 2
        ob2 += 1
        ob1 = 0
    elif self.proxObstaculo == 2:
      ob1 = 0
      ob2 += 1
      if ob2 <= 3:
        self.alturaObstaculo = 55
        self.posicaoObstaculoAlto = self.alturaObstaculo - self.obstaculoBaixo.get_height()
      else:
        self.alturaObstaculo = 260
        self.posicaoObstaculoBaixo = self.alturaObstaculo 
        self.proxObstaculo = 1
        ob1 += 1
        ob2 = 0
# funcao de movimento dos obstaculos-------------------------------------------
  def movimento(self):
    self.posx -= self.velocidadeObstaculo

# funcao desenhar obstaculos-------------------------------------------
  def desenharObstaculo(self, janela):
    if self.proxObstaculo == 1:
      janela.blit(self.obstaculoBaixo, (self.posx, self.posicaoObstaculoBaixo))#desenhar janela
    elif self.proxObstaculo == 2:
      janela.blit(self.obstaculoBaixo, (self.posx, self.posicaoObstaculoAlto))#desenhar janela
      























  



     
   



