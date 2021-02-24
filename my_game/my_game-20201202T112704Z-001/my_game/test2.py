import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = [[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,0,0,0,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,3,0,3,0,0,2,0,0,0,3,3,3,3,3,3,3],
        [3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,0,0,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,0,0,0,3,0,3,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3],
        [3,3,3,3,0,3,0,0,0,0,0,2,0,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,0,0,0,0,0,0,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,0,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,0,0,0,3,3,0,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,0,0,0,3,0,0,0,3,3,3,3],
        [3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3],
        [3,3,3,3,3,3,3,3,0,0,0,3,0,3,0,3,0,3,3,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        ]


# Set row 0, cell 0 to one. (Remember rows and
# column numbers start at zero.)
column = 3
row = 9

grid[column][row] = 1 # 1 - Player




# Draw the grid
def draw(row, column):
    for row in range(20):
        for column in range(20):
            color = WHITE
            if grid[row][column] == 1:
                color = BLUE
            elif grid[row][column] == 3:
                color = RED
            elif grid[row][column] == 2:
                color = GREEN  
            pygame.draw.rect(screen,
                             color,
                             [ WIDTH * column , HEIGHT * row,
                              WIDTH, HEIGHT])





# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
            print(  "Grid coordinates: ", row, column)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if grid[row][column-1] == 0:
                grid[row][column] = 0
                draw(row, column)
                column -= 1
                grid[row][column] = 1
                draw(row, column)
                print(  "Grid coordinates: ", row, column)
            elif grid[row][column-1] == 2 and grid[row][column-2] == 0:
                grid[row][column-1] = 0
                grid[row][column] = 0
                draw(row, column)
                column -= 1
                grid[row][column] = 1
                grid[row][column-1] = 2
                print(  "Grid coordinates: ", row, column)

        if keys[pygame.K_RIGHT]:
            if grid[row][column+1] == 0:
                grid[row][column] = 0
                draw(row, column)
                column += 1
                grid[row][column] = 1
                draw(row, column)
                print(  "Grid coordinates: ", row, column)
            elif grid[row][column+1] == 2 and grid[row][column+2] == 0:
                grid[row][column+1] = 0
                grid[row][column] = 0
                draw(row, column)
                column += 1
                grid[row][column] = 1
                grid[row][column+1] = 2
                print(  "Grid coordinates: ", row, column)


        if keys[pygame.K_UP]:
            if grid[row-1][column] == 0:
                grid[row][column] = 0
                draw(row, column)
                row -= 1
                grid[row][column] = 1
                draw(row, column)
                print(  "Grid coordinates: ", row, column)
            elif grid[row-1][column] == 2 and grid[row-2][column] == 0:
                grid[row-1][column] = 0
                grid[row][column] = 0
                draw(row, column)
                row -= 1
                grid[row][column] = 1
                grid[row-1][column] = 2
                print(  "Grid coordinates: ", row, column)

        if keys[pygame.K_DOWN]:
            if grid[row+1][column] == 0:
                grid[row][column] = 0
                draw(row, column)
                row += 1
                grid[row][column] = 1
                draw(row, column)
                print(  "Grid coordinates: ", row, column)
            elif grid[row+1][column] == 2 and grid[row+2][column] == 0:
                grid[row+1][column] = 0
                grid[row][column] = 0
                draw(row, column)
                row += 1
                grid[row][column] = 1
                grid[row+1][column] = 2
                print(  "Grid coordinates: ", row, column)
            

    
 
    # Set the screen background
    screen.fill(BLACK)
 
    draw(row, column)
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()