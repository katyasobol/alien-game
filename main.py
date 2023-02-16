import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the snake and food
block_size = 10
clock = pygame.time.Clock()

# Define the font
font = pygame.font.SysFont(None, 25)

# Define a function to display text on the screen


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_width/6, screen_height/2])

# Define the game loop


def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    # Create the food
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(
        0, screen_height - block_size) / 10.0) * 10.0

    # Set up the snake
    snake_List = []
    Length_of_snake = 1

    # Main game loop
    while not game_over:

        while game_close == True:
            screen.fill(white)
            message_to_screen("You Lost! Press Q-Quit or C-Play Again", red)
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
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for collisions with the walls
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Draw the snake and food on the screen
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
