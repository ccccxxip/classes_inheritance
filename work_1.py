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

counter = Counter()
counter.inc()
print(counter.value)
counter.inc(7)
print(counter.value)
counter.dec(3)
print(counter.value)
counter.dec(20)
print(counter.value)