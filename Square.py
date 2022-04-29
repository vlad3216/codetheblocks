SIZE = int(input('Введите размер: '))  # Square
for int in range(SIZE):
    x = SIZE
    y = int
    z = SIZE - 1
    place(y, 0, 0)
    place(0, 0, y)
    place(y, 0, z)
    place(x, 0, y)
