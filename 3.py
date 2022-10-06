# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func_minVSmax(arr):
    print(arr)
    res = [arr[0] % 1,arr[0] % 1,0] 
    for i in range(len(arr)):
        res[2] = round(arr[i] % 1, 2)
        if res[2] < res[0] and res[2] != 0:
            res[0] = res[2]
        elif res[2] > res[1]:
            res[1] = res[2]
    return round(res[1]-res[0],2)

test = [1.1, 1.2, 3.1, 5, 10.01]
print('min - max(test):',func_minVSmax(test))