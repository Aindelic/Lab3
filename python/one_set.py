def find_duplicates(input_list):
    seen = set()
    for item in input_list:
        if item in seen:
            return True
        else:
            seen.add(item)
    return False

n1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9,]
n2 = [1, 2, 3, 4, 5, 6, 7, 8]
print("Array: ", n1, "\nContains duplicates: ", find_duplicates(n1))
print("Array: ", n1, "\nContains duplicates: ", find_duplicates(n2))


