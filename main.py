import pygame
from gamepad import Gamepad
from keyboard import Keyboard
from rectangle import Rectangle

pygame.init()

color_white = (255, 255, 255)
rect_color_red = (255, 0, 0)

game_surface = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Game')

rect = Rectangle(500, 400, 30, 30, rect_color_red, 2, 700, 500)

gamepad = Gamepad(dead_zone=0.1)
keyboard = Keyboard()

exit = False

while not exit:
    game_surface.fill(color_white)
    exit = gamepad.process_events() or keyboard.process_events()
    
    left_stick_x, left_stick_y = gamepad.get_movement()
    key_x, key_y = keyboard.get_movement()
    
    rect.update_position(left_stick_x + key_x, left_stick_y + key_y)
    rect.draw(game_surface)

    pygame.display.update()
