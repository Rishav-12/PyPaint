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


WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((255, 255, 255))

pygame.display.set_caption("PyPaint")

COLORS = ["red", "green", "blue", "yellow", "purple", "black", "white"]
drawing_color = COLORS[5]
buttons = []
grid_squares = []
rows = 45
cols = 50
square_size = 8

for i in range(cols):
  for j in range(rows):
    square = GridSquare(i*square_size, j*square_size, square_size, square_size)
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
  
  for square in grid_squares:
    square.draw(win)
    if drawing and square.rect.collidepoint(pygame.mouse.get_pos()):
      square.color = drawing_color
  
  for button in buttons:
    button.draw(win)
    if button.rect.collidepoint(pygame.mouse.get_pos()):
      drawing_color = button.color

  clock.tick(30)
  pygame.display.update()


pygame.quit()