import random

import pygame
from entities.blocks import *
from entities.entities import EnemyTank
from entities.entities import Player

def victory(score):
    return score == 700
def reset_score():
    return 0
def increase(score, amount=100):
    return score + amount

def update_block_sprites(walls, rocks, group, hedge):
    group.empty()
    group.add(walls)
    group.add(rocks)
    group.add(hedge)

enemy_respawns = []

def handle_enemy_respawn(enemies_group, enemy_image_path, spawn_points):
    current_time = pygame.time.get_ticks()
    for respawn in enemy_respawns[:]:
        if current_time - respawn["time"] >= 5000:
            new_enemy = EnemyTank(respawn["pos"][0], respawn["pos"][1], enemy_image_path)
            enemies_group.add(new_enemy)
            enemy_respawns.remove(respawn)

def hit_brick(bullets, bricks, stones, enemies, hero, fence, spawn_points, scene):
    for bullet in bullets.copy():
        brick_hit = pygame.sprite.spritecollideany(bullet, bricks)
        stones_hit = pygame.sprite.spritecollideany(bullet, stones)
        hero_hit = pygame.sprite.spritecollideany(bullet, hero)
        fence_hit = pygame.sprite.spritecollideany(bullet, fence)
        enemy_hit = pygame.sprite.spritecollideany(bullet, enemies)
        if brick_hit:
            bullet.kill()
            brick_hit.kill()
        if stones_hit:
            bullet.kill()
        if fence_hit:
            bullet.kill()
        elif enemy_hit:
            if not bullet.owner.is_enemy:
                bullet.kill()
                enemy_hit.kill()
                spawn_point = random.choice(spawn_points)
                enemy_respawns.append({"time": pygame.time.get_ticks(), "pos": spawn_point})
                scene.score = increase(scene.score, 100)
        elif enemy_hit:
            if bullet.owner == enemy_hit:
                bullet.kill()

        elif hero_hit:
            if bullet.owner.is_enemy:
                bullet.kill()
                hero_hit.kill()





def move(hero_sprites, block_sprites):
    keys = pygame.key.get_pressed()
    direction = [0, 0]

    if keys[pygame.K_a]:
        direction = [-1, 0]
    elif keys[pygame.K_d]:
        direction = [1, 0]
    elif keys[pygame.K_w]:
        direction = [0, -1]
    elif keys[pygame.K_s]:
        direction = [0, 1]

    for hero in hero_sprites:
        if direction != [0, 0]:
            hero.changeSpeed(direction)
            hero.is_move = True
            future_rect = hero.rect.move(hero.speed[0], hero.speed[1])

            collision = False
            for block in block_sprites:
                if block.rect.colliderect(future_rect):
                    collision = True
                    break

            if not collision:
                hero.rect = future_rect
        else:
            hero.is_move = False



