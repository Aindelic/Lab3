def has_dup(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] == n[j]:
                return True
    return False

def main():
    n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Array:", n1, " \nContains duplicates: ", has_dup(n1))

    n2 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Array:", n2, " \nContains duplicates: ", has_dup(n2))

if __name__ == "__main__":
    main()
