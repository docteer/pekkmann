import pygame
pygame.init()

screenHeight = 400
screenWidth = 400

win = pygame.display.set_mode((screenHeight, screenWidth))
pygame.display.set_caption("Pek Mann")



x = 100
y = 110
width = 10
height = 10
vel = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x < screenWidth and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width:
        x += vel
    if keys[pygame.K_UP] and y < screenHeight and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenHeight - height:
        y += vel

        
    win.fill((0,0,0))        
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
pygame.quit()
