import random


class Stock:

    def __init__(self, num_cards = 0):
        if num_cards != 0:
            self.items = [value for value in range(num_cards)]
        else:
            self.items = []
        random.shuffle(self.items)

    def __str__(self):
        list_str = "["
        for index in range(len(self.items)):
            if index != len(self.items)-1:
                list_str += str(self.items[index]) + ", "
            else:
                list_str += str(self.items[index]) + "]"
        return list_str

    def push_list(self, values):
        for value in values:
            self.items += [value]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        if len(self.items) != 0:
            stock_str = "S: " + str(self.items[0]) + " *" * (len(self.items)-1)
        else:
            stock_str = "S:"
        print(stock_str)

    
random.seed(30)
s = Stock(6)