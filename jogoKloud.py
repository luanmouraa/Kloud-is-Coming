# Nome: Luan Moura de Lima              TIA: 42117501
# Nome: Luiz Henrique Marcucci          TIA: 42119812
import pygame
from pygame.locals import *
from sys import exit

# Classe Julie
class Julie(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('C:/Users/DELL/Documents/KloudisComing/julie.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (256, 256))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocity_y = 0
        self.jumping = False

        # Retângulo menor em volta da Julie
        self.collision_rect = pygame.Rect(pos_x + 20, pos_y + 20, 50, 50)

    def update(self):
        if self.jumping:
            self.rect.y += self.velocity_y
            self.velocity_y += 0.8

            if self.rect.y >= ALTURA - 250:
                self.rect.y = ALTURA - 250
                self.jumping = False

        # Atualizar retângulo de colisão
        self.collision_rect.x = self.rect.x + 50
        self.collision_rect.y = self.rect.y + 100

# Classe Kloud
class Kloud(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('C:/Users/DELL/Documents/KloudisComing/nuvem.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (192, 192))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocity = 15

        # Retângulo em volta do Kloud
        self.collision_rect = pygame.Rect(pos_x + 20, pos_y + 20, 50, 50)

    def update(self):
        self.rect.x += self.velocity

        if self.rect.x > 900:
            self.velocity =- 15
        if self.rect.x < -100:
            self.velocity += 15

        # Atualizar retângulo de colisão
        self.collision_rect.x = self.rect.x + 50
        self.collision_rect.y = self.rect.y + 50

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Definição das constantes
LARGURA = 1000
ALTURA = 400
FPS = 30
VERMELHO = (255, 0, 0)
VIDAS = 3


# Configuração da tela
screen = pygame.display.set_mode((LARGURA, ALTURA), 0, 32)
clock = pygame.time.Clock()

#Carregando imagem
background = pygame.image.load('C:/Users/DELL/Documents/KloudisComing/paisagem.png').convert()
background = pygame.transform.scale(background, (LARGURA, ALTURA))
background_menu = pygame.image.load('C:/Users/DELL/Documents/KloudisComing/download.jpeg').convert()
background_menu = pygame.transform.scale(background_menu, (LARGURA, ALTURA))

# Fonte para exibir "Game Over"
fonte = pygame.font.Font(None, 40)

# Variáveis de controle do jogo
vidas_restantes = VIDAS
dificuldade = None
kloud_passed = False

def exibir_menu():
    screen.blit(background_menu, (0, 0))
    texto_titulo = fonte.render("KLOUD IS COMING", True, (255, 255, 255))
    texto_facil = fonte.render("1 - PLAY", True, (255, 255, 255))
    screen.blit(texto_titulo, (LARGURA // 2 - 150, ALTURA // 2 - 100))
    screen.blit(texto_facil, (LARGURA // 2 - 50, ALTURA // 2 - 50))
    pygame.display.update()

#Loop do menu
menu_ativo = True
while menu_ativo:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_1:
                dificuldade = "Play"
                menu_ativo = False
    exibir_menu()

# Criação dos grupos de sprites
all_sprites = pygame.sprite.Group()

# Função para exibir a pontuação e vidas na tela
def exibir_info():
    vidas_text = fonte.render(f"Vidas: {vidas_restantes}", True, (255, 25, 255))
    screen.blit(vidas_text, (LARGURA - 120, 10))


# Criação dos objetos
julie = Julie(LARGURA // 2 - 50, ALTURA - 250)
kloud = Kloud(0, ALTURA // 2)

# Adição dos objetos ao grupo de sprites
all_sprites.add(julie)
all_sprites.add(kloud)

# Carregar músicas
pygame.mixer.music.load('C:/Users/DELL/Documents/KloudisComing/jump_sound.wav')
game_over_sound = pygame.mixer.Sound('C:/Users/DELL/Documents/KloudisComing/game_over_sound.wav')

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE and not julie.jumping:
                julie.jumping = True
                julie.velocity_y = -15
                pygame.mixer.music.play()  # Tocar música de salto

    # Atualização dos sprites
    all_sprites.update()

#Verificar colisão
    if julie.collision_rect.colliderect(kloud.collision_rect):
        vidas_restantes -= 1
        kloud.rect.x = LARGURA + 100
        kloud.rect.y = ALTURA // 2

        if vidas_restantes <= 0:
            game_over = True
            pygame.mixer.music.stop()  # Parar música de salto
            game_over_sound.play()  # Tocar música de "Game Over"

    # Desenho na tela
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    exibir_info()

    # Exibir "Game Over"
    if game_over:
        game_over_text = fonte.render("Game Over", True, (255, 255, 255))
        screen.blit(game_over_text, (LARGURA // 2 - 70, ALTURA // 2))

    pygame.display.update()
    clock.tick(FPS)
