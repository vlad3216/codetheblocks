import math
from ctb import place
RADIUS = int(input('Введите значение радиуса окружности: ')) #Circle
SEGMENTS = 50
for position in range(SEGMENTS):
  radians = 2 * math.pi * position / SEGMENTS
  x = RADIUS * math.cos(radians)
  y = RADIUS * math.sin(radians)
  place(x, y, 0,)
