import string

# Import name list
f = open('problem_22_names.txt', 'r')
name_list_string = f.read()[1:-1]
name_list = name_list_string.split('","')
name_list.sort()

# Generate dict with alphabetical values
values = dict.fromkeys(string.ascii_uppercase, 0)
for counter, key in enumerate(values):
    values[key] = counter+1

# Calculate value of all names in list
result = 0
for counter, name in enumerate(name_list):
    partial_result = 0
    for c in name:
        partial_result += values[c] * (counter + 1)
    result += partial_result

print(result)
