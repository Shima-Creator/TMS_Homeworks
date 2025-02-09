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

# Функция для записи результата в файл
def write_file(search_method, start_time, finish_time, password):
    print(f"Время выполнения {search_method} метода - {finish_time - start_time:4f}. Пароль {password}.\n")

    with open("Results.txt", 'a') as result_file:
        result_file.write(
            f"Время выполнения {search_method} метода - {finish_time - start_time:4f}. Пароль {password}.\n")

# Класс для поиска пароля
class PasswordSearcher:
    def __init__(self, symbols, searched_password):
        if len(searched_password) < 6:
            add_length = 6 - len(searched_password)
            searched_password = ('0' * add_length) + searched_password
        self.symbols_list = symbols  # Принимаемый набор символов для подбора
        self.password = searched_password  # Искомый пароль
        self.stop_thread = False  # Сигнал о завершении потока Thread
        self.stop_process = multiprocessing.Event()  # Сигнал о завершении процесса Process

    def search_with_known_len(self, diapason):
        """
        Перебирает все комбинации паролей заданной длины.
        :param diapason: Диапазон символов для подбора
        """
        if self.stop_thread or self.stop_process.is_set():
            return True

        pass_list = [''] * 6  # Инициализируем список пустыми строками для 6 символов
        current_password = "".join(pass_list)

        if current_password == self.password:
            self.stop_thread = True
            self.stop_process.set()
            print(f"Пароль найден! Ваш пароль = {current_password}")

            return True

        for var1 in diapason:
            pass_list[0] = var1
            if self.stop_thread or self.stop_process.is_set(): break

            for var2 in self.symbols_list:
                pass_list[1] = var2

                for var3 in self.symbols_list:
                    pass_list[2] = var3
                    print(current_password, " STANDART\n")

                    for var4 in self.symbols_list:
                        pass_list[3] = var4

                        for var5 in self.symbols_list:
                            pass_list[4] = var5

                            for var6 in self.symbols_list:
                                pass_list[5] = var6
                                current_password = ''.join(pass_list)

                                if current_password == self.password:
                                    self.stop_thread = True
                                    self.stop_process.set()
                                    print(f"Пароль найден! Ваш пароль = {current_password}")
                                    return True

        print("Пароль не найден :(")
        return False

    def rec_search_with_known_len(self):
        """
        Перебирает все комбинации паролей заданной длины реверсивно.
        """
        if self.stop_thread or self.stop_process.is_set():
            return True

        pass_list = [''] * 6  # Инициализируем список пустыми строками для 8 символов
        current_password = "".join(pass_list)

        if current_password == self.password:
            self.stop_thread = True
            self.stop_process.set()
            print(f"Пароль найден! Ваш пароль = {current_password}")
            return True

        for var1 in self.symbols_list:
            pass_list[5] = var1
            if self.stop_thread or self.stop_process.is_set(): break

            for var2 in self.symbols_list:
                pass_list[4] = var2
                print(current_password, " REVERSE\n")

                for var3 in self.symbols_list:
                    pass_list[3] = var3

                    for var4 in self.symbols_list:
                        pass_list[2] = var4

                        for var5 in self.symbols_list:
                            pass_list[1] = var5

                            for var6 in self.symbols_list:
                                pass_list[0] = var6
                                current_password = ''.join(pass_list)

                                if current_password == self.password:
                                    self.stop_thread = True
                                    self.stop_process.set()
                                    print(f"Пароль найден! Ваш пароль = {current_password}")
                                    return True

        print("Пароль не найден :(")
        return False

    def start_threads(self):
        """Запускает оба метода в отдельных потоках и ждет завершения одного из них."""
        cpu_cores = os.cpu_count()
        symbols_diap = len(self.symbols_list) // cpu_cores

        threads = []

        for i in range(cpu_cores):
            start_index = i * symbols_diap
            end_index = (i + 1) * symbols_diap if i < cpu_cores - 1 else len(
                self.symbols_list)  # last process gets the remainder

            process = threading.Thread(target=self.search_with_known_len,
                                       args=(self.symbols_list[start_index:end_index],))
            threads.append(process)
            process.start()

        for thread in threads:
            thread.join()

        print("Оба процесса завершены.")