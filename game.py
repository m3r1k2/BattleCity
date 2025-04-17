import pygame
from mechanics import victory, reset_score, increase, update_block_sprites
from entities.blocks import Tank
from entities.blocks import Block
from entities.blocks import Obj
from mechanics import move
from projectiles import Bullet
from mechanics import hit_brick
from mechanics import handle_enemy_respawn

from entities.entities import EnemyTank
pygame.init()

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("3")
clock = pygame.time.Clock()

target = pygame.image.load("target.png")
class Scene:
    def __init__(self, game):
        self.game = game
    def h_events(self, events):
        pass
    def update(self, events):
        pass
    def render(self,screen):
        pass
class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
    def h_events(self, events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.game.change_scene(MainScene(self.game))
    def render(self,screen):
        screen.fill((250,45,86))
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("Press to start", True, (255,255, 255))
        screen.blit(text, (100,100))


class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.score = 0

        self.bullets = pygame.sprite.Group()
        self.score = reset_score()
        self.walls = Block().setupWalls("brick.jpg")
        self.bush = Block().setupLeaves("laeves2.png")
        self.rocks = Block().setupStone("stone.png")
        self.hedge = Block().setupFence("fence.png")
        tank = Tank()
        self.obj = Obj()
        self.target = self.obj.setTarget("target.png")
        self.block_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_spawn_points = [(50, 50), (650, 50), (350, 150)]

        handle_enemy_respawn(self.enemies, "enemy.png", self.enemy_spawn_points)
        update_block_sprites(self.walls, self.rocks, self.block_sprites, self.hedge)
        self.hero_sprites, self.enemy_sprites = tank.setupPlayers("wmremove-transformed.png", "enemy.png")

        self.enemy_sprites.add(self.enemies)

    def h_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    for player in self.hero_sprites:
                        player.fire(self.bullets)


    def update(self, events):
        self.block_sprites.update()
        self.enemy_sprites.update(self.bullets, self.block_sprites)
        hit_brick(self.bullets, self.walls, self.rocks, self.enemy_sprites, self.hero_sprites, self.hedge, self.enemy_spawn_points, self)
        handle_enemy_respawn(self.enemies, "enemy.png", self.enemy_spawn_points)
        self.enemy_sprites.add(self.enemies)
        self.bullets.update()
        move(self.hero_sprites, self.block_sprites)
        self.hero_sprites.update()
        if victory(self.score):
            self.game.change_scene(WinScene(self.game, self.score))
            return
        if len(self.hero_sprites) == 0:
            self.game.change_scene(LoseScene(self.game, self.score))
            return




    def render(self,screen):
        screen = pygame.display.get_surface()
        screen.fill((0,0,0))
        font = pygame.font.SysFont('Arial', 30)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (570,50))
        self.walls.draw(screen)
        self.hero_sprites.draw(screen)
        self.enemy_sprites.draw(screen)
        self.hedge.draw(screen)
        self.rocks.draw(screen)
        self.bullets.draw(screen)
        screen.blit(self.target.image, self.target.rect)
        self.bush.draw(screen)

class WinScene(Scene):
    def __init__(self, game, score):
        super().__init__(game)
        self.score = score

    def h_events(self, events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.game.change_scene(MenuScene(self.game))

    def render(self,screen):
        screen.fill((0,123,0))
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(f"You win, with score: {self.score}", True, (255,255, 255))
        text1 = font.render("Press button to go to menu", True, (255,255, 255))
        screen.blit(text, (225,125))
        screen.blit(text1, (225, 325))

class LoseScene(Scene):
    def __init__(self, game, score):
        super().__init__(game)
        self.score = score


    def h_events(self, events):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.game.change_scene(MainScene(self.game))
    def render(self,screen):
        screen.fill((155,123,0))
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(f"You lose, your score: {self.score}", True, (255, 255, 255))
        text1 = font.render("Press button to restart game", True, (255, 255, 255))
        screen.blit(text, (250,150))
        screen.blit(text1, (250,325))

class Game():
    def __init__(self):
        self.scene = MenuScene(self)
    def change_scene(self, new_scene):
        self.scene = new_scene
    def run(self):

        game = True
        while game:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    game = False
            self.scene.h_events(events)
            self.scene.update(events)
            self.scene.render(win)
            pygame.display.update()
            clock.tick(60)
game = Game()
game.run()
pygame.quit()