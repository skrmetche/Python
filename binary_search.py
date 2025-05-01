def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = list[middle]
        print(f"Looking at number {guess}...")

        if guess == item:
            print("Item found! 🎉")
            return middle
        elif guess < item:
            print("Guess is too small! Look to the right ➡️")
            low = middle + 1
        else:
            print("Guess is too big! Look to the left ⬅️")
            high = middle - 1

    print("The item is not available ❌")
    return -1

# Try it out
list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
item = 5
binary_search(list, item)
