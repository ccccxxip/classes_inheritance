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

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        if limit < 0:
            raise ValueError("макс.значение не может быть отрицательным")
        self.limit = limit
    def inc(self, amount):
        if amount < 0:
            raise ValueError("не может быть отрицательным")
        new_value = self.value + amount
        if new_value > self.limit:
            self.value = self.limit
        else:
            self.value = new_value

#Counter
counter = Counter()
counter.inc()
print(counter.value)
counter.inc(7)
print(counter.value)
counter.dec(3)
print(counter.value)
counter.dec(20)
print(counter.value)
print("-------")

#NonDecCounter
non_dec_counter = NonDecCounter(7)
non_dec_counter.inc(3)
non_dec_counter.dec(6) # этот метод ничего не делает
print(non_dec_counter.value) # 7 + 3 = 10
print("-------")

#LimitedCounter
limited_counter = LimitedCounter(12, 20)
print(f"начальное значение = {limited_counter.value}")
limited_counter.inc(11) # перешли за предел, но программа выводит наш заданный предел
print(f"значение после увеличения = {limited_counter.value}")
limited_counter.dec(9)
print(f"значение после уменьшения = {limited_counter.value}")
