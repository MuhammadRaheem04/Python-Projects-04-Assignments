
import pygame
import sys

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20
FPS = 60

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Erase Canvas")
clock = pygame.time.Clock()

# Create the grid of blue cells
cells = []
for row in range(0, WINDOW_HEIGHT, CELL_SIZE):
    for col in range(0, WINDOW_WIDTH, CELL_SIZE):
        cell_rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        cells.append({"rect": cell_rect, "color": BLUE})

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser = pygame.Rect(mouse_x, mouse_y, ERASER_SIZE, ERASER_SIZE)

    # Draw and erase logic
    for cell in cells:
        if eraser.colliderect(cell["rect"]):
            cell["color"] = WHITE
        pygame.draw.rect(screen, cell["color"], cell["rect"])

    # Draw eraser (on top)
    pygame.draw.rect(screen, PINK, eraser)

    # Refresh screen
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
