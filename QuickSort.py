def quick_sort(array, ascending=True):
    for i in range(len(array)):
        array2 = []

        if i > 0:
            counter = 0
            for subarray in array:
                subarray = move_numbers(subarray)

                # If subarray is a list, it will have nested lists inside it when it is split
                # Thus, we must append each sub-list into array2, rather than the entire list
                if type(subarray[0]) is list:
                    for j in range(len(subarray)):
                        array2.append(subarray[j])
                else:
                    array2.append(subarray)
                    counter += 1
        else:
            counter = 0
            array2 = move_numbers(array)

        # counter used to check whether all items in list have been sorted
        if counter == len(array):
            break

        array = array2

    output = []
    for num in range(len(array)):
        output.append(array[num][0])

    # Reverses order of list if ascending = False (aka descending)
    if ascending:
        return output
    else:
        return output[::-1]


# Shifts smaller numbers to left of pivot (middle number) and larger numbers to the right
def move_numbers(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array) // 2
        pivot = array[mid]
        array2 = [pivot]
        array.pop(mid)
        pivot_pos = 0

        for i in range(len(array)):
            if array[i] > pivot:
                array2.append(array[i])
            elif array[i] <= pivot:
                array2.insert(0, array[i])
                pivot_pos += 1

        array2 = split_array(array2, pivot_pos)

        return array2


# Splits array into 2 or 3 smaller arrays, depending on position of pivot
def split_array(array, pivot_pos):
    if pivot_pos == 0:
        return [[array[pivot_pos]], array[pivot_pos+1:]]
    elif pivot_pos == len(array) - 1:
        return [array[:pivot_pos], [array[pivot_pos]]]
    else:
        return [array[:pivot_pos], [array[pivot_pos]], array[pivot_pos+1:]]


if __name__ == "__main__":
    a = [42, 5, 2, 9, 12, 10, 7, 13, 1, 22, 13, 14354, 23, 2, 6, 2, 7, 2323, 1010]
    a2 = quick_sort(a)
    print(a2)
