import pygame

pygame.init()

LARGURA = 640
ALTURA = 480

background_image_filename = 'C:\Users\DELL\Downloads\New Piskel.png'
sprite_image_filename = 'C:\Users\DELL\Downloads\New Piskel (1).png'

BRANCO = (255,255,255)
tela = pygame.display.set_mode((LARGURA, ALTURA))
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

pygame.display.set_caprtion('Kloud is Coming')

while True:
    for event in pygame.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

            
    screen.blit(background,(0,0))
    #screen.blit(sprite, (position.x, position.y))
    pygame.display.update()
