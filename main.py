import pygame 

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) 
             for x in range(pygame.joystick.get_count())]

# Initialize joystick
for joystick in joysticks:
    joystick.init()
    print(f"Joystick initialized: {joystick.get_name()}")


# Colors
color_white = (255,255,255) 
rect_color_red = (255, 0, 0) 
pipe_color = (0, 0, 255)

# Create surface
game_surface = pygame.display.set_mode((700, 500))

# Title
pygame.display.set_caption('Surface')

# Rectangle properties
rect_x, rect_y = 500, 400 
rect_width, rect_height = 30, 30
rect_speed = 2

# Pipe properties
pipe_width, pipe_height = 20, 8
pipe_x, pipe_y = rect_x + rect_width, rect_y + rect_height
pipe_speed =2

# Dead-zone
dead_zone = 0.1

exit = False

while not exit:
    game_surface.fill(color_white)

    for event in pygame.event.get():
        # Gempad 
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Joystick {event.joy} button {event.button} pressed.")
        # Gempad-Axis
        if event.type == pygame.JOYAXISMOTION:
                
                print(f"Axis {event.axis} moved to {event.value:.2f}")
                if event.axis == 4:  # L2 Trigger
                    print("L2 Trigger moved")
                elif event.axis == 5:  # R2 Trigger
                    print("R2 Trigger moved")            
    # Movement of rect-axis
    for joystick in joysticks:
        left_stick_x = joystick.get_axis(0)  
        left_stick_y = joystick.get_axis(1)  

        right_stick_x = joystick.get_axis(2)
        right_stick_y = joystick.get_axis(3)

        # Deadzone
        if abs(left_stick_x) < dead_zone:
            left_stick_x = 0
        if abs(left_stick_y) < dead_zone:
            left_stick_y = 0

        if abs(right_stick_x) < dead_zone:
            right_stick_x = 0
        if abs(right_stick_y) < dead_zone:
            right_stick_y = 0    
        # Update rectangle position
        rect_x += int(left_stick_x * rect_speed)
        rect_y += int(left_stick_y * rect_speed)
        

        # Keep the rectangle within screen boundaries
        rect_x = max(0, min(700 - rect_width, rect_x))
        rect_y = max(0, min(500 - rect_height, rect_y))
        # Bullet-pipe
        pipe_x = rect_x + rect_width
        pipe_y = rect_y + rect_height

        # Moving with right stick
        pipe_x += int(right_stick_x * pipe_speed)
        pipe_y += int(right_stick_y * pipe_speed)

        # Keep in boundaries
        pipe_x = max(0, min(700 - pipe_width, pipe_x))
        pipe_y = max(rect_y, min(rect_y + pipe_height - rect_height, pipe_y))


        if event.type == pygame.QUIT:
            exit = True
    pygame.draw.rect(game_surface, rect_color_red, 
                     pygame.Rect(rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(game_surface, pipe_color, 
                     pygame.Rect(pipe_x, pipe_y, pipe_width, pipe_height))  
    pygame.display.update()        
