# 1 Задание

class MyTime:
    def __init__(self, *args):
        if len(args) == 0:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif len(args) == 1 and isinstance(args[0], str):
            h, m, s = map(int, args[0].split(':'))
            self.hours = h
            self.minutes = m
            self.seconds = s
        elif len(args) == 3:
            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = args[2]
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds

        self.show_time()

    def print_args(self):
        print(self.hours, self.minutes, self.seconds)

    def show_time(self):
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes %= 60
        if self.hours >= 24:
            self.hours %= 24

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    # Переопределение оператора *
    def __mul__(self, number):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) * number
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return MyTime(hours, minutes, seconds)

    # Переопределение оператора +
    def __add__(self, time_class):
        return MyTime(self.hours + time_class.hours, self.minutes + time_class.minutes, self.seconds + time_class.seconds)

    # Переопределение оператора -
    def __sub__(self, time_class):
        total_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_other = time_class.hours * 3600 + time_class.minutes * 60 + time_class.seconds
        total_diff = total_self - total_other

        hours = total_diff // 3600
        total_diff %= 3600
        minutes = total_diff // 60
        seconds = total_diff % 60
        return MyTime(hours, minutes, seconds)

    # Переопределение оператора ==
    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    # Переопределение оператора !=
    def __ne__(self, other):
        return not self == other

    # Переопределение оператора <
    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    # Переопределение оператора >
    def __gt__(self, other):
        return (self.hours, self.minutes, self.seconds) > (other.hours, other.minutes, other.seconds)

    # Переопределение оператора <=
    def __le__(self, other):
        return self < other or self == other

    # Переопределение оператора >=
    def __ge__(self, other):
        return self > other or self == other


time_1 = MyTime(20, 53, 48)
time_2 = MyTime("20:53:28")
time_3 = MyTime(time_1)
time_4 = MyTime(19, 26, 17)


