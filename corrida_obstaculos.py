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


