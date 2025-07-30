from random import randrange

import pygame, random
from pygame.examples.sprite_texture import sprite
from pygame.examples.video import backgrounds

pygame.init()       #iniciamos pygame

WIDTH = 800
HEIGHT = 600
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)     #definimos colores y medidads
y = 0
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT)) #pantalla donde se muestra el juego
clock = pygame.time.Clock()
background = pygame.image.load("assets/FOndodelJuego.png").convert()

def uploadBackground():
    global y
    y_relativa = y % background.get_rect().height
    screen.blit(background, (0, y_relativa - background.get_rect().height))
    if y_relativa < HEIGHT:
        screen.blit(background, (0, y_relativa))
    y += 5                                                  #fondo en movimiento, veritical

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif",size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)                  #texto del puntaje

def show_go_screen():
    screen.blit(background, [0, 0])                                      #dejo la pantalla con el fondo
    draw_text(screen, "Gracias por jugar", 27, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Presione tecla para salir", 17, WIDTH // 2, HEIGHT * 2/3)
    draw_text(screen, "Puntaje total", 22, WIDTH // 2,  450)
    draw_text(screen, str(score), 30, WIDTH // 2, 500)                #dibuja los textos al final

    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(70)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:  # pregunto si una tecla se ha soltado( presionar tecla para salir)
                waiting = False

class Car(pygame.sprite.Sprite):
    def  __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/auto3.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH  //  2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0                             # se define la clase con su imagen, velocidad(solo horizontal se mueve)

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
            self.rect.left = 0              #se actualiza el movimiento y con que teclas moverlo(flechas)

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(obstaculo_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-110,-40)
        self.speedy = 5
        self.speedx = random.randrange(-5,5)                #se define la clase con su lista imagen, velocidad igual q fondo y spawn random

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.bottom > WIDTH + 50 or self.rect.left < -50  or self.rect.right > WIDTH +  50:
            self.rect.y = random.randrange(-110,-40)
            self.speedy = 5
        if self.rect.bottom < 0:
            self.kill()
            global score               #si se sale de la pantalla se elimina y se suman puntos al score
            score += 1

obstaculo_images =[]
obstaculo_list = ["assets/TV1.png",
                  "assets/CAJA.png",
                  "assets/TV1.png",
                  "assets/POZO.png",
                  "assets/CONO1.png",
                  "assets/VALLA1.png",
                  "assets/TH5.png"]        #lista imagenes clase obstaculos

for img in obstaculo_list:
    obstaculo_images.append(pygame.image.load(img).convert())


all_sprites = pygame.sprite.Group()
obstaculo_list = pygame.sprite.Group()

car = Car()
all_sprites.add(car)

for i in range(6):            #lo q carga de obstaculos, cargamos 6 pq sino mucho(ganeralmente 8)
    obstaculo = Obstaculo()
    all_sprites.add(obstaculo)
    obstaculo_list.add(obstaculo)

#musicsound = pygame.mixer.Sound("assets/Musica.ogg")
#pygame.mixer.music.set_volume(0.1)
#pygame.mixer.music.play(loops=-1)


game_over = False
running  =  True
score = 0                      #se definen variables(para q desp puedan cambiar)
while running:
    if game_over:  # mover la logica del juego para dentro de game over
        running = False
        show_go_screen()  #se ensenia el fondo con los textos dados del game over
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                 # si ponemos TRUE  se cierra

    hits = pygame.sprite.spritecollide(car, obstaculo_list, False)
    if hits:
        #running = False
        game_over = True                #lo q pasa cuando colicion

    all_sprites.update()
    screen.blit(background, [0,0])
    uploadBackground()
    draw_text(screen, str(score), 25, WIDTH // 2, 10) #str convierte el numero en texto, ayuda a q no de error
    all_sprites.draw(screen)
    pygame.display.flip()
