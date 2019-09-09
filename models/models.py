class Time:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end
        self.start_hour, self.start_minute = map(int, start.split(':'))
        self.end_hour, self.end_minute = map(int, end.split(':'))

    def start_h(self):
        return self.start_hour

    def start_m(self):
        return self.start_minute

    def end_h(self):
        return self.end_hour

    def end_m(self):
        return self.end_minute

    def value(self, of_start=True):
        if of_start:
            return int('{}{}'.format(self.start_h(), self.start_m()))
        return int('{}{}'.format(self.end_h(), self.end_m()))

    def conflict(self, time):
        """
        we can have 3 conflict between times
        A
            [...]
              [...]
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
        self_value = self.value()
        time_value = time.value()
        if self_value == time:
            return True
        # A
        self_value = self.value(of_start=False)
        time_value = time.value()
        if self_value > time_value:
            return True
        # C
        self_value = self.value()
        time_value = time.value(of_start=False)
        if time_value > self_value:
            return True
        # we have no conflict
        return False

    def __str__(self):
        return '{}-{}'.format(self.start, self.end)

    def __repr__(self):
        return self.__str__()
