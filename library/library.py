class Order(object):
    def __init(self):
        self.user = ''
        self.phone = ''
        self.bread = ''
        self.sandwich = ''
        self.__quantity = '' #check for valid quantity
        self.chips = ''

    @property
    def quantity(self):
        pass

    @quantity.setter
    def quantity(self, num):
        self.__quantity = num