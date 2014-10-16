class OrderSandwich(object):
    def __init(self):
        self.user = ''
        self.phone = ''
        self.bread = ''
        self.sandwich = ''
        self.quantity = '' #check for valid quantity
        self.chips = ''


    def add_order(self, s):
        self.__your_order(s)


    def compile_order(self):
        output = ''
        for order in self.__your_order:
            output += 'Your Name: ' + ' ' + 'You wanted ' + '<br />'
        return output



    def calc_order_total(self):
        '''
        calculate the total of the order
        '''
