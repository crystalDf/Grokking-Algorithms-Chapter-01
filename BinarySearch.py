def binary_search(input_list, item):

    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = input_list[mid]

        if guess == item:
            return guess
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
