import math

number_string = str(int(math.pow(2, 1000)))

print(sum(x for x in list(map(int, number_string))))
