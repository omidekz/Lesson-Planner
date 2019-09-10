from typing import List, Tuple


class Time:
    def __init__(self, start: str, end: str):
        h, m = start.split(':')
        self.start = '{}:{}'.format(h.zfill(2), m.zfill(2))
        h, m = end.split(':')
        self.end = '{}:{}'.format(h.zfill(2), m.zfill(2))
        self.start_hour, self.start_minute = map(int, self.start.split(':'))
        self.end_hour, self.end_minute = map(int, self.end.split(':'))

    def start_h(self):
        return self.start_hour

    def start_m(self):
        return self.start_minute

    def end_h(self):
        return self.end_hour

    def end_m(self):
        return self.end_minute

    def value(self, of_start=True) -> int:
        if of_start:
            return int(self.start.replace(':', ''))
        return int(self.end.replace(':', ''))

    def conflict(self, time):
        """
        we can have 3 conflict between times

        B
            [...]
            [...]
        C
            [...]
          [...]
        :param time:
        :return:
        """
        # B
        #   [...]
        #   [...]
        self_start_value = self.value()
        self_end_value = self.value(of_start=False)
        time_start_value = time.value()
        time_end_value = time.value(of_start=False)

        if self_start_value == time_start_value or \
                self_end_value == time_end_value:
            return True
        # A
        #  [...]
        #   [...]
        if self_start_value < time_start_value < self_end_value:
            return True
        # C
        #   [...]
        #  [...]
        if self_start_value < time_end_value < self_end_value:
            return True
        # we have no conflict
        return False

    def __lt__(self, other):
        return self.value() < other.value()

    def __str__(self):
        return '{}-{}'.format(self.start, self.end)

    def __repr__(self):
        return self.__str__()


class Day:
    days = {
        'شنبه': 0,
        'یکشنبه': 1,
        'دوشنبه': 2,
        'سه شنبه': 3,
        'چهارشنبه': 4,
        'پنجشنبه': 5,
        'جمعه': 6,

        'شمبه': 0,
        'یک شنبه': 1,
        'سشنبه': 3,
        'دو شنبه': 2,
        'چهار شنبه': 4,
        'پنج شنبه': 5,
    }

    def __init__(self, name, time: Time):
        if name not in self.days:
            raise Exception('Bad Day Passed {}'.format(name))
        self.day = name
        self.time = time
        self.val = self.days[name]

    def value(self):
        return self.val

    def __str__(self):
        return '({} -> {})'.format(self.day, self.time)

    def __repr__(self):
        return self.__str__()

    def times(self):
        return self.time

    def __eq__(self, other):
        return self.value() == other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __lt__(self, other):
        return self.value() < other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __sub__(self, other):
        def pos(x):
            return x if x > 0 else -x

        return pos(other.value() - self.value())


class Package:
    def __init__(self, code, exam_date: Tuple[int, int, Time]):
        self.days: List[Day] = []
        self.code = code
        self.lesson_name = None
        # tuple of date and day
        # (mon, day_date, Time)
        self.exam_day = exam_date

    def adday(self, day: Day):
        self.days.append(day)

    def __str__(self):
        return self.days.__str__()

    def __repr__(self):
        return self.__str__()


class Program:
    def __init__(self, packages=None):
        self.packages: List[Package] = []
        self.days = {
            'شنبه': [],
            'یکشنبه': [],
            'دوشنبه': [],
            'سه شنبه': [],
            'چهار شنبه': [],
            'پنجشنبه': [],
        }
        self.addpackages(packages)

    def addpackage(self, package: Package):
        self.packages.append(package)
        for ind, day in enumerate(package.days):
            if day.day in self.days:
                self.days[day.day].append((package.lesson_name, day.times()))

    def addpackages(self, packages):
        if packages is None:
            return
        for i in packages:
            self.addpackage(i)

    def __str__(self):
        return self.days.__str__()

    def __repr__(self):
        return self.__str__()


class Lesson:
    DAYS = 'days'
    TIMES = 'times'
    CODE = 'code'
    EXAM_TIME = 'exam_time'
    EXAM_MONTH = 'exam_month'
    EXAM_DAY_DATE = 'exam_day'

    def __init__(self, name, code):
        self.name: str = name
        self.code = code
        self.packages = []

    def addpackage(self, **kwargs):
        days = kwargs[Lesson.DAYS]  # list of name of day
        times = kwargs[Lesson.TIMES]  # list of tuples of time
        code = kwargs[Lesson.CODE]
        ext = kwargs[Lesson.EXAM_TIME]
        exm = kwargs[Lesson.EXAM_MONTH]
        exd = kwargs[Lesson.EXAM_DAY_DATE]

        if len(times) != len(days):
            raise Exception('not equal')

        package = Package(code, (exm, exd, Time(ext[0], ext[1])))
        package.lesson_name = self.name
        del code

        for index in range(len(days)):
            time = Time(times[index][0], times[index][1])
            day = Day(days[index], time)
            package.adday(day)

        self.packages.append(package)

    def __str__(self):
        return '{} [{}]'.format(self.name, ', '.join([package.__str__() for package in self.packages]))

    def __repr__(self):
        return self.__str__()
