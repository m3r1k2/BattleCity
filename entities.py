import random

import pygame
from time import *
from core.projectiles import Bullet
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image_path=None):
        super().__init__()
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.mask = pygame.mask.from_surface(self.image)
            self.image = pygame.transform.scale(self.image, (30, 30))
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

class Leaves(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, role_image_path):
        super().__init__()
        self.image = pygame.image.load(role_image_path).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image.set_alpha(200)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
class Stone(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, role_image_path):
        super().__init__()

        self.image = pygame.image.load(role_image_path).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
class Hedge(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, role_image_path):
        super().__init__()

        self.image = pygame.image.load(role_image_path).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, role_image_path):
        self.is_enemy = False
        pygame.sprite.Sprite.__init__(self)
        self.last_direction = (0, -1)
        self.base_image = pygame.image.load(role_image_path).convert_alpha()
        self.image = self.base_image.copy()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.dx = 0
        self.dy = 0
        self.base_speed = [30, 30]
        self.speed = [0, 0]
        self.is_move = False

    def fire(self, bullets_gr):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.centery, 25, 30, 15, self.last_direction, owner=self)
        bullets_gr.add(bullet)
    '''Изменить направление скорости'''

    def changeSpeed(self, direction):
        self.last_direction = direction
        self.dx, self.dy = direction
        if direction[0] < 0:
            self.rotation_angle = 90
            self.image = pygame.transform.rotate(self.base_image, self.rotation_angle)

        elif direction[0] > 0:
            self.rotation_angle = -90
            self.image = pygame.transform.rotate(self.base_image, self.rotation_angle)

        elif direction[1] < 0:
            self.rotation_angle = 0
            self.image = pygame.transform.rotate(self.base_image, self.rotation_angle)

        elif direction[1] > 0:
            self.rotation_angle = 180
            self.image = pygame.transform.rotate(self.base_image, self.rotation_angle)

        self.image = pygame.transform.scale(self.image, (50, 50))
        self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
        self.base_speed = [2, 2]
        return self.base_speed

class EnemyTank(Player):
    def __init__(self, x, y, role_image_path):
        super().__init__(x, y, role_image_path)
        self.is_enemy = True
        self.base_speed = [1, 1]
        self.speed = [0, 0]


        self.base_image = pygame.image.load(role_image_path).convert_alpha()
        self.image = self.base_image.copy()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.move_timer = 0
        self.move_interval = 80
        self.shoot_timer = 0
        self.shoot_interval = 100
        self.dx = 0
        self.dy = 0


    def update(self, bullets_gr, block_sprites):

        self.move_timer += 1
        if self.move_timer >= self.move_interval:
            self.move_timer = 0
            direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            self.changeSpeed(direction)

        future_rect = self.rect.move(self.speed[0], self.speed[1])
        collision = False
        for block in block_sprites:
            if block.rect.colliderect(future_rect):
                collision = True
                break

        if not collision:
            self.rect = future_rect

        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.fire(bullets_gr)
            self.shoot_timer = 0




class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path=None):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y




