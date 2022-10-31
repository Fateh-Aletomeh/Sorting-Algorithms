def bubble_sort(array, ascending=True):
    counter = 1
    for i in range(len(array)):
        flag = False
        for j in range(len(array) - counter):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = True

        # If there were no changes made, then list must be in order
        if not flag:
            break

        counter += 1

    # Reverses list if ascending = False (aka descending)
    if ascending:
        return array
    else:
        return array[::-1]


if __name__ == "__main__":
    a = ['strawberry', 'abacus', 'milk', 'prison', 'lake', 'mill']
    new_a = bubble_sort(a, False)  # descending
    print(new_a)

    b = [23, 4, 5, 1, 45, 184, 62, 5, 9, 10]
    new_b = bubble_sort(b)  # ascending
    print(new_b)
