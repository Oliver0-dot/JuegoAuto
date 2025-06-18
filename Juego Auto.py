import pygame, random
from pygame.examples.sprite_texture import sprite
from pygame.examples.video import backgrounds

pygame.init()

WIDTH = 800
HEIGHT = 600
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)     #definimos colores y medidads

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
screen.fill (BLACK)

class Car(pygame.sprite.Sprite):
    def  __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/auto 2.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH  //  2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate [pygame.K_LEFT]:
            self.speed_x = -5
        if keystate [pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
car = Car()
all_sprites.add(car)


running  =  True
while running:
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                 # si ponemos TRUE  se cierra

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

#mejorar imagen auto(color fondo) y agrandar un poco
#linea background a bajo de screen
#mejorar imagen rueda(fondo y png, assets)
