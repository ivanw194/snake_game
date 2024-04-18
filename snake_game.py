import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define constants
block_size = 20
speed = 10

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]  # Initial segments of the snake
        self.direction = "RIGHT"

    def move(self):
        head = list(self.body[0])  # Current head position
        if self.direction == "RIGHT":
            head[0] += block_size
        elif self.direction == "LEFT":
            head[0] -= block_size
        elif self.direction == "UP":
            head[1] -= block_size
        elif self.direction == "DOWN":
            head[1] += block_size

        self.body.insert(0, tuple(head))  # Insert new head position
        self.body.pop()  # Remove the tail

    def change_direction(self, direction):
        if direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction

    def grow(self):
        tail = list(self.body[-1])
        if self.direction == "RIGHT":
            tail[0] -= block_size
        elif self.direction == "LEFT":
            tail[0] += block_size
        elif self.direction == "UP":
            tail[1] += block_size
        elif self.direction == "DOWN":
            tail[1] -= block_size

        self.body.append(tuple(tail))

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, white, pygame.Rect(segment[0], segment[1], block_size, block_size))

class Food:
    def __init__(self):
        self.position = (random.randrange(1, width//block_size) * block_size,
                         random.randrange(1, height//block_size) * block_size)

    def draw(self):
        pygame.draw.rect(screen, red, pygame.Rect(self.position[0], self.position[1], block_size, block_size))

def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")

        snake.move()

        # Check for collision with food
        if snake.body[0] == food.position:
            snake.grow()
            food = Food()

        # Check for collision with walls
        if (snake.body[0][0] >= width or snake.body[0][0] < 0 or
            snake.body[0][1] >= height or snake.body[0][1] < 0):
            game_over = True

        # Check for collision with itself
        if snake.body[0] in snake.body[1:]:
            game_over = True

        # Clear the screen
        screen.fill(black)

        # Draw the snake and food
        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()

if __name__ == "__main__":
    main()