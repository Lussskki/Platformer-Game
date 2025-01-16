import pygame

class Rectangle:
    def __init__(self, x, y, width, height, color, speed, screen_width, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update_position(self, dx, dy):
        self.x += int(dx * self.speed)
        self.y += int(dy * self.speed)

        # Keep rectangle within screen boundaries
        self.x = max(0, min(self.screen_width - self.width, self.x))
        self.y = max(0, min(self.screen_height - self.height, self.y))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
                         pygame.Rect(self.x, self.y, self.width, self.height))
