nums = []
target = int(input("Введите целое число для которого хотите найти индексы: "))
count_list = int(input("Количество элементов в списке: "))
nums = [0 for num in range(count_list)]

for i in range(count_list):
    nums[i] = int(input(f"Введите {i} элемент в списке: "))
    Dict = []

def twoSum(nums: list, target: int) -> list:
    """
    Функция находит индексы списка nums, которые в сумме дают target
    """
    index1 = 0
    index2 = 0
    answer = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                index1 = i
                index2 = j
                answer.append((index1, index2))
                break
    answer.sort(key=lambda x: (x[0], x[0]))
    return answer[0]


arr = twoSum(nums, target)
arr.sort(key = lambda x: (x[0], x[0]))

print(arr)
print(nums)
