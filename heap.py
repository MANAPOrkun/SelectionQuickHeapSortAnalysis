import pygame
import random

pygame.font.init()

screen = pygame.display.set_mode((900, 650))

pygame.display.set_caption("SORTING VISUALISER")
run = True

width = 900
length = 600
array = [0] * 10
arr_clr = [(0, 255, 0)] * 10
clr = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 255)]

counter = 0
step = 0


def generate_arr():
    decision = input('Press R to create random elements and press E to enter 10 numbers: ')
    if decision == 'R':
        for i in range(1, 10):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(100, 400)

    elif decision == 'E':
        for i in range(1, 10):
            arr_clr[i] = clr[0]
            array[i] = int(input('Enter number: '))


def refill():
    screen.fill((0, 0, 0))
    draw()
    pygame.display.update()
    pygame.time.delay(30)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        pygame.event.pump()
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arr_clr[i] = clr[1]
        refill()
        heapify(arr, 0, i)


def heapify(arr, root, size):
    print(array)
    global counter
    left = root * 2 + 1
    right = root * 2 + 2
    largest = root

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        arr_clr[largest] = clr[2]
        arr_clr[root] = clr[2]
        arr[largest], arr[root] = arr[root], arr[largest]
        refill()
        arr_clr[largest] = clr[0]
        arr_clr[root] = clr[0]
        heapify(arr, largest, size)
        refill()




def draw():
    element_width = 70

    for i in range(1, 10):
        pygame.draw.line(screen, arr_clr[i], (80 * i - 3, length),
                         (80 * i - 3,
                          array[i]),
                         element_width)


generate_arr()

while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                heap_sort(array)
                step += 1
    draw()
    pygame.display.update()

pygame.quit()
