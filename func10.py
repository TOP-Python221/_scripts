def average(num1, num2, *nums):
    nums += (num1, num2)
    return round(sum(nums) / len(nums), 3)

print(average(1, 10))
print(average(1, 10, 100))
print(average(1, 10, 100, 1000))
# вызовет ошибку
print(average(1))
