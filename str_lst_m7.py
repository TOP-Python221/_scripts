# CSV (comma-separated values)
data = '12,34,15,16,18,17'
# очень длинная строка
data2 = ','.join([str(i) for i in range(10**7)])

# формируется список из 15+1 значений
# последнее значение – неразбитая строка
print(*data2.split(',', 15)[:-1], sep='\n', end='\n\n')
# первое значение – неразбитая строка
print(*data2.rsplit(',', 15)[1:], sep='\n')
