# CSV (comma-separated values)
data = '1.23,3,2.4;8,4.3'
# строка с символами-разделителями
separs = '.,;'
# индекс предпоследнего разделителя
q = 0
result = []
# перебираем все символы в исходной строке
for i in range(len(data)):
    # нашли разделитель
    if data[i] in separs:
        # срез от предпоследнего разделителя до только что найденного
        result += [data[q:i]]
        # записываем индекс только что найденного разделителя в предпоследний
        q = i + 1
# последнее значение в исходной строке
result += [data[q:]]
