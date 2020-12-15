def BinarySearch(array, search_key):
    start = 0
    end = array.length
    middle = (end - start) // 2

    while (middle >= 1):
        if search_key == middle:
            return (array[middle])
        elif search_key < middle:
            end = middle
            middle == (end - start) / 2
        elif search_key > middle:
            start = middle,
            middle == (end - start) / 2
    return -1