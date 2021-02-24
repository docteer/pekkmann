import pygame
import random


# Параметри ігрового вікна
WIDTH = 400
HEIGHT = 400
FPS = 60

# Додаємо кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Ініціалізація гри і створення дисплея
pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 1

    def update(self):
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if keystate[pygame.K_RIGHT]:
            self.rect.x += self.vel
        if keystate[pygame.K_UP]:
            self.rect.y -= self.vel
        if keystate[pygame.K_DOWN]:
            self.rect.y += self.vel
        

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Box(pygame.sprite.Sprite):
    def __init__(self, box_x, box_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = box_x
        self.rect.y = box_y
        self.box_vel = 1

    def update(self, Player):
        
        if (Player.rect.topleft == self.rect.topright) and (Player.rect.bottomleft == self.rect.bottomright):
            self.rect.x -= self.box_vel
        
        if (Player.rect.topright== self.rect.topleft) and (Player.rect.bottomright == self.rect.bottomleft):
            self.rect.x += self.box_vel

        if (Player.rect.topright== self.rect.bottomright) and (Player.rect.topleft == self.rect.bottomleft):
            self.rect.y -= self.box_vel

        if (Player.rect.bottomright== self.rect.topright) and (Player.rect.bottomleft == self.rect.topleft):
            self.rect.y += self.box_vel    


        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


           
        




               
all_sprites = pygame.sprite.Group()
man = Player(0, 0)

boxs = pygame.sprite.Group()
box1 = Box(100, 100)
box2 = Box(140, 140)



all_sprites.add(man)
boxs.add(box1, box2)

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            
    all_sprites.update()
    boxs.update(man)


    
    win.fill(BLACK)
    all_sprites.draw(win)
    boxs.draw(win)
    
    pygame.display.flip()

pygame.quit()   