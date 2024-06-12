import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dodger Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 20
player_speed = 5

# Obstacles
obstacle_width = 100
obstacle_height = 20
obstacle_speed = 5
obstacle_color = RED
obstacle_gap = 200
obstacles = []

# Score
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_player():
    pygame.draw.rect(screen, BLACK, [player_x, player_y, player_size, player_size])

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle)

def generate_obstacle():
    x = random.randint(0, SCREEN_WIDTH - obstacle_width)
    y = -obstacle_height
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

def move_obstacles():
    for obstacle in obstacles:
        obstacle.y += obstacle_speed
        if obstacle.y > SCREEN_HEIGHT:
            obstacles.remove(obstacle)

def check_collision():
    for obstacle in obstacles:
        if obstacle.colliderect(pygame.Rect(player_x, player_y, player_size, player_size)):
            return True
    return False

def show_instructions():
    instructions = [
        "Welcome to the Dodger Game!",
        "Instructions:",
        "1. Use the LEFT and RIGHT arrow keys to move.",
        "2. Avoid the falling obstacles.",
        "3. Survive as long as you can to score points.",
        "Press any key to start..."
    ]
    y_offset = 100
    for line in instructions:
        draw_text(line, font, WHITE, SCREEN_WIDTH // 2, y_offset)
        y_offset += 40
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Show instructions before starting the game
show_instructions()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    screen.fill(WHITE)

    draw_player()
    move_obstacles()
    draw_obstacles()
    draw_text(f"Score: {score}", font, BLACK, 100, 50)

    if random.randint(1, 100) < 2:
        generate_obstacle()

    if check_collision():
        running = False

    score += 1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
