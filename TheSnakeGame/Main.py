import pygame
import sys
import random
from Constants import*
from Score import Score
from Snake import Snake


pygame.init()

# Direction (initially right)
direction = (1, 0)
next_direction = (1, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game over flag
game_over = False

score = Score(screen)

snake = Snake()

# prevent the snake from going backward
def is_direction_valid(dir, current_dir):
    return (dir[0] * -1, dir[1] * -1) != current_dir

# Main loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            if event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            if event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            if event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))

    # Check for collisions
    if snake.check_food_collision(food):
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        score.increase()
        snake.move(grow=True)
    else:
        snake.move(grow=False)

    if snake.check_collision():
        game_over = True

    # Clear the screen
    screen.fill(BLACK)

    # Draw the food
    pygame.draw.rect(
        screen, GREEN, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Draw the snake
    for segment in snake.body:
        pygame.draw.rect(
            screen,
            WHITE,
            (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
        )

    # Display the score
    score.display()

    # Update the screen
    pygame.display.update()

    # Delay to control game speed
    pygame.time.Clock().tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
sys.exit()