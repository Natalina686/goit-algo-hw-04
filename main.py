import random
import timeit

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Timsort
def timsort(arr):
    return sorted(arr)

# Генерація випадкового масиву
def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

# Тестування часу на виконання
def test_sorting_algorithms(array_size):
    random_array = generate_random_array(array_size)

    # Тестування сортування злиттям
    merge_time = timeit.timeit(lambda: merge_sort(random_array.copy()), number=10)

    # Тестування сортування вставками
    insertion_time = timeit.timeit(lambda: insertion_sort(random_array.copy()), number=10)

    # Тестування Timsort
    timsort_time = timeit.timeit(lambda: timsort(random_array.copy()), number=10)

    return merge_time, insertion_time, timsort_time

# Запуск тестування на масивах різного розміру
sizes = [100, 1000, 5000, 10000]
results = {}

for size in sizes:
    results[size] = test_sorting_algorithms(size)

# Результати
for size, times in results.items():
    print(f"Array Size: {size}")
    print(f"Merge Sort Time: {times[0]:.5f} seconds")
    print(f"Insertion Sort Time: {times[1]:.5f} seconds")
    print(f"Timsort Time: {times[2]:.5f} seconds")
    print([100, 1000, 5000, 10000])