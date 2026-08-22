import math
import matplotlib.pyplot as plt

# Exercise 1: Implementing linear search
def linear_search(arr, item):
    steps = 0
    for index, value in enumerate(arr):
        steps += 1
        if value == item:
            return index, steps
    return None, steps

# Exercise 2: Implement Binary Search
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid, steps
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None, steps

# Exercise 3: Implement Max Step Binary Search
def max_steps_binary_search(n):
    arr = list(range(n))
    _, steps = binary_search(arr, -1)
    return steps

if __name__ == "__main__":
    sample_sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 89, 95]

# Exercise 4
    found_index_linear, steps_linear = linear_search(sample_sorted_list, 67)
    print(found_index_linear)
    print(steps_linear)

    found_index_binary, steps_binary = binary_search(sample_sorted_list, 67)
    print(found_index_binary)
    print(steps_binary)

# Exercise 5: Call Max Step Binary Search in the book size loop
book_sizes = (128, 256, 1024, 2048)
for n in book_sizes:
    steps = max_steps_binary_search(n)
    naive_formula = math.ceil(math.log2(n)) + 1
    print(n)
    print(steps)
    print(naive_formula)

# Exercise 6: Build lists and measure step counts inside the sizes loop
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    linear_counts = []
    binary_counts = []

for n in sizes:
    arr = list(range(n))
    _, l_steps = linear_search(arr, -1)
    _, b_steps = binary_search(arr, -1)
    linear_counts.append(l_steps)
    binary_counts.append(b_steps)
    print(n)
    print(l_steps)
    print(b_steps)

# Exercise 7: Plot comparison data
plt.figure(figsize=(8, 5))
plt.plot(sizes, linear_counts, marker="o", label="Linear search: O(n)")
plt.plot(sizes, binary_counts, marker="o", label="Binary search: O(log n)")
plt.xscale("log")
plt.xlabel("List size (n)")
plt.ylabel("Comparisons (worst case)")
plt.title("Growth of linear vs. binary search")
plt.legend()
plt.tight_layout()
plt.close()
