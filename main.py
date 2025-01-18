import pygame
from gamepad import Gamepad
from keyboard import Keyboard
from rectangle import Rectangle

pygame.init()

# Colors
color_white_sky = (0, 0, 255)
rect_color_red = (255, 0, 0)
way_color_green = (0, 255, 0)

# Game surface setup
game_surface = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Game')

# Rectangles for the player and platform
rect = Rectangle(50, 250, 50, 50, rect_color_red, 2, 700, 500)
way = Rectangle(50, 250, 300, 30, way_color_green, 2, 700, 500)

# Gravity variables
gravity = 0.3  # The force pulling the rectangle down
velocity_y = 0
on_ground = False

# FPS
fps = pygame.time.Clock()

# Input handlers
gamepad = Gamepad(dead_zone=0.1)
keyboard = Keyboard()

exit = False

while not exit:
    # Game surface, keyboard and gamepad events
    game_surface.fill(color_white_sky)
    exit = gamepad.process_events() or keyboard.process_events()

    # Movement of rect (horizontal)
    left_stick_x, left_stick_y = gamepad.get_movement()
    key_x, key_y = keyboard.get_movement()

    # Apply gravity (vertical movement)
    if not on_ground:
        velocity_y += gravity  # Increase velocity due to gravity
    rect.y += velocity_y

    # Collision with platform (way)
    if rect.y + rect.height >= way.y and rect.y < way.y + way.height and \
            rect.x + rect.width > way.x and rect.x < way.x + way.width:
        rect.y = way.y - rect.height  # Reset position on top of the platform
        velocity_y = 0
        on_ground = True
    else:
        on_ground = False

    # Collision with ground
    if rect.y + rect.height >= 500:  # Ground level
        rect.y = 500 - rect.height
        velocity_y = 0
        on_ground = True

    # Jumping (only when on the ground)
    if (keyboard.is_jumping() or gamepad.is_jumping()) and on_ground:
        velocity_y = -10  # Jump force
        on_ground = False

    # Draw rectangles on surface
    rect.update_position(left_stick_x + key_x, 0)  # Only horizontal movement
    rect.draw(game_surface)
    way.draw(game_surface)

    # Update FPS and display
    fps.tick(60)
    pygame.display.update()
