import time
import random
from prettytable import PrettyTable
import matplotlib.pyplot as plt

element_numbers = [500, 1000, 2000, 4000, 8000, 16000, 32000]
array = []
mean_quick = [0, 0, 0, 0, 0, 0, 0]
mean_heap = [0, 0, 0, 0, 0, 0, 0]
mean_selection = [0, 0, 0, 0, 0, 0, 0]
iteration = 10

def generate_arr(ELEMENT_NUMBER):
    global array
    array = []
    for numb in range(ELEMENT_NUMBER):
        array.append(random.randint(100, 400))


def selection_sort(arr, ELEMENT_NUMBER):
    for i in range(ELEMENT_NUMBER):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

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

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)


def heapify(arr, root, size):
    left = root * 2 + 1
    right = root * 2 + 2
    largest = root

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        heapify(arr, largest, size)

test_iteration_heap = []
for j in range(iteration):
    run_time = []
    for i in element_numbers:
        generate_arr(i)
        start_time = time.time()
        heap_sort(array)
        run_time.append(time.time() - start_time)
    test_iteration_heap.append(run_time)

test_iteration_quick = []
for j in range(iteration):
    run_time = []
    for i in element_numbers:
        generate_arr(i)
        start_time = time.time()
        quick_sort(array, 0, i-1)
        run_time.append(time.time() - start_time)
    test_iteration_quick.append(run_time)

test_iteration_selection = []
for j in range(iteration):
    run_time = []
    for i in element_numbers:
        generate_arr(i)
        start_time = time.time()
        selection_sort(array, i)
        run_time.append(time.time() - start_time)
    test_iteration_selection.append(run_time)

t = PrettyTable(['500', '1000', '2000', '4000', '8000', '16000', '32000'])

for val in test_iteration:
    t.add_row(val)

for i in range(7):
  for j in range(10):
    mean_selection[i] = test_iteration_selection[j][i]
  mean_selection[i] = mean_selection[i] / iteration

for i in range(7):
  for j in range(10):
    mean_quick[i] = test_iteration_quick[j][i]
  mean_quick[i] = mean_quick[i] / iteration

for i in range(7):
  for j in range(10):
    mean_heap[i] = test_iteration_heap[j][i]
  mean_heap[i] = mean_heap[i] / iteration

print('Mean values quick sort: ', mean_quick)

print('Mean values heap sort: ', mean_heap)

print('Mean values selection sort: ', mean_selection)

print(t)

x = element_numbers
y1 = mean_heap
y2 = mean_quick
y3 = mean_selection

plt.plot(x, y1, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='orange', markersize=12)

plt.plot(x, y2, color='blue', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='orange', markersize=12)

plt.plot(x, y3, color='red', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='orange', markersize=12)

plt.xlim(500, 32000)
plt.ylim(0, .1)

plt.xlabel('Element Number')
plt.ylabel('Time')

#plt.title('Selection Sort Experimental')
plt.title('Comparison Sort Experimental')

plt.show()

x = element_numbers
y = []

for i in x:
  y.append(i ** 2)

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.xlim(500, 32000)
plt.ylim(0, 1024000000)

plt.xlabel('Element Number')
plt.ylabel('Time')

#plt.title('Selection Sort Experimental')
plt.title('Selection Sort Theoretical')

plt.show()

x = element_numbers
y = []

for i in x:
  y.append(i * i)


print(y)

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.xlim(500, 32000)
plt.ylim(0, 1024000000)

plt.xlabel('Element Number')
plt.ylabel('Time')

plt.title('Quick Sort Theoretical Worst Case')

plt.show()

x = np.linspace(-5,5,100)

x
