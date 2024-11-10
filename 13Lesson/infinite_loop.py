import time


length_num = int(input("Введите длину последовательности чисел:"))

def generator_func(len):
    while True:
        for i in range(1, len + 1):
            yield i

def print_gen(gener):
    while True:
        print(next(gener))
        time.sleep(0.3)


inf_gen = generator_func(length_num)

print_gen(inf_gen)