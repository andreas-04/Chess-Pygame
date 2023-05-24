import pygame

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Chess Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)

# Define other constants for the board and pieces
square_size = window_width // 8

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Get the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Calculate the clicked square coordinates
                col = mouse_x // square_size
                row = mouse_y // square_size

                # Convert the coordinates to chess notation
                letter = chr(col + 97)
                number = 8 - row
                square = f"{letter}{number}"

                # Print the clicked square coordinates
                print("Clicked square:", square)

    # Clear the window
    window.fill(WHITE)

    # Draw the board
    for row in range(8):
        for col in range(8):
            square_color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
            pygame.draw.rect(window, square_color, (col * square_size, row * square_size, square_size, square_size))

    # Draw the pieces

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()