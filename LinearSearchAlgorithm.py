arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
search_for = 'e'
for i in range(len(arr)):
    if arr[i] == search_for:
        print("Found at index: {}".format(i))