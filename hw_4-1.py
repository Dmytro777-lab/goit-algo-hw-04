import random
import timeit


class Mix_sort:
    def __init__(self, size=10_000):
        self.size = size
        self.random_array = random.sample(range(1, 100001), 10000)
        self.sorted_array = list(range(1, 10001))
        self.revers_array = list(range(10000, 0, -1))
        print(f"Massifs are successfully created")

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def insetion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
        return arr

    def timsort_it(self, arr):
        return sorted(arr)

    def measure_time(self):
        print("Measuring performance...")

        merge_sort_random = timeit.timeit(
            lambda: self.merge_sort(self.random_array.copy()), number=5
        )
        merge_sort_sorted = timeit.timeit(
            lambda: self.merge_sort(self.sorted_array.copy()), number=5
        )
        merge_sort_reverse = timeit.timeit(
            lambda: self.merge_sort(self.revers_array.copy()), number=5
        )

        insertion_sort_random = timeit.timeit(
            lambda: self.insetion_sort(self.random_array.copy()), number=5
        )
        insertion_sort_sorted = timeit.timeit(
            lambda: self.insetion_sort(self.sorted_array.copy()), number=5
        )
        insertion_sort_reverse = timeit.timeit(
            lambda: self.insetion_sort(self.revers_array.copy()), number=5
        )

        timsort_random = timeit.timeit(
            lambda: self.timsort_it(self.random_array.copy()), number=5
        )
        timsort_sorted = timeit.timeit(
            lambda: self.timsort_it(self.sorted_array.copy()), number=5
        )
        timsort_reverse = timeit.timeit(
            lambda: self.timsort_it(self.revers_array.copy()), number=5
        )

        print("Results (time in seconds):")
        print(f"Merge Sort (random): {merge_sort_random:.4f}")
        print(f"Merge Sort (sorted): {merge_sort_sorted:.4f}")
        print(f"Merge Sort (reverse): {merge_sort_reverse:.4f}")
        print(f"Insertion Sort (random): {insertion_sort_random:.4f}")
        print(f"Insertion Sort (sorted): {insertion_sort_sorted:.4f}")
        print(f"Insertion Sort (reverse): {insertion_sort_reverse:.4f}")
        print(f"Timsort (random): {timsort_random:.4f}")
        print(f"Timsort (sorted): {timsort_sorted:.4f}")
        print(f"Timsort (reverse): {timsort_reverse:.4f}")


sorter = Mix_sort()
sorter.measure_time()
