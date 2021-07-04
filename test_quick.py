import time
import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

element_numbers = [500, 1000, 2000, 4000, 8000, 16000, 32000]
test_iteration = []
array = []
mean = [0, 0, 0, 0, 0, 0, 0]
iteration = 10


def generate_arr(ELEMENT_NUMBER):
    global array
    array = []
    for numb in range(ELEMENT_NUMBER):
        array.append(random.randint(100, 400))


def quick_sort(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(array, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def partition(arr, l, h):
    i = (l - 1)
    x = array[h]

    for j in range(l, h):
        if array[j] <= x:
            # increment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[h] = array[h], array[i + 1]
    return (i + 1)


for j in range(iteration):
    run_time = []
    for i in element_numbers:
        generate_arr(i)
        start_time = time.time()
        quick_sort(array, 0, 9)
        run_time.append(time.time() - start_time)
    test_iteration.append(run_time)

t = PrettyTable(['500', '1000', '2000', '4000', '8000', '16000', '32000'])

for val in test_iteration:
    t.add_row(val)

for i in range(7):
    mean[i] = test_iteration[0][i] + test_iteration[1][i] + test_iteration[2][i] + test_iteration[3][i] + \
              test_iteration[4][i] + test_iteration[5][i] + test_iteration[6][i] + test_iteration[7][i] + \
              test_iteration[8][i] + test_iteration[9][i]
    mean[i] = mean[i] / iteration

print(t)
print('Mean values: ', mean)

x = element_numbers
y = mean

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.xlim(500, 32000)
plt.ylim(0, 60)

plt.xlabel('Element Number')
plt.ylabel('Time')

plt.title('Selection Sort Experimental')

plt.show()
