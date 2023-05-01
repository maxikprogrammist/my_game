# настройка игры
import pygame
import random
import time
pygame.init()
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('my game')
game_fon = pygame.image.load('sprites\game_fon.jpg')
player_fon = pygame.image.load('sprites\player\player_10_new.png')

# бег персонажа
player_walk = [
    pygame.image.load('sprites\player\player_1_new.png'),
    pygame.image.load('sprites\player\player_2_new.png'),
    pygame.image.load('sprites\player\player_3_new.png'),
    pygame.image.load('sprites\player\player_4_new.png'),
    pygame.image.load('sprites\player\player_5_new.png'),
    pygame.image.load('sprites\player\player_6_new.png'),
    pygame.image.load('sprites\player\player_7_new.png'),
    pygame.image.load('sprites\player\player_8_new.png'),
    pygame.image.load('sprites\player\player_9_new.png'),
    pygame.image.load('sprites\player\player_10_new.png')
    ]
# стрельба персонажа
player_fire = [
    pygame.image.load('sprites\player\player_fire_1_new.png'),
    pygame.image.load('sprites\player\player_fire_2_new.png'),
    pygame.image.load('sprites\player\player_fire_3_new.png'),
    pygame.image.load('sprites\player\player_fire_4_new.png'),
    pygame.image.load('sprites\player\player_fire_5_new.png')
    ]
# характеристики player
walk_anim_count = 0
fire_anim_count = 0
player_x = 400
player_y = 350
player_speed = 5
player_damage = 10
# характеристика monster
monster_anim_count = 0
monster_x = 800
monster_y = 300
monster_speed = 10
monster_health = 500



#главный цикл
running = True
while running:
    # фон и спрайт монстра
    screen.blit(game_fon, (0, 0))
    screen.blit((player_fon), (monster_x, monster_y))
    # персонаж идет вверх или вниз при нелбходимости
    if player_y > monster_y:
        player_y -= 3
    if player_y < monster_y:
        player_y += 3

    if monster_x - player_x <= 200 and monster_y - player_y > 5:
        if player_y > monster_y:
            screen.blit(player_walk[walk_anim_count], (player_x, player_y))
            player_y -= 3
        if player_y < monster_y:
            screen.blit(player_walk[walk_anim_count], (player_x, player_y))
            player_y += 3
        screen.blit(player_fire[fire_anim_count], (player_x, player_y))
        monster_health -= player_damage 

    # проверка расстояния между объектами
    if monster_x - player_x > 200:
        player_x += player_speed
        screen.blit(player_walk[walk_anim_count], (player_x, player_y))
    if monster_x - player_x <= 200:
        screen.blit(player_fire[fire_anim_count], (player_x, player_y))
        monster_health -= player_damage 

    

    if monster_health <= 0:
        a = random.randint(750, 800)
        b = random.randint(300, 400)
        monster_x = a
        monster_y = b
        monster_health = 500


    if walk_anim_count == 9:
        walk_anim_count = 0
    else:
        walk_anim_count += 1 
    if fire_anim_count == 4:
        fire_anim_count = 0
    else:
        fire_anim_count += 1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False
    clock.tick(10)
