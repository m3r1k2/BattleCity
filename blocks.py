import pygame
from entities.entities import Brick
from entities.entities import Player
from entities.entities import Target
from entities.entities import Leaves
from entities.entities import Stone
from entities.entities import EnemyTank
from entities.entities import Hedge
class Block:
    def __init__(self):
        pass

    def setupWalls(self, image_path):
        self.wall_sprites = pygame.sprite.Group()
        self.brick_sprites = pygame.sprite.Group()

        wall_positions = [

            (240, 60), (270, 60), (300, 60), (330, 60), (360, 60), (390, 60), (420, 60), (450, 60),


            (520, 90), (520, 120), (520, 150),


            (180, 90), (180, 120), (180, 150),


            (330, 480), (360, 480), (390, 480),

            (120, 540), (150, 540), (180, 540),
            (120, 570), (180, 570),
            (150, 600),

            (50, 640), (20, 640), (80, 640),
            (50, 670), (20, 670), (80, 670),



            (510, 540), (540, 540), (570, 540),
            (510, 570), (570, 570),
            (540, 600)




        ]

        for x, y in wall_positions:
            wall = Brick(x, y, 30, 30, image_path=image_path)
            self.wall_sprites.add(wall)
            self.brick_sprites.add(wall)

        return self.wall_sprites

    def setupStone(self, role_image_path):
        self.stones = pygame.sprite.Group()

        stones_position = [

            (180, 210), (210, 210),
            (180, 240), (210, 240),

            (510, 210), (540, 210),
            (510, 240), (540, 240),

            (290, 670), (320, 670), (350, 670),(380, 670),(410, 670),

            (360, 330), (330, 330), (390, 330),
            (360, 360),

            (25, 390), (25, 420), (25, 360),(25,330),


            (730, 420), (730, 390), (730, 360),(730, 330)



        ]

        for x, y in stones_position:
            rock = Stone(x, y, 30, 40, role_image_path)
            self.stones.add(rock)

        return self.stones

    def setupLeaves(self, role_image_path):
        self.leaves = pygame.sprite.Group()

        leaves_position = [
            # Камуфляж на флангах
            (150, 270), (150, 300), (150, 330),
            (180, 300),

            (600, 270), (600, 300), (600, 330),
            (570, 300),

            # Трохи в центрі
            (390, 390), (330, 390),
            (360, 420),


            (20, 700), (50, 700), (70, 700),
            (20, 730), (50, 730),

            (725, 700), (695, 700), (665, 700),
            (725, 730), (695, 730),
        ]

        for x, y in leaves_position:
            grass = Leaves(x, y, 30, 40, role_image_path)
            self.leaves.add(grass)

        return self.leaves

    def setupFence(self, role_image_path):
        self.fences = pygame.sprite.Group()
        fence_position = []


        for x in range(0, 800, 30):
            fence_position.append((x, 0))


        for x in range(0, 800, 30):
            fence_position.append((x, 770))


        for y in range(0, 800, 30):
            fence_position.append((0, y))


        for y in range(0, 800, 30):
            fence_position.append((770, y))

        for x, y in fence_position:
            fence = Hedge(x, y, 30, 40, role_image_path)
            self.fences.add(fence)
        return self.fences
class Tank():
    def __init__(self):
        pass

    def setupPlayers(self, hero_image_path, enemy_image_path):
        self.hero_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        hero = Player(423, 600, hero_image_path)
        enemy = EnemyTank(50, 50, enemy_image_path)
        enemy1 = EnemyTank(650, 50, enemy_image_path)

        self.hero_sprites.add(hero)
        self.enemy_sprites.add(enemy, enemy1)


        return self.hero_sprites, self.enemy_sprites



class Obj():
    def __init__(self):
        self.target = None
    def setTarget(self, image_path):
        self.target = Target(50, 700, image_path)
        return self.target

