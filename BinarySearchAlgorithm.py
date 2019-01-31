def main():
    sorted_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    search_for = 3
    low = sorted_arr[0]
    high = sorted_arr[len(sorted_arr)-1]

    while low <= high:
        mid_of_array = int((high + low) / 2)
        if mid_of_array < search_for:
            low = mid_of_array + 1
        elif mid_of_array == search_for:
            print("{} found at index: {}".format(search_for, mid_of_array))
            break
        else:
            high = mid_of_array - 1

    if low > high:
        print("{} isn't present in the list.\n".format(search_for))


if __name__ == "__main__":
    main()