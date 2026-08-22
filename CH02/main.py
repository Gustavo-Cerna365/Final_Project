# Exercise 1: Impliment Find Smallest
def find_smallest(arr):
    # Assume the first element is the smallest to start
    smallest_value = arr[0]
    smallest_index = 0

    # Loop over the rest of the list, looking for a smaller value
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i

    return smallest_index

# Exercise 2: Impliment Selection Sort
def selection_sort(arr):
    # Creat a copy to not mutate the caller's list
    arr_copy = arr[:]

    result = []

    while arr_copy:
        smallest_index = find_smallest(arr_copy)
        smallest_value = arr_copy.pop(smallest_index)
        result.append(smallest_value)

    return result

# Exercise 3: Impliment Rank Artists
def rank_artists(plays):
    artist_counts = list(plays.items())
    remaining = artist_counts[:]
    result = []

    while remaining:
        largest_index = 0
        largest_count = remaining[0][1]

        for i in range(1, len(remaining)):
            if remaining[i][1] > largest_count:
                largest_count = remaining[i][1]
                largest_index = i
                
        largest_pair = remaining.pop(largest_index)
        result.append(largest_pair[0])

    return result

# Test Cases
if __name__ == "__main__":
  print(selection_sort([5, 3, 6, 2, 10, 13, 9, 7, 22, 74, 56, 33, 11, 88]))  # Expected: [2, 3, 5, 6, 7, 9, 10, 11, 13, 22, 33, 56, 74, 88]
  print(rank_artists({'Artist A': 100, 'Artist B': 200, 'Artist C': 150}))  # Expected: ['Artist B', 'Artist C', 'Artist A']
