def main():
    unsorted_arr = [8, 1, 6, 9, 5, 4, 2, 7, 0, 3]
    arr_length = len(unsorted_arr)

    temp = 0
    for i in range(arr_length):
        for j in range(1, arr_length-i):
            if unsorted_arr[j - 1] > unsorted_arr[j]:
                # swap elements
                temp = unsorted_arr[j - 1]
                unsorted_arr[j - 1] = unsorted_arr[j]
                unsorted_arr[j] = temp
    # for

    for i in range(arr_length):
        print(unsorted_arr[i], " ")


if __name__ == "__main__":
    main()