import pygame
from gamepad import Gamepad
from rectangle import Rectangle

pygame.init()

color_white = (255, 255, 255)
rect_color_red = (255, 0, 0)

game_surface = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Surface')

rect = Rectangle(500, 400, 30, 30, rect_color_red, 2, 700, 500)

gamepad = Gamepad(dead_zone=0.1)

exit = False

while not exit:
    game_surface.fill(color_white)

    # Process gamepad events
    exit = gamepad.process_events()

    # Get joystick movement
    left_stick_x, left_stick_y = gamepad.get_movement()

    # Update rectangle position
    rect.update_position(left_stick_x, left_stick_y)

    # Draw rectangle
    rect.draw(game_surface)

    pygame.display.update()
