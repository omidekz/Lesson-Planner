class Time:
    def __init__(self, start: str, end: str):
        def fill_with(x):
            return x.zfill(2)

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

    def value(self, of_start=True):
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

    def __str__(self):
        return '{}-{}'.format(self.start, self.end)

    def __repr__(self):
        return self.__str__()
