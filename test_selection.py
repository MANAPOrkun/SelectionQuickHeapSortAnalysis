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


def selection_sort(arr, ELEMENT_NUMBER):
    for i in range(ELEMENT_NUMBER):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


for j in range(iteration):
    run_time = []
    for i in element_numbers:
        generate_arr(i)
        start_time = time.time()
        selection_sort(array, i)
        run_time.append(time.time() - start_time)
    test_iteration.append(run_time)

t = PrettyTable(['500', '1000', '2000', '4000', '8000', '16000', '32000'])

for val in test_iteration:
    t.add_row(val)

for i in test_iteration:
    count = 0
    for j in i:
        mean[count] += mean[count] + j
        count += 1

print(t)

for i in range(0, 7):
    mean[i] = mean[i] / iteration

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