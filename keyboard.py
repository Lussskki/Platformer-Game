import pygame

class Keyboard:
    def __init__(self, speed = 0.1):
        self.keys = pygame.key.get_pressed()
        self.speed = speed  
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False
    
    def get_movement(self):
        keys = pygame.key.get_pressed()
        key_x = 0
        key_y = 0
        
        if keys[pygame.K_LEFT]:
            key_x = -1
        if keys[pygame.K_RIGHT]:
            key_x = 1
        if keys[pygame.K_UP]:
            key_y = -1
        if keys[pygame.K_DOWN]:
            key_y = 1
        # WSAD 
        if keys[pygame.K_a]:
            key_x = -1
        if keys[pygame.K_d]:
            key_x = 1
        if keys[pygame.K_w]:
            key_y = -1
        if keys[pygame.K_s]:
            key_y = 1            
            
        
        return key_x, key_y
