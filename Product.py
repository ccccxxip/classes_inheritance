class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_weight(self):
        return self.__weight

    def set_name(self, name):
        self.__name = name
    def set_price(self, price):
        self.__price = price
    def set_weight(self, weight):
        self.__weight = weight

class Buy(Product):
    def __init__(self, name, price, weight, count):
        super().__init__(name, price, weight)
        self.__count = count
        self.__total_price = price * count
        self.__total_weight = weight * count

    def get_count(self):
        return self.__count
    def get_total_price(self):
        return self.__total_price
    def get_total_weight(self):
        return self.__total_weight

    def set_count(self, count):
        self.__count = count
        self.__total_price = self.get_price() * count
        self.__total_weight = self.get_weight() * count

class Check(Buy):
    def __init__(self, name, price, weight, count):
        super().__init__(name, price, weight, count)

    def information(self):
        print(f"товар: {self.get_name()}")
        print(f"цена за штуку: {self.get_price()}")
        print(f"вес за штуку: {self.get_weight()}")
        print(f"количество: {self.get_count()}")
        print(f"общая цена: {self.get_total_price()}")
        print(f"общий вес: {self.get_total_weight()}")

check = Check("Бананы", 90, 0.4, 5)
check.information()