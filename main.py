import pygame
from gamepad import Gamepad
from keyboard import Keyboard
from rectangle import Rectangle

pygame.init()

color_white_sky = (0, 0, 255)
rect_color_red = (255, 0, 0)

game_surface = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Game')

rect = Rectangle(500, 400, 50, 50, rect_color_red, 2, 700, 500)
way = Rectangle(50, 250, 300, 30, 'green',2, 700,500 )

# FPS
fps=pygame.time.Clock()

gamepad = Gamepad(dead_zone=0.1)
keyboard = Keyboard()

exit = False

while not exit:
    fps.tick(60)
    # Game surface, keyboard and gamepad events
    game_surface.fill(color_white_sky)
    exit = gamepad.process_events() or keyboard.process_events()
    
    # Movement of rect 
    left_stick_x, left_stick_y = gamepad.get_movement()
    key_x, key_y = keyboard.get_movement()
    
    # Draw on surface
    rect.update_position(left_stick_x + key_x, left_stick_y + key_y)
    rect.draw(game_surface)
    way.draw(game_surface)

    pygame.display.update()
