import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 700
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
pygame.display.set_caption("Snake By Silvano A Onyango")

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
grass = (0, 153, 0)
black = (0, 0, 0)
white = (255, 255, 255)
sky_blue = (51, 153, 255)

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 20)

def le_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def your_score(score, colour, width, height):
    value = score_font.render("Your score: " + str(score), True, colour)
    dis.blit(value, [width, height])

def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [display_width/2.5, display_height/2])

def menu(msg, colour, width, height):
    mesg = font_style.render(msg, True, colour)
    dis.blit(mesg, [width, height])

def game_loop():

    game_over = False
    game_close = False
    menu_screen = True
    wall_choice = True

    up_down = display_height / 2
    left_right = display_width / 2

    up_down_change = 0
    left_right_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, display_height - snake_block) / 10) * 10

    snake_direction = 0

    

    while not game_over:

        while wall_choice == True:

            dis.fill(sky_blue)
            menu("Welcome to Snake", black, display_width/3, display_height/4)
            menu("A - WALLS   B - NO WALLS", black, display_width/4, display_height/2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        walls = True
                        wall_choice = False
                        menu_screen = True
                        game_over = False
                        game_close = False
                    if event.key == pygame.K_b:
                        walls = False
                        wall_choice = False
                        menu_screen = True
                        game_over = False
                        game_close = False

        while menu_screen == True:

            dis.fill(sky_blue)
            menu("Choose difficulty", black, display_width/3, display_height/4)
            menu("A - EASY  B - MEDIUM  C - HARD", black, display_width/4, display_height/2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        snake_speed = 10
                        menu_screen = False
                        game_over = False
                        game_close = False
                    if event.key == pygame.K_b:
                        snake_speed = 30
                        menu_screen = False
                        game_over = False
                        game_close = False
                    if event.key == pygame.K_c:
                        snake_speed = 50
                        menu_screen = False
                        game_over = False
                        game_close = False

        while game_close == True:
            dis.fill(black)
            message("GAME OVER!!", red)
            menu("Q - QUIT  C - PLAY AGAIN", red, display_width/3.5, display_height/1.5)
            your_score(length_of_snake - 1, red, display_width/2.5, display_height/4)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and snake_direction != 2:
                    left_right_change = -snake_block
                    up_down_change = 0
                    snake_direction = 1
                if (event.key == pygame.K_RIGHT) and snake_direction != 1:
                    left_right_change = snake_block
                    up_down_change = 0
                    snake_direction = 2
                if (event.key == pygame.K_UP) and snake_direction != 4:
                    left_right_change = 0
                    up_down_change = -snake_block
                    snake_direction = 3
                if (event.key == pygame.K_DOWN) and snake_direction != 3:
                    left_right_change = 0
                    up_down_change = snake_block
                    snake_direction = 4
        
        if walls == True:
            if up_down >= display_height or up_down < 0 or left_right >= display_width or left_right < 0:
                game_close = True
        
        if walls == False:
            if up_down >= display_height:
                up_down = 0
            if up_down < 0:
                up_down = display_height
            if left_right >= display_width:
                left_right = 0
            if left_right < 0:
                left_right = display_width

        up_down += up_down_change 
        left_right += left_right_change

        dis.fill(grass)
        
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(left_right)
        snake_head.append(up_down)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        le_snake(snake_block, snake_list)
        your_score(length_of_snake - 1, blue, 0, 0)

        pygame.display.update()

        if up_down == foody and left_right == foodx:
            foodx = round(random.randrange(0, display_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, display_height - snake_block) / 10) * 10
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()