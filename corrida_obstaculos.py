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

#criar classes-=------------------
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
    
    if deslocamentoPersonagem > 11:  #vai pra baixo(quanto maior o numero, maior a velocidade da queda)
      deslocamentoPersonagem = 11
    elif deslocamentoPersonagem < 0:
      deslocamentoPersonagem -= 10 #pra cima

    self.posy +=  deslocamentoPersonagem

    if self.imagem.index(self.imagem) == 0:# papai noel deitado
      





  



     
   



