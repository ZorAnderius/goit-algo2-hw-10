import random
import time
import matplotlib.pyplot as plt

# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)


# Детермінований QuickSort (опорний елемент - останній)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = {'randomized': [],'randomized_sorted': [], 'deterministic': [], 'deterministic_sorted': []}

    for size in sizes:
        arr = [random.randint(1, 1000000) for _ in range(size)]

        sort_arr = sorted(arr)
        # Час для рандомізованого QuickSort
        rand_time = measure_time(randomized_quick_sort, arr)

        # Час для детермінованого QuickSort
        det_time = measure_time(deterministic_quick_sort, arr)

        rand_sorted_time = measure_time(randomized_quick_sort, sort_arr)

        det_sorted_time = measure_time(deterministic_quick_sort, sort_arr)

        results['randomized_sorted'].append(rand_sorted_time)
        results['deterministic_sorted'].append(det_sorted_time)

        results['randomized'].append(rand_time)
        results['deterministic'].append(det_time)

    for i, size in enumerate(sizes):
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {results['randomized'][i]:.4f} секунд")
        print(f"   Детермінований QuickSort: {results['deterministic'][i]:.4f} секунд")
        print(f"   Рандомізований QuickSort (сортування вже відсортованого масиву): {results['randomized_sorted'][i]:.4f} секунд")
        print(f"   Детермінований QuickSort (сортування вже відсортованого масиву): {results['deterministic_sorted'][i]:.4f} секунд")

    plt.plot(sizes, results['randomized'], label='Рандомізований QuickSort', marker='o')
    plt.plot(sizes, results['deterministic'], label='Детермінований QuickSort', marker='x')

    plt.plot(sizes, results['randomized_sorted'], label='Рандомізований QuickSort (сортування вже відсортованого масиву)', marker='o')
    plt.plot(sizes, results['deterministic_sorted'], label='Детермінований QuickSort (сортування вже відсортованого масиву)', marker='x')

    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння рандомізованого та детермінованого QuickSort')
    plt.legend()
    plt.grid(True)
    plt.show()