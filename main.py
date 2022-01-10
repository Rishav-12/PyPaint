# TODO: implement a grid-based approach


import pygame

pygame.init()

win = pygame.display.set_mode((400, 400))
win.fill((255, 255, 255))

pygame.display.set_caption("PyPaint")

COLORS = ["red", "green", "blue", "yellow", "purple", "black", "white"]
drawing_color = COLORS[5]
SIZE = 20
BUTTONS = []

clock = pygame.time.Clock()
running = True
drawing = False

for i, color in enumerate(COLORS):
    BUTTONS.append({ 'obj' : pygame.draw.rect(win, color, (4*(i+1)+SIZE*i, 375, 20, 20)), 'color' : color})


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        for button in BUTTONS:
          if button['obj'].collidepoint(event.pos):
            drawing_color = button['color']
        drawing = True
    if event.type == pygame.MOUSEBUTTONUP:
      drawing = False

  if drawing:
    x, y = pygame.mouse.get_pos()
    pygame.draw.circle(win, drawing_color, (x, y), 10)

  clock.tick(30)
  pygame.display.update()


pygame.quit()