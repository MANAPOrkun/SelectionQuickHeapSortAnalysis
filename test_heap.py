import random
import time

from prettytable import PrettyTable
import matplotlib.pyplot as plt

element_numbers = [500, 1000, 2000, 4000, 8000, 16000, 32000]
array = []
mean_heap = [0, 0, 0, 0, 0, 0, 0]
iteration = 10


def generate_arr(ELEMENT_NUMBER):
    global array
    array = []
    for numb in range(ELEMENT_NUMBER):
        array.append(random.randint(100, 400))


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

t = PrettyTable(['500', '1000', '2000', '4000', '8000', '16000', '32000'])

for val in test_iteration_heap:
    t.add_row(val)

for i in range(7):
    for j in range(10):
        mean_heap[i] = test_iteration_heap[j][i]
    mean_heap[i] = mean_heap[i] / iteration

print('Mean values heap sort: ', mean_heap)

print(t)

x = element_numbers
y = mean_heap

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='orange', markersize=12)

plt.xlim(500, 32000)
plt.ylim(0, .1)

plt.xlabel('Element Number')
plt.ylabel('Time')

plt.title('Heap Sort Experimental')

plt.show()
