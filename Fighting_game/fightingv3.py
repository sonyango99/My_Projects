import pygame
import random

pygame.init()

# Functions to control attacks - DO NOT DELETE
def p1_attack_movement(player_1, p1_attack_list, character):
    if player_1:
        if p1_attack_list:
            for p1_attack_rect in p1_attack_list:
                if blue_ghost_rect.x >= fire_bender_rect.x:
                    p1_attack_rect.x -= 10
                if blue_ghost_rect.x < fire_bender_rect.x:
                    p1_attack_rect.x += 10

                dis.blit(water_attack, p1_attack_rect)

            p1_attack_list = [p1_attack for p1_attack in p1_attack_list if p1_attack.x > 0 and p1_attack.x < dis_width and p1_attack.y > 0 and p1_attack.y < dis_height]

            if character == 4:
                if len(p1_attack_list) >= 7:
                    del p1_attack_list[6]
            else:
                if len(p1_attack_list) >= 4:
                    del p1_attack_list[3]
            if p1_attack_collide > 0:
                del p1_attack_list[0]
            if game_end_score or first_main_menu:
                del p1_attack_list[0:]

            return p1_attack_list
        
        else:
            return []
    
    else:
        if p1_attack_list:
            for p1_attack_rect in p1_attack_list:
                if blue_ghost_rect.x < fire_bender_rect.x:
                    p1_attack_rect.x -= 10
                if blue_ghost_rect.x >= fire_bender_rect.x:
                    p1_attack_rect.x += 10

                dis.blit(water_attack, p1_attack_rect)

            p1_attack_list = [p1_attack for p1_attack in p1_attack_list if p1_attack.x > 0 and p1_attack.x < dis_width and p1_attack.y > 0 and p1_attack.y < dis_height]

            if character == 4:
                if len(p1_attack_list) >= 7:
                    del p1_attack_list[6]
            else:
                if len(p1_attack_list) >= 4:
                    del p1_attack_list[3]
            if p2_attack_collide > 0:
                del p1_attack_list[0]
            if game_end_score or first_main_menu:
                del p1_attack_list[0:]

            return p1_attack_list
        
        else:
            return []
def p1_special_movement(player_1, special_list, character):
    if player_1:
        if special_list:
            for special_rect in special_list:
                if blue_ghost_rect.x >= fire_bender_rect.x:
                    special_rect.x -= 10
                if blue_ghost_rect.x < fire_bender_rect.x:
                    special_rect.x += 10

                dis.blit(fire_attack, special_rect)


            special_list = [special for special in special_list if special.x > 0 and special.x < dis_width and special.y > 0 and special.y < dis_height]

            if character == 4:
                if len(special_list) >= 7:
                    del special_list[6]
            else:
                if len(special_list) >= 4:
                    del special_list[3]
            if p1_special_collide > 0:
                del special_list[0]
            if game_end_score or first_main_menu:
                del special_list[0]
                

            return special_list

        else:
            return []
        
    if not player_1:
        if special_list:
            for special_rect in special_list:
                if blue_ghost_rect.x < fire_bender_rect.x:
                    special_rect.x -= 10
                if blue_ghost_rect.x >= fire_bender_rect.x:
                    special_rect.x += 10

                dis.blit(fire_attack, special_rect)


            special_list = [special for special in special_list if special.x > 0 and special.x < dis_width and special.y > 0 and special.y < dis_height]

            if character == 4:
                if len(special_list) >= 7:
                    del special_list[6]
            else:
                if len(special_list) >= 4:
                    del special_list[3]
            if p2_special_collide > 0:
                del special_list[0]
            if game_end_score or first_main_menu:
                del special_list[0]

            return special_list

        else:
            return []

# Function for collision - DO NOT DELETE
def p2_hit(player2, attack):
    if attack:
        for attack_rect in attack:
            if player2.colliderect(attack_rect):
                return True
            else:
                return False

# Functions to determine texts - DO NOT DELETE
def p1_health_bar(health):
    p1_bar = health_font.render(f"Health: {health}", True, black)
    p1_bar_rect = p1_bar.get_rect(topleft = [100, 10])
    dis.blit(p1_bar, p1_bar_rect)
def p2_health_bar(health):
    p2_bar = health_font.render(f"Health: {health}", True, black)
    p2_bar_rect = p2_bar.get_rect(topright = [1400, 10])
    dis.blit(p2_bar, p2_bar_rect)
def p1_special_bar(special, character):
    if character == 4:
        p1_spec = special_font.render(f"Mana: NONE", True, black)
        p1_spec_rect = p1_spec.get_rect(topleft = [400, 25])
        dis.blit(p1_spec, p1_spec_rect)
    else:
        if special == 100:
            if character == 1:
                p1_spec = special_font.render(f"Mana: {special}", True, red)
                p1_spec_rect = p1_spec.get_rect(topleft = [400, 25])
                dis.blit(p1_spec, p1_spec_rect)
            if character == 2:
                p1_spec = special_font.render(f"Mana: {special}", True, blue)
                p1_spec_rect = p1_spec.get_rect(topleft = [400, 25])
                dis.blit(p1_spec, p1_spec_rect)
            if character == 3:
                p1_spec = special_font.render(f"Mana: {special}", True, green)
                p1_spec_rect = p1_spec.get_rect(topleft = [400, 25])
                dis.blit(p1_spec, p1_spec_rect)
        else:
            p1_spec = special_font.render(f"Mana: {special}", True, black)
            p1_spec_rect = p1_spec.get_rect(topleft = [400, 25])
            dis.blit(p1_spec, p1_spec_rect)
def p2_special_bar(special, character):
    if character == 4:
        p2_spec = special_font.render(f"Mana: NONE", True, black)
        p2_spec_rect = p2_spec.get_rect(topright = [1100, 25])
        dis.blit(p2_spec, p2_spec_rect)
    else:
        if special == 100:
            if character == 1:
                p2_spec = special_font.render(f"Mana: {special}", True, red)
                p2_spec_rect = p2_spec.get_rect(topright = [1100, 25])
                dis.blit(p2_spec, p2_spec_rect)
            if character == 2:
                p2_spec = special_font.render(f"Mana: {special}", True, blue)
                p2_spec_rect = p2_spec.get_rect(topright = [1100, 25])
                dis.blit(p2_spec, p2_spec_rect)
            if character == 3:
                p2_spec = special_font.render(f"Mana: {special}", True, green)
                p2_spec_rect = p2_spec.get_rect(topright = [1100, 25])
                dis.blit(p2_spec, p2_spec_rect)
        else:
            p2_spec = special_font.render(f"Mana: {special}", True, black)
            p2_spec_rect = p2_spec.get_rect(topright = [1100, 25])
            dis.blit(p2_spec, p2_spec_rect)

# Time text and time control - DO NOT DELETE
def timer(count, start_time):
    global game_time
    time = int(pygame.time.get_ticks()/1000) - start_time
    game_time = count - time
    time_count = time_font.render(f"{game_time}", True, black)
    time_count_rect = time_count.get_rect( midtop = [750, 10])
    dis.blit(time_count, time_count_rect)
# Functions to determine texts - DO NOT DELETE
def menu_message(msg, colour, positionx, positiony):
    mess = message_font.render(msg, True, colour)
    mess_rect = mess.get_rect(center = [positionx, positiony])
    dis.blit(mess, mess_rect)
def choice_message(msg, colour, positionx, positiony):
    choice = choice_font.render(msg, True, colour)
    choice_rect = choice.get_rect(center = [positionx, positiony])
    dis.blit(choice, choice_rect)
def controls_message(msg, colour, positionx, positiony):
    mess = controls_font.render(msg, True, colour)
    mess_rect = mess.get_rect(center = [positionx, positiony])
    dis.blit(mess, mess_rect)
# Function for player 1 to pick a character - DO NOT DELETE 
def player_choice(player1):
    global player_1_character, player_1_character_win, player_1_character_lost

    if player1 == 1:
        player_1_character = fire_bender
        player_1_character_win = pygame.transform.rotozoom(player_1_character, 0, 1)
        player_1_character_lost = pygame.transform.rotozoom(player_1_character, 90, 1)

    elif player1 == 2:
        player_1_character = blue_ghost
        player_1_character_win = pygame.transform.rotozoom(player_1_character, 0, 1)
        player_1_character_lost = pygame.transform.rotozoom(player_1_character, 90, 1)

    elif player1 == 3:
        player_1_character = green_ghost
        player_1_character_win = pygame.transform.rotozoom(player_1_character, 0, 1)
        player_1_character_lost = pygame.transform.rotozoom(player_1_character, 90, 1)

    elif player1 == 4:
        player_1_character = yellow_ghost
        player_1_character_win = pygame.transform.rotozoom(player_1_character, 0, 1)
        player_1_character_lost = pygame.transform.rotozoom(player_1_character, 90, 1)

    if p1_invincible_mode:
        player_1_character = special_ghost

def player_choice_left(player1):
    global player_1_character_left

    if player1 == 1:
        player_1_character_left = fire_bender_left

    elif player1 == 2:
        player_1_character_left = blue_ghost_left

    elif player1 == 3:
        player_1_character_left = green_ghost_left

    elif player1 == 4:
        player_1_character_left = yellow_ghost_left

    if p1_invincible_mode:
        player_1_character_left = special_ghost_left

# Function for player 2 to pick a character - DO NOT DELETE 
def player2_choice(player2):
    global player_2_character, player_2_character_win, player_2_character_lost

    if player2 == 1:
        player_2_character = fire_bender
        player_2_character_win = pygame.transform.rotozoom(player_2_character, 0, 1)
        player_2_character_lost = pygame.transform.rotozoom(player_2_character, 90, 1)

    elif player2 == 2:
        player_2_character = blue_ghost
        player_2_character_win = pygame.transform.rotozoom(player_2_character, 0, 1)
        player_2_character_lost = pygame.transform.rotozoom(player_2_character, 90, 1)

    elif player2 == 3:
        player_2_character = green_ghost
        player_2_character_win = pygame.transform.rotozoom(player_2_character, 0, 1)
        player_2_character_lost = pygame.transform.rotozoom(player_2_character, 90, 1)

    elif player2 == 4:
        player_2_character = yellow_ghost
        player_2_character_win = pygame.transform.rotozoom(player_2_character, 0, 1)
        player_2_character_lost = pygame.transform.rotozoom(player_2_character, 90, 1)

    if p2_invincible_mode:
        player_2_character = special_ghost

def player2_choice_left(player2):
    global player_2_character_left

    if player2 == 1:
        player_2_character_left = fire_bender_left

    elif player2 == 2:
        player_2_character_left = blue_ghost_left

    elif player2 == 3:
        player_2_character_left = green_ghost_left

    elif player2 == 4:
        player_2_character_left = yellow_ghost_left
    
    if p2_invincible_mode:
        player_2_character_left = special_ghost_left

def menu_ghost_random(random):
    global blue_ghost_menu

    if random == 1:
        blue_ghost_menu = fire_bender_left

    elif random == 2:
        blue_ghost_menu = blue_ghost_left

    elif random == 3:
        blue_ghost_menu = green_ghost_left

    elif random == 4:
        blue_ghost_menu = yellow_ghost_left

# Pygame varibales - DO NOT DELETE
dis_width = 1500
dis_height = 750
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption("Fighting verson 3 by Silvano A. Onyango")

# Colours - DO NOT DELETE
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
grass = (0, 153, 0)
blue = (0, 0, 255)
sky_blue = (51, 153, 255)
black = (0, 0, 0)

# Fonts - DO NOT DELETE
health_font = pygame.font.SysFont("helvetica", 40, 1)
time_font = pygame.font.SysFont("frutiger", 60)
message_font = pygame.font.SysFont("garamond", 100)
choice_font = pygame.font.SysFont("garamond", 50)
special_font = pygame.font.SysFont("helvetica", 40)
controls_font = pygame.font.SysFont("ariel", 25)

# FPS
clock = pygame.time.Clock()

# Characters movement speed - DO NOT DELETE
movement = 10

# Easy to change values
health = 500
time = 120
p1_basic_damage = 10
p2_basic_damage = 10
p1_second_damage = 20
p2_second_damage = 20
special_impact_amount = 10
basic_special_amount_add = 5
second_special_amount_add = 10
p1_start_x = 200
p2_start_x = 1300
start_y = 650

# Player 1 variables for health, attacks and movement - DO NOT DELETE
p1_move_right = False
p1_move_left = False
p1_move_up = False

p1_attack_collide = 0
p1_special_collide = 0
p1_health = health
p1_special_amount = 0
        # Player 1 postioning
p1_bender_x = p1_start_x
p1_bender_y = start_y
        # Defines Player 1 gravity
p1_bender_gravity = 0
        # List to control attack
p1_attack_rect_list = []
p1_special_rect_list = []

# Player 2 variables for health, attacks and movement - DO NOT DELETE
p2_move_right = False
p2_move_left = False
p2_move_up = False

p2_attack_collide = 0
p2_special_collide = 0
p2_health = health
p2_special_amount = 0
        # Player 2 postioning
p2_bender_x = p2_start_x
p2_bender_y = start_y
        # Defines Player 2 gravity
p2_bender_gravity = 0
        # List to control attack
p2_attack_rect_list = []
p2_special_rect_list = []

# Surfaces - DO NOT DELETE
            # Main menu surface
main_menu_surf = pygame.image.load("avatar_images\main_menu.png").convert_alpha()
main_menu_surf = pygame.transform.scale(main_menu_surf, (dis_width, dis_height))
            # Background surfaces
ground_surf = pygame.image.load("avatar_images\ground.png")
ground_surf = pygame.transform.scale(ground_surf, (dis_width, 200))
ground_rect = ground_surf.get_rect(topleft = (0, 650))
ground_surf_burn = pygame.image.load("avatar_images\ground_burn.png")
ground_surf_burn = pygame.transform.scale(ground_surf_burn, (dis_width, 200))

sky_surf = pygame.image.load("avatar_images\Sky.png")
sky_surf = pygame.transform.scale(sky_surf, (dis_width, dis_height))
sky_surf_burn = pygame.image.load("avatar_images\Sky_burn.png")
sky_surf_burn = pygame.transform.scale(sky_surf_burn, (dis_width, dis_height))
            # Blue character menu surface
ghost_menu = pygame.image.load("avatar_images\ghost_blue_right.png").convert_alpha()
ghost_menu = pygame.transform.rotozoom(ghost_menu, 0, .15)
            # Blue Character surface
blue_ghost = pygame.image.load("avatar_images\ghost_blue_right.png").convert_alpha()
blue_ghost = pygame.transform.rotozoom(blue_ghost, 0, .15)
blue_ghost_rect = blue_ghost.get_rect(midbottom = (p1_bender_x, p1_bender_y))
blue_ghost_left = pygame.image.load("avatar_images\ghost_blue_left.png").convert_alpha()
blue_ghost_left = pygame.transform.rotozoom(blue_ghost_left, 0, .15)
            # Green Character surface
green_ghost = pygame.image.load("avatar_images\ghost_green_right.png").convert_alpha()
green_ghost = pygame.transform.rotozoom(green_ghost, 0, .15)
green_ghost_left = pygame.image.load("avatar_images\ghost_green_left.png").convert_alpha()
green_ghost_left = pygame.transform.rotozoom(green_ghost_left, 0, .15)
            # Yellow Character surface
yellow_ghost = pygame.image.load("avatar_images\ghost_yellow_right.png").convert_alpha()
yellow_ghost = pygame.transform.rotozoom(yellow_ghost, 0, .15)
yellow_ghost_left = pygame.image.load("avatar_images\ghost_yellow_left.png").convert_alpha()
yellow_ghost_left = pygame.transform.rotozoom(yellow_ghost_left, 0, .15)
            # Red Character surface
fire_bender = pygame.image.load("avatar_images\ghost_red_right.png").convert_alpha()
fire_bender = pygame.transform.rotozoom(fire_bender, 0, .15)
fire_bender_rect = fire_bender.get_rect(midbottom = (p2_bender_x, p2_bender_y))
fire_bender_left = pygame.image.load("avatar_images\ghost_red_left.png").convert_alpha()
fire_bender_left = pygame.transform.rotozoom(fire_bender_left, 0, .15)
            # White special character surface
special_ghost = pygame.image.load("avatar_images\ghost_white_right.png").convert_alpha()
special_ghost = pygame.transform.rotozoom(special_ghost, 0, .15)
special_ghost_left = pygame.image.load("avatar_images\ghost_white_left.png").convert_alpha()
special_ghost_left = pygame.transform.rotozoom(special_ghost_left, 0, .15)
            # Button 2 attack surface
fire_attack = pygame.image.load("avatar_images\water_bullet.png").convert_alpha()
fire_attack = pygame.transform.rotozoom(fire_attack, 90, 0.04)
fire_attack_rect = fire_attack.get_rect(center = blue_ghost_rect.center)
            # Button 1 attack surface
water_attack = pygame.image.load("avatar_images\pack_bullet.png").convert_alpha()
water_attack = pygame.transform.rotozoom(water_attack, 0, 0.04)
water_attack_rect = water_attack.get_rect(center = blue_ghost_rect.center)
            # Defines variables used for character select function
blue_ghost_menu = ghost_menu
player_1_character = blue_ghost
player_1_character_left = blue_ghost_left
player_2_character = fire_bender
player_2_character_left = fire_bender_left

# Variables for the screens - DO NOT DELETE
game_quit = False
game_end_score = False
first_main_menu = True
second_main_menu = False
third_main_menu = False
controls_page = False

# Defines variable to determine which character attack to do - DO NOT DELETE
player1 = False
player2 = False

# Defines variable to determine what option is hovered over - DO NOT DELETE
show_back = 0

# Defines variable to determine colour of text in some screens - DO NOT DELETE
colour1 = white
colour2 = white
colour3 = white
colour4 = white

# Defines the variables for choosing player characters - DO NOT DELETE
player_1 = 0
player_2 = 0

# Variable for game count down reset - DO NOT DELETE
start_time = 0

# Timer event for attacks
p1_special_timer = pygame.USEREVENT + 1
pygame.time.set_timer(p1_special_timer, 1000)
p2_special_timer = pygame.USEREVENT + 2
pygame.time.set_timer(p2_special_timer, 1000)
p1_count_up = 0
p2_count_up = 0
count_up_max = 10

# Variables for special attacks - DO NOT DELETE
p2_burning_mode = False
p1_burning_mode = False
p2_invincible_mode = False
p1_invincible_mode = False

# The game running, ends when game_quit = True - DO NOT DELETE
while not game_quit:

    # Varibales to decide who player is
    player_choice(player_1)
    player_choice_left(player_1)
    player2_choice(player_2)
    player2_choice_left(player_2)
    menu_ghost_random(random.randint(1,4))

    # First screen seen and main menu 
    while first_main_menu:

        # Variables for screen
        choose_play = pygame.draw.rect(dis, red, [150, 500, 200, 100])
        choose_quit = pygame.draw.rect(dis, red, [1150, 500, 200, 100])
        choose_controls = pygame.draw.rect(dis, red, [575, 550, 350, 100])

        mouse_pos = pygame.mouse.get_pos()
        
        # When hover over options
        dis.blit(main_menu_surf, (0, 0))
        if show_back == 2:
            dis.blit(blue_ghost_menu, (175, 475))
        if show_back == 3:
            dis.blit(blue_ghost_menu, (1175, 475))
        if show_back == 4:
            dis.blit(blue_ghost_menu, (675, 525))
        
        if choose_play.collidepoint(mouse_pos):
            show_back = 2
            colour2 = white
        elif choose_quit.collidepoint(mouse_pos):
            show_back = 3
            colour3 = white
        elif choose_controls.collidepoint(mouse_pos):
            show_back = 4
            colour4 = white
        else:
            show_back = 0
            colour2 = white
            colour3 = white
            colour4 = white
            
        # Printed on screen
        menu_message("Ghost Fight", colour1, 750, 150)
        menu_message("Play", colour2, 250, 550)
        menu_message("Quit", colour3, 1250, 550)
        menu_message("Controls", colour4, 750, 600)
        
        # Inputs for options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                first_main_menu = False
                game_quit = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    first_main_menu = False
                    game_quit = True
                if event.key == pygame.K_p:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = True
                if event.key == pygame.K_c:
                    first_main_menu = False
                    game_quit = False
                    controls_page = True
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if choose_play.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = True
                if choose_quit.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = True
                if choose_controls.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    controls_page = True

        pygame.display.update()

    # Player 1 Character select
    while second_main_menu:

        # Variables for screen
        choose_red = pygame.draw.rect(dis, red, [350, 500, 200, 80])
        choose_blue = pygame.draw.rect(dis, blue, [850, 500, 200, 80])
        choose_green = pygame.draw.rect(dis, green, [350, 600, 200, 80])
        choose_yellow = pygame.draw.rect(dis, yellow, [850, 600, 200, 80])

        mouse_pos = pygame.mouse.get_pos()

        # What appears when hover over options
        dis.blit(main_menu_surf, (0, 0))
        if show_back == 1:
            dis.blit(fire_bender, (375, 475))
        if show_back == 2:
            dis.blit(blue_ghost, (875, 475))
        if show_back == 3:
            dis.blit(green_ghost, (375, 575))
        if show_back == 4:
            dis.blit(yellow_ghost, (875, 575))
        
        if choose_red.collidepoint(mouse_pos):
            show_back = 1
            colour1 = white
        elif choose_blue.collidepoint(mouse_pos):
            show_back = 2
            colour2 = white
        elif choose_green.collidepoint(mouse_pos):
            show_back = 3
            colour3 = white
        elif choose_yellow.collidepoint(mouse_pos):
            show_back = 4
            colour4 = white
        else:
            show_back = 0
            colour1 = red
            colour2 = blue
            colour3 = green
            colour4 = yellow

        # Printed on screen
        menu_message("Player 1 Character Select", white, 750, 150)
        choice_message("Red", colour1, 450, 550)
        choice_message("Blue", colour2, 950, 550)
        choice_message("Green", colour3, 450, 650)
        choice_message("Yellow", colour4, 950, 650)
        
        # Inputs for options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                first_main_menu = False
                game_quit = True
                second_main_menu = False
                third_main_menu = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 1
                if event.key == pygame.K_2:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 2
                if event.key == pygame.K_3:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 3
                if event.key == pygame.K_4:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 4
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if choose_blue.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 2
                if choose_red.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 1
                if choose_green.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 3
                if choose_yellow.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = True
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_1 = 4

        pygame.display.update()

    # Player 2 character select
    while third_main_menu:

        # Variables for screen
        choose_red = pygame.draw.rect(dis, red, [350, 500, 200, 80])
        choose_blue = pygame.draw.rect(dis, blue, [850, 500, 200, 80])
        choose_green = pygame.draw.rect(dis, green, [350, 600, 200, 80])
        choose_yellow = pygame.draw.rect(dis, yellow, [850, 600, 200, 80])

        mouse_pos = pygame.mouse.get_pos()

        # What appears when hover over option
        dis.blit(main_menu_surf, (0, 0))
        if show_back == 1:
            dis.blit(fire_bender, (375, 475))
        if show_back == 2:
            dis.blit(blue_ghost, (875, 475))
        if show_back == 3:
            dis.blit(green_ghost, (375, 575))
        if show_back == 4:
            dis.blit(yellow_ghost, (875, 575))
        
        if choose_red.collidepoint(mouse_pos):
            show_back = 1
            colour1 = white
        elif choose_blue.collidepoint(mouse_pos):
            show_back = 2
            colour2 = white
        elif choose_green.collidepoint(mouse_pos):
            show_back = 3
            colour3 = white
        elif choose_yellow.collidepoint(mouse_pos):
            show_back = 4
            colour4 = white
        else:
            show_back = 0
            colour1 = red
            colour2 = blue
            colour3 = green
            colour4 = yellow

        # Printed on screen
        menu_message("Player 2 Character Select", white, 750, 150)
        choice_message("Red", colour1, 450, 550)
        choice_message("Blue", colour2, 950, 550)
        choice_message("Green", colour3, 450, 650)
        choice_message("Yellow", colour4, 950, 650)
        
        # Inputs for options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                first_main_menu = False
                game_quit = True
                second_main_menu = False
                third_main_menu = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 1
                if event.key == pygame.K_2:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 2
                if event.key == pygame.K_3:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 3
                if event.key == pygame.K_4:
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 4
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if choose_blue.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 2
                if choose_red.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 1
                if choose_green.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 3
                if choose_yellow.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    second_main_menu = False
                    third_main_menu = False
                    start_time = int(pygame.time.get_ticks()/1000)
                    player_2 = 4

        pygame.display.update()

    # End of game screen
    while game_end_score:

        # Variables for screen
        choose_play_again = pygame.draw.rect(dis, red, [150, 500, 200, 80])
        choose_character_select = pygame.draw.rect(dis, blue, [950, 500, 355, 80])
        choose_main_menu = pygame.draw.rect(dis, green, [330, 600, 250, 80])
        choose_quit_game = pygame.draw.rect(dis, yellow, [850, 600, 200, 80])

        colour1 = white
        colour2 = white
        colour3 = white

        mouse_pos = pygame.mouse.get_pos()
        
        # Different screen shown depending on end of game condition
        if p1_health > 0 and p2_health <= 0:
            dis.fill(black)

            if show_back == 1:
                dis.blit(player_1_character, (175, 475))
            if show_back == 2:
                dis.blit(player_1_character, (1075, 475))
            if show_back == 3:
                dis.blit(player_1_character, (355, 575))
            if show_back == 4:
                dis.blit(player_1_character, (880, 575))

            dis.blit(player_1_character_win, (650, 250))
            menu_message("Player 1 WINS", white, 750, 150)
            choice_message("Play Again", colour1, 250, 550)
            choice_message("Character Select", colour2, 1150, 550)
            choice_message("Main Menu", colour3, 450, 650)
            choice_message("Quit", colour4, 950, 650)
        
        elif p2_health > 0 and p1_health <= 0:
            dis.fill(black)

            if show_back == 1:
                dis.blit(player_2_character, (175, 475))
            if show_back == 2:
                dis.blit(player_2_character, (1075, 475))
            if show_back == 3:
                dis.blit(player_2_character, (355, 575))
            if show_back == 4:
                dis.blit(player_2_character, (880, 575))

            dis.blit(player_2_character_win, (650, 250))
            menu_message("Player 2 WINS", white, 750, 150)
            choice_message("Play Again", colour1, 250, 550)
            choice_message("Character Select", colour2, 1150, 550)
            choice_message("Main Menu", colour3, 450, 650)
            choice_message("Quit", colour4, 950, 650)
        
        elif p1_health <= 0 and p2_health <= 0:
            dis.fill(black)

            if show_back == 1:
                dis.blit(blue_ghost_menu, (175, 475))
            if show_back == 2:
                dis.blit(blue_ghost_menu, (1075, 475))
            if show_back == 3:
                dis.blit(blue_ghost_menu, (355, 575))
            if show_back == 4:
                dis.blit(blue_ghost_menu, (880, 575))

            dis.blit(player_2_character_lost, (1050, 300))
            dis.blit(player_1_character_lost, (450, 300))
            menu_message("DRAW", white, 750, 150)
            choice_message("Play Again", colour1, 250, 550)
            choice_message("Character Select", colour2, 1150, 550)
            choice_message("Main Menu", colour3, 450, 650)
            choice_message("Quit", colour4, 950, 650)
        
        elif game_time <= 0:
            dis.blit(main_menu_surf, (0, 0))

            if show_back == 1:
                dis.blit(blue_ghost_menu, (175, 475))
            if show_back == 2:
                dis.blit(blue_ghost_menu, (1075, 475))
            if show_back == 3:
                dis.blit(blue_ghost_menu, (355, 575))
            if show_back == 4:
                dis.blit(blue_ghost_menu, (880, 575))
            
            menu_message("DRAW", white, 750, 150)
            choice_message("Play Again", colour1, 250, 550)
            choice_message("Character Select", colour2, 1150, 550)
            choice_message("Main Menu", colour3, 450, 650)
            choice_message("Quit", colour4, 950, 650)
        
        # Collison detection
        if choose_play_again.collidepoint(mouse_pos):
            show_back = 1
        elif choose_character_select.collidepoint(mouse_pos):
            show_back = 2
        elif choose_main_menu.collidepoint(mouse_pos):
            show_back = 3
        elif choose_quit_game.collidepoint(mouse_pos):
            show_back = 4
        else:
            show_back = 0
            colour2 = white
            colour3 = white
            colour4 = white

        # Inputs to choose options
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                first_main_menu = False
                game_quit = True
                game_end_score = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    first_main_menu = False
                    game_quit = True
                    game_end_score = False

                if event.key == pygame.K_p:
                    first_main_menu = False
                    game_quit = False
                    game_end_score = False
                    p2_burning_mode = False
                    p1_burning_mode = False
                    p2_health = health
                    p1_health = health
                    start_time = int(pygame.time.get_ticks()/1000)
                    p1_attack_rect_list.clear()
                    p1_special_rect_list.clear()
                    p2_attack_rect_list.clear()
                    p2_special_rect_list.clear()
                    fire_bender_rect.bottom = 650
                    blue_ghost_rect.bottom = 650
                
                if event.key == pygame.K_c:
                    first_main_menu = False
                    game_quit = False
                    game_end_score = False
                    second_main_menu = True
                    p2_burning_mode = False
                    p1_burning_mode = False
                    p2_health = health
                    p1_health = health
                    start_time = int(pygame.time.get_ticks()/1000)
                    p1_attack_rect_list.clear()
                    p1_special_rect_list.clear()
                    p2_attack_rect_list.clear()
                    p2_special_rect_list.clear()
                    fire_bender_rect.bottom = 650
                    blue_ghost_rect.bottom = 650
                
                if event.key == pygame.K_m:
                    first_main_menu = True
                    game_quit = False
                    game_end_score = False
                    p2_burning_mode = False
                    p1_burning_mode = False
                    p2_health = health
                    p1_health = health
                    start_time = int(pygame.time.get_ticks()/1000)
                    p1_attack_rect_list.clear()
                    p1_special_rect_list.clear()
                    p2_attack_rect_list.clear()
                    p2_special_rect_list.clear()
                    fire_bender_rect.bottom = 650
                    blue_ghost_rect.bottom = 650
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if choose_play_again.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    game_end_score = False
                    p2_burning_mode = False
                    p1_burning_mode = False
                    p2_health = health
                    p1_health = health
                    start_time = int(pygame.time.get_ticks()/1000)
                    p1_attack_rect_list.clear()
                    p1_special_rect_list.clear()
                    p2_attack_rect_list.clear()
                    p2_special_rect_list.clear()
                    fire_bender_rect.bottom = 650
                    blue_ghost_rect.bottom = 650
                
                if choose_quit_game.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = True
                    game_end_score = False
                
                if choose_main_menu.collidepoint(mouse_pos):
                    first_main_menu = True
                    game_quit = False
                    game_end_score = False
                    p2_burning_mode = False
                    p1_burning_mode = False
                    p2_health = health
                    p1_health = health
                    start_time = int(pygame.time.get_ticks()/1000)
                    p1_attack_rect_list.clear()
                    p1_special_rect_list.clear()
                    p2_attack_rect_list.clear()
                    p2_special_rect_list.clear()
                    fire_bender_rect.bottom = 650
                    blue_ghost_rect.bottom = 650

                if choose_character_select.collidepoint(mouse_pos):
                    first_main_menu = False
                    game_quit = False
                    game_end_score = False
                    second_main_menu = True
                    p2_burning_mode = False
                    p1_burning_mode = False
                    p2_health = health
                    p1_health = health
                    start_time = int(pygame.time.get_ticks()/1000)
                    p1_attack_rect_list.clear()
                    p1_special_rect_list.clear()
                    p2_attack_rect_list.clear()
                    p2_special_rect_list.clear()
                    fire_bender_rect.bottom = 650
                    blue_ghost_rect.bottom = 650

        pygame.display.update()

    # Controls screen
    while controls_page:

        mouse_pos = pygame.mouse.get_pos()
        choose_return = pygame.draw.rect(dis, red, [675, 575, 150, 50])

        dis.fill(black)
        # What shows when hover over return
        if choose_return.collidepoint(mouse_pos):
            dis.blit(blue_ghost_menu, (675, 510))

        menu_message("Controls", white, 750, 50)
        # Player 1 controls
        controls_message("Player 1", white, 375, 150 )
        controls_message("WASD - For Movement", white, 375, 200)
        controls_message("1 - Basic Attack", white, 375, 250)
        controls_message("2 - Heavy Attack", white, 375, 300)
        controls_message("3 - Magic", white, 375, 350)
        # Player 2 controls
        controls_message("Player 2", white, 1075, 150 )
        controls_message("Arrow Keys - For Movement", white, 1075, 200)
        controls_message("NUM 1 - Basic Attack", white, 1075, 250)
        controls_message("NUM 2 - Heavy Attack", white, 1075, 300)
        controls_message("NUM 3 - Magic", white, 1075, 350)
        # Character lore
                    # Red
        controls_message("Red - Scorched Earth", red, 750, 125)
        controls_message("10 damage per second for 10 seconds", red, 750, 150)
                    # Blue
        controls_message("Blue - Healing Afterlife", blue, 750, 225)
        controls_message("Turns Mana into Health", blue, 750, 250)
                    # Green
        controls_message("Green - Ghostly Protection", green, 750, 325)
        controls_message("Invincible for 10 Seconds", green, 750, 350)
                    # Yellow
        controls_message("Yellow - The Untalented but Hardworking", yellow, 750, 425)
        controls_message("Cannot use Magic", yellow, 750, 450)
        controls_message("Has a higher Jump", yellow, 750, 475)
        controls_message("Can fire double the amount of Basic and Heavy Attacks", yellow, 750, 500)
        # Return to main menu
        choice_message("Return", white, 750, 600)

        # Inputs for control screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                controls_page = False
                game_quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    controls_page = False
                    game_quit = True

                if event.key == pygame.K_r:
                    controls_page = False
                    first_main_menu = True
                    game_quit = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if choose_return.collidepoint(mouse_pos):
                    controls_page = False
                    first_main_menu = True
                    game_quit = False

        pygame.display.update()

    # Key inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
        
        if event.type == pygame.KEYDOWN:

            # Player 1 movement input
            if event.key == pygame.K_w:
                p1_move_up = True
            
            if event.key == pygame.K_d:
                p1_move_right = True
        
            if event.key == pygame.K_a:
                p1_move_left = True

            if event.key == pygame.K_1:
                p1_attack_rect_list.append(water_attack.get_rect(center = blue_ghost_rect.center))
                player1 = True

            if event.key == pygame.K_2:
                    p1_special_rect_list.append(fire_attack.get_rect(center = blue_ghost_rect.center))
                    player1 = True

            if event.key == pygame.K_3:
                if player_1 == 1 and p1_special_amount == 100:
                    p1_burning_mode = True
                    
                if player_1 == 2:
                    p1_health += p1_special_amount
                    p1_special_amount = 0
                    
                if player_1 == 3 and p1_special_amount == 100:
                    p1_invincible_mode = True
                    
            
            # Player 2 movement input
            if event.key == pygame.K_UP:
                p2_move_up = True
            
            if event.key == pygame.K_RIGHT:
                p2_move_right = True
        
            if event.key == pygame.K_LEFT:
                p2_move_left = True

            if event.key == pygame.K_KP1:
                p2_attack_rect_list.append(water_attack.get_rect(center = fire_bender_rect.center))
                player2 = True

            if event.key == pygame.K_KP2:
                p2_special_rect_list.append(fire_attack.get_rect(center = fire_bender_rect.center))
                player2 = True

            if event.key == pygame.K_KP3:
                if player_2 == 1 and p2_special_amount == 100:
                    p2_burning_mode = True
                    player2 = True
                if player_2 == 2:
                    p2_health += p2_special_amount
                    p2_special_amount = 0
                    
                if player_2 == 3 and p2_special_amount == 100:
                    p2_invincible_mode = True
                    

        if event.type == pygame.KEYUP:

            # Player 1 movement continued
            if event.key == pygame.K_w:
                p1_move_up = False
            
            if event.key == pygame.K_d:
                p1_move_right = False
        
            if event.key == pygame.K_a:
                p1_move_left = False

            # Player 2 movement continued
            if event.key == pygame.K_UP:
                p2_move_up = False
            
            if event.key == pygame.K_RIGHT:
                p2_move_right = False
        
            if event.key == pygame.K_LEFT:
                p2_move_left = False

        if event.type == p2_special_timer:
            if p2_burning_mode:
                if player_2 == 1 and p2_special_amount == 100:
                    if p2_count_up < count_up_max and p2_count_up >= 0:
                        p2_count_up += 1
                        p1_health -= special_impact_amount
                    elif p2_count_up >= count_up_max:
                        p2_count_up = 0
                        p2_burning_mode = False
                        p2_special_amount = 0

            if p2_invincible_mode:
                if p2_special_amount == 100:
                    if p2_count_up < count_up_max and p2_count_up >= 0:
                        p2_count_up +=1
                        p2_health += 0
                        p1_basic_damage = 0
                        p1_second_damage = 0
                        special_impact_amount = 0
                    elif p2_count_up >= count_up_max:
                        p2_count_up = 0
                        p2_invincible_mode = False
                        p2_special_amount = 0
                        p1_basic_damage = 10
                        p1_second_damage = 20
                        special_impact_amount = 10

        if event.type == p1_special_timer:
            if p1_burning_mode:
                if player_1 == 1 and p1_special_amount == 100:
                    if p1_count_up < count_up_max and p1_count_up >= 0:
                        p1_count_up += 1
                        p2_health -= special_impact_amount
                    elif p1_count_up >= count_up_max:
                        p1_count_up = 0
                        p1_burning_mode = False
                        p1_special_amount = 0

            if p1_invincible_mode:
                if p1_special_amount == 100:
                    if p1_count_up < count_up_max and p1_count_up >= 0:
                        p1_count_up +=1
                        p2_basic_damage = 0
                        p2_second_damage = 0
                        special_impact_amount = 0
                    elif p1_count_up >= count_up_max:
                        p1_count_up = 0
                        p1_invincible_mode = False
                        p1_special_amount = 0
                        p2_basic_damage = 10
                        p2_second_damage = 20
                        special_impact_amount = 10

    # Player 1 movement executed
    if p1_move_right and blue_ghost_rect.right < dis_width:
        blue_ghost_rect.x += movement
    if p1_move_left and blue_ghost_rect.left > 0:
        blue_ghost_rect.x -= movement
    # Yellow has a higher jump
    if p1_move_up and blue_ghost_rect.bottom >= 650:
        if player_1 == 4:
            p1_bender_gravity = -35
        else:
            p1_bender_gravity = -25

    # Player 2 movement executed
    if p2_move_right and fire_bender_rect.right < dis_width:
        fire_bender_rect.x += movement
        p2_bender_x += movement
    if p2_move_left and fire_bender_rect.left > 0:
        fire_bender_rect.x -= movement
        p2_bender_x -= movement
    # Yellow has a higher jump
    if p2_move_up and fire_bender_rect.bottom >= 650:
        if player_2 == 4:
            p2_bender_gravity = -35
        else:
            p2_bender_gravity = -25

    # The background for arena
    if p1_burning_mode or p2_burning_mode:
        dis.blit(sky_surf_burn, (0, 0))
        dis.blit(ground_surf_burn, ground_rect)
    else:
        dis.blit(sky_surf, (0, 0))
        dis.blit(ground_surf, ground_rect)
    
    # Attack list for attack to work
    if player1:
        p1_attack_rect_list = p1_attack_movement(True, p1_attack_rect_list, player_1)
        p1_special_rect_list = p1_special_movement(True, p1_special_rect_list, player_1)
    if player2:
        p2_attack_rect_list = p1_attack_movement(False, p2_attack_rect_list, player_2)
        p2_special_rect_list = p1_special_movement(False, p2_special_rect_list, player_2)

    # Player 1 gravity and floor
    p1_bender_gravity += 1
    blue_ghost_rect.y += p1_bender_gravity
    if blue_ghost_rect.bottom > 650:
        blue_ghost_rect.bottom = 650
    if blue_ghost_rect.x <= fire_bender_rect.x:
        dis.blit(player_1_character, blue_ghost_rect)
    else:
        dis.blit(player_1_character_left, blue_ghost_rect)

    # Player2 gravity and floor
    p2_bender_gravity += 1
    fire_bender_rect.y += p2_bender_gravity
    if fire_bender_rect.bottom > 650:
        fire_bender_rect.bottom = 650
    if blue_ghost_rect.x <= fire_bender_rect.x:
        dis.blit(player_2_character_left, fire_bender_rect)
    else:
        dis.blit(player_2_character, fire_bender_rect)

    # Collison with attacks
    if player1:
        damage = p2_hit(fire_bender_rect, p1_attack_rect_list)
        if damage and p1_attack_collide == 0:
            p1_attack_collide += 1
            p2_health -= p1_basic_damage
            if not p1_burning_mode:
                p1_special_amount += basic_special_amount_add
            if p1_special_amount >= 100:
                p1_special_amount = 100
        elif p1_attack_collide > 0:
            p1_attack_collide = 0
        else:
            p2_health -= 0

        special_damage = p2_hit(fire_bender_rect, p1_special_rect_list)
        if special_damage and p1_special_collide == 0:
            p1_special_collide += 1
            p2_health -= p1_second_damage
            if not p1_burning_mode:
                p1_special_amount += second_special_amount_add
            if p1_special_amount >= 100:
                p1_special_amount = 100
        elif p1_special_collide > 0:
            p1_special_collide = 0
        else:
            p2_health -= 0

    if player2:
        damage = p2_hit(blue_ghost_rect, p2_attack_rect_list)
        if damage and p2_attack_collide == 0:
            p2_attack_collide += 1
            p1_health -= p2_basic_damage
            if not p2_burning_mode:
                p2_special_amount += basic_special_amount_add
            if p2_special_amount >= 100:
                p2_special_amount = 100
        elif p2_attack_collide > 0:
            p2_attack_collide = 0
        else:
            p1_health -= 0

        special_damage = p2_hit(blue_ghost_rect, p2_special_rect_list)
        if special_damage and p2_special_collide == 0:
            p2_special_collide += 1
            p1_health -= p2_second_damage
            if not p2_burning_mode:
                p2_special_amount += second_special_amount_add
            if p2_special_amount >= 100:
                p2_special_amount = 100
        elif p2_special_collide > 0:
            p2_special_collide = 0
        else:
            p1_health -= 0
       
    # Printed on screen, health and time
    p1_health_bar(p1_health)
    p2_health_bar(p2_health)
    timer(time, start_time)
    p1_special_bar(p1_special_amount, player_1)
    p2_special_bar(p2_special_amount, player_2)

    # End of game conditions
    if p1_health <=0:
        game_end_score = True
        p1_count_up = 0
        p2_count_up = 0
        p1_special_amount = 0
        p2_special_amount = 0
        blue_ghost_rect.centerx = p1_start_x
        fire_bender_rect.centerx = p2_start_x
    if p2_health <= 0:
        game_end_score = True
        p1_count_up = 0
        p2_count_up = 0
        p1_special_amount = 0
        p2_special_amount = 0
        blue_ghost_rect.centerx = p1_start_x
        fire_bender_rect.centerx = p2_start_x
    if p1_health <= 0 and p2_health <= 0:
        game_end_score = True
        p1_count_up = 0
        p2_count_up = 0
        p1_special_amount = 0
        p2_special_amount = 0
        blue_ghost_rect.centerx = p1_start_x
        fire_bender_rect.centerx = p2_start_x
    if game_time <= 0:
        game_end_score = True
        p1_count_up = 0
        p2_count_up = 0
        p1_special_amount = 0
        p2_special_amount = 0
        blue_ghost_rect.centerx = p1_start_x
        fire_bender_rect.centerx = p2_start_x

    pygame.display.update()

    # FPS
    clock.tick(120)

pygame.display.quit()
quit()