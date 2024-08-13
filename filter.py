def bigger_than_3(x):
    return x > 3

numbers = [1, 2, 3, 4, 5]
filtered_numbers = list(filter(bigger_than_3, numbers))

print(filtered_numbers)

    