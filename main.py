def number_hash(number: int) -> int:
    # Turning the number into an array of digits
    number_arr = [i for i in str(number)]
    # Sorting the array to find the samllest number possible
    number_arr.sort()
    smallest_value = "".join(number_arr)
    # Sorting the array to find the largest number possible
    number_arr.sort(reverse=True)
    largest_value = "".join(number_arr)

    # Turning both into integers then subtracting them
    return int(largest_value) - int(smallest_value)


if __name__ == '__main__':
    print(number_hash(198))