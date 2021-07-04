import pygame
import random

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

ELEMENT_NUMBER = 10

pygame.font.init()

screen = pygame.display.set_mode((900, 650))

pygame.display.set_caption("SORTING VISUALISER")
run = True

width = 900
length = 600
array = [0] * ELEMENT_NUMBER
arr_clr = [(0, 255, 0)] * ELEMENT_NUMBER
# White sorted, blue unsorted, red moved, green selected
clr = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 255)]

counter = 0


def generate_arr():
    decision = input('Press R to create random elements and press E to enter 10 numbers: ')
    if decision == 'R':
        for i in range(1, ELEMENT_NUMBER):
            arr_clr[i] = clr[0]
            array[i] = random.randrange(100, 400)

    elif decision == 'E':
        for i in range(1, ELEMENT_NUMBER):
            arr_clr[i] = clr[0]
            array[i] = int(input('Enter number: '))


def refill():
    screen.fill((0, 0, 0))
    draw()
    pygame.display.update()
    pygame.time.delay(30)


def selection_sort(arr):
    global counter
    # if counter < ELEMENT_NUMBER:
    for i in range(ELEMENT_NUMBER):
        print(i, array)
        min_idx = i
        arr_clr[i] = clr[1]
        refill()
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            arr_clr[min_idx] = clr[0]
            arr_clr[j] = clr[2]
            arr_clr[i] = clr[3]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        refill()

        counter += 1


def draw():
    if ELEMENT_NUMBER > width:
        element_width = int(ELEMENT_NUMBER / width)
    else:
        element_width = int(width / ELEMENT_NUMBER)
    for i in range(1, ELEMENT_NUMBER):
        pygame.draw.line(screen, arr_clr[i], ((element_width * i), length),
                         ((element_width * i),
                          array[i]),
                         element_width)


generate_arr()


def run_code(element_number):
    global run
    global ELEMENT_NUMBER
    ELEMENT_NUMBER = element_number
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    selection_sort(array)
        draw()
        pygame.display.update()

    pygame.quit()


run_code(10)
print(len(array))
