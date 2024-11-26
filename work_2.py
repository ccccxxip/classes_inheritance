class Counter:
    def __init__(self, start=0):
        if start < 0:
            raise ValueError("Начальное значение не может быть отрицательным")
        self.value = start
    def inc(self, amount=1):
        if amount <= 0:
            raise ValueError("Число должно быть больше нуля")
        self.value += amount
    def dec(self, amount=1):
        if amount <= 0:
            raise ValueError("Число должно быть больше нуля")
        self.value -= amount
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    def __init__(self, start=0):
        super().__init__(start)
    def dec(self, amount=1):
        pass

non_dec_counter = NonDecCounter(7)
non_dec_counter.inc(3)
non_dec_counter.dec(6) # этот метод ничего не делает
print(non_dec_counter.value) # 7 + 3 = 10
