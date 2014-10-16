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
        if num > 1: #if the number is not valid
            print "Error, invalid number!"
            self.__quantity = 1
        else:
            self.__quantity = num