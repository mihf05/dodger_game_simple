# dodger_game_simple
Here is a detailed breakdown of the code for the Dodger Game implemented using Pygame:

### Initial Setup

1. **Import Libraries**:
   ```python
   import pygame
   import random
   import sys
   ```
   These imports bring in the necessary libraries. `pygame` is used for game development, `random` is used for random number generation, and `sys` is used for system-specific parameters and functions.

2. **Initialize Pygame**:
   ```python
   pygame.init()
   ```
   This initializes all the Pygame modules.

### Screen Configuration

3. **Screen Dimensions**:
   ```python
   SCREEN_WIDTH = 800
   SCREEN_HEIGHT = 600
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   pygame.display.set_caption("Dodger Game")
   ```
   This sets up the screen size (800x600) and gives the game window a title.

### Color Definitions

4. **Colors**:
   ```python
   WHITE = (255, 255, 255)
   BLACK = (0, 0, 0)
   RED = (255, 0, 0)
   ```
   Defines colors in RGB format for use in the game.

### Player Configuration

5. **Player Settings**:
   ```python
   player_size = 50
   player_x = SCREEN_WIDTH // 2 - player_size // 2
   player_y = SCREEN_HEIGHT - player_size - 20
   player_speed = 5
   ```
   Sets the player size, initial position (centered horizontally near the bottom), and movement speed.

### Obstacle Configuration

6. **Obstacle Settings**:
   ```python
   obstacle_width = 100
   obstacle_height = 20
   obstacle_speed = 5
   obstacle_color = RED
   obstacles = []
   ```
   Sets the obstacle size, speed, color, and initializes an empty list to hold obstacles.

### Score Configuration

7. **Score and Font**:
   ```python
   score = 0
   font = pygame.font.Font(None, 36)
   ```
   Initializes the score and sets the font for rendering text.

### Main Functions

8. **Draw Text**:
   ```python
   def draw_text(text, font, color, x, y):
       text_surface = font.render(text, True, color)
       text_rect = text_surface.get_rect()
       text_rect.center = (x, y)
       screen.blit(text_surface, text_rect)
   ```
   Renders and displays text at specified coordinates.

9. **Draw Player**:
   ```python
   def draw_player():
       pygame.draw.rect(screen, BLACK, [player_x, player_y, player_size, player_size])
   ```
   Draws the player as a black rectangle.

10. **Draw Obstacles**:
    ```python
    def draw_obstacles():
        for obstacle in obstacles:
            pygame.draw.rect(screen, obstacle_color, obstacle)
    ```
    Draws each obstacle in the obstacles list.

11. **Generate Obstacle**:
    ```python
    def generate_obstacle():
        x = random.randint(0, SCREEN_WIDTH - obstacle_width)
        y = -obstacle_height
        obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))
    ```
    Creates a new obstacle at a random horizontal position above the screen and adds it to the obstacles list.

12. **Move Obstacles**:
    ```python
    def move_obstacles():
        global obstacle_speed
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > SCREEN_HEIGHT:
                obstacles.remove(obstacle)
                increase_difficulty()
    ```
    Moves obstacles downward, removes them if they move off-screen, and increases difficulty periodically.

13. **Check Collision**:
    ```python
    def check_collision():
        for obstacle in obstacles:
            if obstacle.colliderect(pygame.Rect(player_x, player_y, player_size, player_size)):
                return True
        return False
    ```
    Checks if any obstacle collides with the player.

14. **Show Instructions**:
    ```python
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
            draw_text(line, font, BLACK, SCREEN_WIDTH // 2, y_offset)
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
    ```
    Displays the instructions on the screen and waits for a key press to start the game.

15. **Game Over**:
    ```python
    def game_over():
        screen.fill(WHITE)
        draw_text("Game Over", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text(f"Final Score: {score}", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        draw_text("Press any key to restart", font, BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    return
    ```
    Displays a game over screen with the final score and waits for a key press to restart the game.

16. **Increase Difficulty**:
    ```python
    def increase_difficulty():
        global obstacle_speed
        if score % 1000 == 0:
            obstacle_speed += 1
    ```
    Increases the speed of obstacles as the score increases, making the game more challenging.

### Game Loop

17. **Main Game Loop**:
    ```python
    show_instructions()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed

        screen.fill(WHITE)

        draw_player()
        move_obstacles()
        draw_obstacles()
        draw_text(f"Score: {score}", font, BLACK, 100, 50)

        if random.randint(1, 100) < 2:
            generate_obstacle()

        if check_collision():
            game_over()
            # Reset game
            obstacles.clear()
            score = 0
            obstacle_speed = 5
            player_x = SCREEN_WIDTH // 2 - player_size // 2
            show_instructions()

        score += 1
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
    ```
    - **Initialization**: Displays instructions before starting the game.
    - **Event Handling**: Handles quitting the game and player movement.
    - **Game Mechanics**: Updates the game state, including player and obstacle movements, drawing elements on the screen, and checking for collisions.
    - **Score and Difficulty**: Updates the score and adjusts obstacle speed over time.
    - **Game Over Handling**: Displays the game over screen, resets game variables, and allows for restarting the game.

### Summary
- **Screen Setup**: Initializes the display window and its properties.
- **Player and Obstacle Configuration**: Defines player and obstacle properties.
- **Game Logic**: Handles rendering, movement, collision detection, scoring, and difficulty adjustments.
- **User Interaction**: Displays instructions and handles user inputs for game control and restarting.

This game structure ensures a clear flow from initialization to gameplay and end-of-game conditions, making it both modular and easy to understand.
