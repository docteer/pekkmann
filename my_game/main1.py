import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First Game")


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.vel = 10 

    def player_draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.display.update()



x1 = 80
y1 = 80
width1 = 20
height1 = 20
vel1 = 10


man = player(0, 0)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel            
    elif keys[pygame.K_RIGHT]:
        x += vel            
    elif keys[pygame.K_UP]:
        y -= vel            
    elif keys[pygame.K_DOWN]:        
        y += vel

    win.fill((0,0,0))

    pygame.draw.rect(win, (255, 0, 0), (man.x, man.y, man.width, man.height))
    pygame.draw.rect(win, (0, 0, 255), (x1, y1, width1, height1))
    pygame.display.update()