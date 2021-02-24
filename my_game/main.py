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

    def player_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel            
        elif keys[pygame.K_RIGHT]:
            self.x += self.vel            
        elif keys[pygame.K_UP]:
            self.y -= self.vel            
        elif keys[pygame.K_DOWN]:        
            self.y += self.vel

    def player_draw(self):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.display.update() 
            



class box(object):
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
        self.width1 = 20
        self.height1 = 20
        self.vel1 = 10

    def box_move(self, player):
        keys = pygame.key.get_pressed()

        if (player.x  == self.x1 + self.width1) and (player.y == self.y1):
            self.x1 -= self.vel1
            
        if (player.x  == self.x1 ) and (player.y == self.y1):
            self.x1 += self.vel1
        
        if (player.x  == self.x1 + 10) and (player.y  == self.y1 + self.height1):
            self.y1 -= self.vel1
        
        if (player.x + 10 == self.x1 + 10) and (player.y + player.height  == self.y1):
            self.y1 += self.vel1

    def box_draw(self):
        if (self.x1 == 200) and (self.y1 == 200):
            pygame.draw.rect(win, (0, 0, 128), (self.x1, self.y1, self.width1, self.height1))
        else:
            pygame.draw.rect(win, (0, 0, 255), (self.x1, self.y1, self.width1, self.height1))

        pygame.display.update()            



box1 = box(80, 80)
box2 = box(120, 120)
box3 = box(280, 280)
man = player(0, 0)
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    man.player_move()
    box1.box_move(man)
    box2.box_move(man)
    box3.box_move(man)

    win.fill((0,0,0)) 
       

    man.player_draw()    
    box1.box_draw()
    box2.box_draw()
    box3.box_draw()
       

    pygame.draw.circle(win, (0, 255, 0), (200, 200), 3)
    pygame.display.update()       