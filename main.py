import pygame
import sys
import os
import sys

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return os.path.join(os.path.abspath("."), filename)

# Use:
image = pygame.image.load(resource_path("jack.png")).convert_alpha()

# Init
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jack")

# Load and scale image

jackImage = pygame.transform.scale(image, (100, 100))

# Position and velocity
imageX = 100
imageY = 100
velocityX = 3
velocityY = 3

# Background colors
backgroundColors = [
    (1, 255, 247),
    (79, 253, 102),
    (246, 255, 0)
]
currentColorIndex = 0
currentColor = backgroundColors[currentColorIndex]

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                currentColorIndex = (currentColorIndex + 1) % len(backgroundColors)
                currentColor = backgroundColors[currentColorIndex]

    # Update position
    imageX += velocityX
    imageY += velocityY

    # Bounce off edges
    if imageX <= 0 or imageX >= 800 - 100:
        velocityX *= -1
    if imageY <= 0 or imageY >= 600 - 100:
        velocityY *= -1

    # Draw
    screen.fill(currentColor)
    screen.blit(jackImage, (imageX, imageY))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
