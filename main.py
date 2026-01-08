import pygame
import random
import os

pygame.init()

# ---------------- COLORS ----------------
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 155, 0)

# ---------------- SCREEN ----------------
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def gameloop():
    exit_game = False
    game_over = False

    snake_x = 100
    snake_y = 100
    velocity_x = 0
    velocity_y = 0
    snake_size = 20

    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width - 40)
    food_y = random.randint(20, screen_height - 40)

    score = 0
    fps = 60
    speed = 5

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over!", red, 360, 250)
            text_screen("Press ENTER to Restart", black, 300, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = speed
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -speed
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -speed
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = speed
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
                score += 10
                food_x = random.randint(20, screen_width - 40)
                food_y = random.randint(20, screen_height - 40)
                snk_length += 5

            gameWindow.fill(black)
            text_screen(f"Score: {score}", white, 10, 10)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
                game_over = True

            plot_snake(gameWindow, green, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()
