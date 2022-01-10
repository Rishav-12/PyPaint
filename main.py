# TODO: implement a grid-based approach

import pygame

pygame.init()

class GridSquare:
  def __init__(self, left, top, width, height):
    self.rect = pygame.Rect(left, top, width, height)
    self.color = "white"
  def draw(self, window):
    pygame.draw.rect(window, self.color, self.rect)

class ColorButton:
  def __init__(self, left, top, width, height, color):
    self.rect = pygame.Rect(left, top, width, height)
    self.color = color
  def draw(self, window):
    pygame.draw.rect(window, self.color, self.rect)

ROWS = 45
COLS = 50
SQUARE_SIZE = 8
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill("white")

pygame.display.set_caption("PyPaint")

COLORS = ["red", "green", "blue", "yellow", "purple", "black"]
drawing_color = COLORS[5]

grid_squares = []
buttons = []

clear = pygame.image.load('eraser.png')

for i in range(COLS):
  for j in range(ROWS):
    square = GridSquare(i*SQUARE_SIZE, j*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    grid_squares.append(square)

for i, color in enumerate(COLORS):
    button = ColorButton(4*i+20*(i+1), 375, 20, 20, color)
    buttons.append(button)

clock = pygame.time.Clock()
running = True
drawing = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      drawing = True
    if event.type == pygame.MOUSEBUTTONUP:
      drawing = False
  
  # Render the drawing grid
  for square in grid_squares:
    square.draw(win)
    if drawing and square.rect.collidepoint(pygame.mouse.get_pos()):
      square.color = drawing_color
  
  # Render the color buttons
  for button in buttons:
    button.draw(win)
    if pygame.mouse.get_pressed()[0] and button.rect.collidepoint(pygame.mouse.get_pos()):
      drawing_color = button.color
  
  # Render the clear button
  clear_rect = clear.get_rect(topleft = (188, 375))
  win.blit(clear, clear_rect)
  if pygame.mouse.get_pressed()[0] and clear_rect.collidepoint(pygame.mouse.get_pos()):
    drawing_color = "white"

  clock.tick(30)
  pygame.display.update()


pygame.quit()