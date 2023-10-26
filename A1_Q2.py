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

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        if len(self.items) == 0:
            return "ERROR: The stock pile is empty!"
        else:
            removed_element = self.items.pop(-1)
        return removed_element

    def remove_rear(self):
        if len(self.items) == 0:
            return "ERROR: The stock pile is empty!"
        else:
            removed_element = self.items.pop(0)
        return removed_element

    def peek_front(self):
        if len(self.items) == 0:
            return "ERROR: The stock pile is empty!"
        else:
            temp_list = [value for value in self.items]
            return temp_list.pop(-1)
        
    def peek_rear(self):
        if len(self.items) == 0:
            return "ERROR: The stock pile is empty!"
        else:
            temp_list = [value for value in self.items]
            return temp_list.pop(0)

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

s = Stock()
s.push_list([2, 5, 1, 4, 3, 0])
print(s)
print(s.peek_front())
print(s)
print(s.peek_rear())
print(s)