from ctb import place
import math
SIZE = int(input('Введите размер: ')) #CUBE
for int in range(SIZE):
  x = SIZE
  y = int
  z = SIZE-1
  place(y, 0, 0)
  place(0, y, 0)
  place(0, 0, y)
  place(x, 0,y)
  place(0, x, y)
  place(0, y, z)
  place(x, y, 0)
  place(x, x, y)
  place(x, y, z)
  place(y, x, z)
  place(y, x, 0)
  place(y, 0 ,z)
