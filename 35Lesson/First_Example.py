import multiprocessing
import os
import threading
import time

numbers_list = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)

low_letters_list = ('a', 'b', 'c', 'd', 'e', 'f', 'g',
                    'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z',)

high_letters_list = ('A', 'B', 'C', 'D', 'E', 'F', 'G',
                     'H', 'I', 'J', 'K', 'L', 'M', 'N',
                     'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                     'V', 'W', 'X', 'Y', 'Z',)

spec_symbols_list = ('~', '|', '/', '.', ',', '*', '-',
                     '+', '<', '>', '?', '!', '&', '%',
                     '@', '#', '$', '(', ')',)

#Функция для записи результата в файл
def write_file(search_method, start_time, finish_time, password):
    print(f"Время выполнения {search_method} метода - {finish_time - start_time:4f}. Пароль {password}.\n")

    with open("Results.txt", 'a') as result_file:
        result_file.write(
            f"Время выполнения {search_method} метода - {finish_time - start_time:4f}. Пароль {password}.\n")

#Класс для поиска пароля
class PasswordSearcher:
    def __init__(self, symbols, searched_password):
        if len(searched_password) < 6:
            add_length = 6 - len(searched_password)
            searched_password = ('0' * add_length) + searched_password
        self.symbols_list = symbols  # Принимаемый набор символов для подбора
        self.password = searched_password  # Искомый пароль
        self.stop_thread = False  # Сигнал о завершении потока Thread
        self.stop_process = multiprocessing.Event()  # Сигнал о завершении процесса Process