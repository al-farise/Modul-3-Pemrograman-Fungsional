random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_data = tuple(filter(lambda item: type(item) is float, random_list))

string_data = list(filter(lambda item: type(item) is str, random_list))

integer_data = list(map(lambda item: {
    "ratusan": int(item / 100),
    "puluhan": int((item % 100) / 10),
    "satuan": int(((item % 100) % 10) / 1)
}, filter(lambda item: type(item) is int, random_list)))

print(f'Float data: {float_data}')
print(f'String data: {string_data}')
print(f'Integer data: {integer_data}')
