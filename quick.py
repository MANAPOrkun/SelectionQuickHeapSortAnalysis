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


def quicksort(arr, l, r):
    global counter
    global step
    if l < r:
        pi = partition(arr, l, r)
        print(arr)
        if counter == step:
            quicksort(arr, l, pi - 1)
            counter += 1

            refill()
            for i in range(0, pi + 1):
                arr_clr[i] = clr[3]
            quicksort(arr, pi + 1, r)


def partition(arr, low, high):
    global counter
    pygame.event.pump()
    pivot = arr[high]
    arr_clr[high] = clr[2]
    i = low - 1

    for j in range(low, high):
        # if low < counter < high:
        arr_clr[j] = clr[1]
        refill()
        arr_clr[high] = clr[2]
        arr_clr[j] = clr[0]
        arr_clr[i] = clr[0]
        if arr[j] < pivot:
            i = i + 1
            arr_clr[i] = clr[1]
            arr[i], arr[j] = arr[j], arr[i]
    refill()
    arr_clr[i] = clr[0]
    arr_clr[high] = clr[0]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


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
                quicksort(array, 1, len(array) - 1)
                step += 1
    draw()
    pygame.display.update()

pygame.quit()
