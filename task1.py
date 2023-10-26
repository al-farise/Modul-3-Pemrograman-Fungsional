data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

def convert(w=0):
    def day(d=0):
        def hour(h=0):
            def minute(m=0):
                return m + (h * 60) + (d * 1440) + (w * 10080)
            return minute
        return hour
    return day

data_numbers = map(lambda text: [int(word) for word in text.split() if word.isdigit()], data)
data_output = map(lambda numbers: convert(numbers[0])(numbers[1])(numbers[2])(numbers[3]), data_numbers)

print("OutputData =",list(data_output))