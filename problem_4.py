def find_largest_palindrome(roof):
    for x in range(roof, 10, -1):
        for y in range(roof, 10, -1):
            if str(x*y) == str(x*y)[::-1]:
                return x*y

print(find_largest_palindrome(1000))
