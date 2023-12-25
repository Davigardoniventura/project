import pygame
from pygame.locals import *
import random

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10

def collision(pos1, pos2):
    return pos1 == pos2

def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else: 
        return True
    
def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0] - PIXEL_SIZE)
    y = random.randint(0, WINDOW_SIZE[1] - PIXEL_SIZE)
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE

def show_start_message():
    message = "Pressione qualquer botão para começar"
    message_text = font.render(message, True, (255, 255, 255))
    
    while True:
        pygame.time.Clock().tick(5)
        screen.fill((0, 0, 0))
        screen.blit(message_text, (WINDOW_SIZE[0] // 2 - message_text.get_width() // 2, WINDOW_SIZE[1] // 2 - message_text.get_height() // 2))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                return

def show_game_over_message():
    score_text = font.render(f"Pontuação: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WINDOW_SIZE[0] // 2 - score_text.get_width() // 2, WINDOW_SIZE[1] // 2 - score_text.get_height() // 2 - 50))
    
    game_over_message = "Pressione qualquer botão para recomeçar"
    game_over_text = font.render(game_over_message, True, (255, 255, 255))
    screen.blit(game_over_text, (WINDOW_SIZE[0] // 2 - game_over_text.get_width() // 2, WINDOW_SIZE[1] // 2 + 20))
    
    pygame.display.update()
    
    while True:
        pygame.time.Clock().tick(5)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                return

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE))
pygame.display.set_caption("Snake")

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direction = K_a

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()

font = pygame.font.Font(None, 36) 
score = 0

def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    global score
    
    show_game_over_message()
    
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_a
    apple_pos = random_on_grid()
    score = 0 

show_start_message()

while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_w, K_s, K_a, K_d]:
                snake_direction = event.key
                
    screen.blit(apple_surface, apple_pos)
    
    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()
        score += 1 

    for pos in snake_pos:
        screen.blit(snake_surface, pos)
        
    for i in range(len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i - 1]
        
    if off_limits(snake_pos[0]):
        restart_game()
        
    if snake_direction == K_w:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_s:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_a:    
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_d:   
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WINDOW_SIZE[0] - score_text.get_width() - 10, 10))
    
    pygame.display.update()
