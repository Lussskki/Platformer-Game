import pygame

class Gamepad:
    def __init__(self, dead_zone=0.1):
        pygame.joystick.init()
        self.joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        self.dead_zone = dead_zone

        for joystick in self.joysticks:
            joystick.init()
            print(f"Joystick initialized: {joystick.get_name()}")

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Joystick {event.joy} button {event.button} pressed.")
            if event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} moved to {event.value:.2f}")
                if event.axis == 4:
                    print("L2 Trigger moved")
                elif event.axis == 5:
                    print("R2 Trigger moved")
            if event.type == pygame.QUIT:
                return True
        return False

    def get_movement(self):
        left_stick_x, left_stick_y = 0, 0
        for joystick in self.joysticks:
            left_stick_x = joystick.get_axis(0)
            left_stick_y = joystick.get_axis(1)

            if abs(left_stick_x) < self.dead_zone:
                left_stick_x = 0
            if abs(left_stick_y) < self.dead_zone:
                left_stick_y = 0

        return left_stick_x, left_stick_y
    def is_jumping(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_SPACE]
