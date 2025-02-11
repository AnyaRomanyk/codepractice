array1, array2 = [], []

with open('input_1.txt') as file:
    for line in file:
        numbers = line.split()
        array1.append(int(numbers[0]))
        array2.append(int(numbers[1]))

def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

selection_sort(array1)
selection_sort(array2)

result_sum = 0
for i in range(len(array1)):
    if array1[i] >= array2[i]:
        result_sum += array1[i] - array2[i]
    else:
        result_sum += array2[i] - array1[i]

print("Count of all distance:", result_sum)
