# 3 задание

class SuperStr(str):
    def is_repeatance(self, s):
        repeat_bool = False

        if len(self) % len(s) == 0 and len(self) != 0:
            num_repeat = len(self) // len(s)

            if self == s * num_repeat:
                repeat_bool = True
            else:
                repeat_bool = False

        return repeat_bool

    def is_palindrom(self):
        low_str = self.lower()
        reverse_str = low_str[::-1]
        if low_str == reverse_str or self == 0:
            return True
        else:
            return False


text_full = SuperStr(input("Введите текст:"))
text_repeat = SuperStr(input("Введите повторяющийся текст для метода:"))


print(f"Текст может быть получен повтором строки {text_repeat} - {text_full.is_repeatance(text_repeat)}")
print(f"Текст палиндром - {text_full.is_palindrom()}")
