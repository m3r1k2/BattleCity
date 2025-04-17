import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,image_path, x, y, width, height, speed, direction, owner=None):
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10
        self.dx, self.dy = direction
        self.direction = direction
        self.owner = owner
        if direction[0] < 0:
            self.rotation_angle = 0
            self.image = pygame.transform.rotate(self.image, self.rotation_angle)
        elif direction[0] > 0:
            self.rotation_angle = 180
            self.image = pygame.transform.rotate(self.image, self.rotation_angle)
        elif direction[1] < 0:
            self.rotation_angle = -90
            self.image = pygame.transform.rotate(self.image, self.rotation_angle)
        elif direction[1] > 0:
            self.rotation_angle = 90
            self.image = pygame.transform.rotate(self.image, self.rotation_angle)
    def update(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

