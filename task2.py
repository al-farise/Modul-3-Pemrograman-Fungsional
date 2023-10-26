data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

data_1 = filter(lambda word: word.isdigit(), data[0].split())
data_2 = filter(lambda word: word.isdigit(), data[1].split())
data_3 = filter(lambda word: word.isdigit(), data[2].split())

print(list(data_1))
print(list(data_2))
print(list(data_3))