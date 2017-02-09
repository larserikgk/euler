def smallest_int_divisbile_by_range(number):
    result = number
    while True:
        for x in range(1, number):
            if result % x != 0:
                result += 1
                continue

    return result

print(smallest_int_divisbile_by_range(2520))