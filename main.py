import pygame



# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 400
screen_height = 400

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the size of the squares
square_size = 50

# Set the colors of the squares
light_color = (255, 255, 255)
dark_color = (128, 128, 128)

# Draw the squares
for row in range(8):
    for col in range(8):
        x = col * square_size
        y = row * square_size
        if (row + col) % 2 == 0:
            color = light_color
        else:
            color = dark_color
        pygame.draw.rect(screen, color, pygame.Rect(x, y, square_size, square_size))

# Update the screen
pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()