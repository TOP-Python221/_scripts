from math import prod

def average(num1=1, num2=1, *nums, mode='a'):
    nums += (num1, num2)
    if mode == 'a':
        return round(sum(nums) / len(nums), 3)
    elif mode == 'g':
        return round((prod(nums))**(1/len(nums)), 3)

print(average(1, 10))
print(average(1, 10, 100))
print(average(1, 10, 100, 1000))
print(average(1, 10, 100, 1000, mode='g'))

print(average(1))
print(average(15, 10, 5, 6))
# вызовет ошибку
# print(average(num2=10, num1=15, 5, 6))

