def number_in_array(array, num):
    return num_in_array(array, num, 0, len(array[0])-1)


def num_in_array(array, num, a, b):
    if a >= len(array) or b < 0:
        return False
    if num > array[a][b]:
        return num_in_array(array, num, a+1, b)
    elif num < array[a][b]:
        return num_in_array(array, num, a, b-1)
    else:
        return True


if __name__ == '__main__':
    array = [[1, 4, 13], [2, 5, 15], [6, 9, 20], [7, 10, 21]]
    print(number_in_array(array, 3))