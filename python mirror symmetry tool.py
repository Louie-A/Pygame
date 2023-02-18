import pygame
import numpy as np

# Define screen size and line color
SCREEN_SIZE = (800, 800)
LINE_COLOR = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# Define a function to draw a line and its symmetrical counterpart
def draw_symmetrical_line(start_pos, end_pos, axis):
    # Draw original line
    pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos)

    # Calculate symmetrical endpoint based on axis of symmetry
    if axis == 'vertical':
        symmetrical_end_pos = (SCREEN_SIZE[0] - end_pos[0], end_pos[1])
    elif axis == 'horizontal':
        symmetrical_end_pos = (end_pos[0], SCREEN_SIZE[1] - end_pos[1])
    elif axis == 'diagonal':
        symmetrical_end_pos = (SCREEN_SIZE[0] - end_pos[0], SCREEN_SIZE[1] - end_pos[1])
    else:
        return

    # Draw symmetrical line
    pygame.draw.line(screen, LINE_COLOR, start_pos, symmetrical_end_pos)

# Define a function to draw a symmetrical line based on mouse movement
def draw_symmetrical_lines(mouse_pos, prev_mouse_pos, axis):
    # Calculate line start and end points
    start_pos = prev_mouse_pos
    end_pos = mouse_pos

    # Draw symmetrical line
    draw_symmetrical_line(start_pos, end_pos, axis)

# Main game loop
prev_mouse_pos = None
while True:
    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get current mouse position
    mouse_pos = np.array(pygame.mouse.get_pos())

    # Draw symmetrical lines if mouse button is down
    if pygame.mouse.get_pressed()[0]:
        if prev_mouse_pos is not None:
            draw_symmetrical_lines(mouse_pos, prev_mouse_pos, 'vertical')
            draw_symmetrical_lines(mouse_pos, prev_mouse_pos, 'horizontal')
            draw_symmetrical_lines(mouse_pos, prev_mouse_pos, 'diagonal')
        prev_mouse_pos = mouse_pos
    else:
        prev_mouse_pos = None

    # Update display
    pygame.display.flip()
