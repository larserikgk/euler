def number_to_text(input_number):
    number = int(input_number)
    answer = ""

    single_digits = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
                     10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
                     16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    multiple_digits = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
                       90: "ninety", 100: "hundred", 1000: "thousand"}
    if number >= 1000:
        answer += single_digits[int(number / 1000)]
        answer += multiple_digits[1000]
        number -= 1000 * int(number / 1000)
    if number >= 100:
        answer += single_digits[int(number / 100)]
        answer += multiple_digits[100]
        if number % 100 != 0:
            answer += "and"
        number -= 100 * int(number/100)
    if 20 <= number < 100:
        answer += multiple_digits[int(number/10)*10]
        number -= 10 * int(number/10)
    if 0 < number < 20:
        answer += single_digits[number]

    return answer


def return_number_as_strings(number):
    result = ""
    for x in range(1, number+1):
        result += number_to_text(x)
    return result

print(len(return_number_as_strings(1000)))
