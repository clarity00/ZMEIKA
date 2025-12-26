import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
SPEED = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
DARK_GREEN = (0, 150, 0)

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("comicsansms", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Score: " + str(score), True, BLUE)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
    dis.blit(mesg, text_rect)

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 2

    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            dis.fill(BLACK)
            message("You Lost! Press C to Play Again or Q to Quit", RED)
            your_score(Length_of_snake - 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change != BLOCK_SIZE:
                        x1_change = -BLOCK_SIZE
                        y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change != -BLOCK_SIZE:
                        x1_change = BLOCK_SIZE
                        y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change != BLOCK_SIZE:
                        y1_change = -BLOCK_SIZE
                        x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change != -BLOCK_SIZE:
                        y1_change = BLOCK_SIZE
                        x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)
        
        pygame.draw.rect(dis, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if x1_change != 0 or y1_change != 0:
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

        for x in snake_List[:-1]:
            pygame.draw.rect(dis, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])
        
        head = snake_List[-1] 
        pygame.draw.rect(dis, DARK_GREEN, [head[0], head[1], BLOCK_SIZE, BLOCK_SIZE])

        your_score(Length_of_snake - 2)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            Length_of_snake += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

gameLoop()