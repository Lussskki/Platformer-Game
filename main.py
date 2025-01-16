import pygame 

pygame.init()

color = (255,255,255) 
rect_color_red = (255, 0, 0) 

# Create canvas
canvas = pygame.display.set_mode((500, 500))

# Title
pygame.display.set_caption('Game')
exit = False

while not exit:
    canvas.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.draw.rect(canvas, rect_color_red, 
                     pygame.Rect(30,30,60,60)) 
    pygame.display.update()        
