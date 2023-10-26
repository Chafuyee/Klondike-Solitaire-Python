import random

def br():
    print("=" * 20)

class Foundation:

    def __init__(self):
        self.items = []

    def __str__(self):
        if not self.is_empty():
            list_str = "["
            for index in range(len(self.items)):
                if index != len(self.items)-1:
                    list_str += str(self.items[index]) + ", "
                else:
                    list_str += str(self.items[index]) + "]"
        else:
            list_str = ""
        return list_str

    def push_list(self, values):
        for item in values:
            self.items += [item]

    def is_empty(self):
        if (self.items == None):
            return True
        elif (len(self.items) == 0):
            return True
        else:
            return False

    def size(self):
        if self.is_empty() == True:
            return 0
        else:
            return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        if self.is_empty() == True:
            print("ERROR: The foundation pile is empty!")
        else:
            self.items = [value for value in self.items if value != self.items[-1]]

    def remove_rear(self):
        if self.is_empty() == True:
            print("ERROR: The foundation pile is empty!")
        else:
            self.items = [value for value in self.items if value != self.items[0]]
    
    def peek_front(self):
        if self.is_empty() == True:
            print("ERROR: The foundation pile is empty!")
        else:
            temp_list = [value for value in self.items]
            return temp_list.pop[-1]

    def peek_rear(self):
        if self.is_empty() == True:
            print("ERROR: The foundation pile is empty!")
        else:
            temp_list = [value for value in self.items]
            return temp_list.pop[0]

class Stock:

    def __init__(self, num_cards = 0):
        if num_cards != 0:
            self.items = [value for value in range(num_cards)]
        else:
            self.items = []
        random.shuffle(self.items)

    def __str__(self):
        if len(self.items) != 0:
            list_str = "["
            for index in range(len(self.items)):
                if index != len(self.items)-1:
                    list_str += str(self.items[index]) + ", "
                else:
                    list_str += str(self.items[index]) + "]"
        else:
            list_str = ""
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

    def move(self, pile = None):
        if len(self.items) == 0:
            print("ERROR: The stock pile is empty!")
            return False
        elif pile == None:
            temp_list = [value for value in self.items if value != self.items[0]]
            temp_list.append(self.items[0])
            self.items = temp_list
            return True
        elif (pile.is_empty()) and (pile != None):
            pile.items.append(self.items[0])
            self.items = [value for value in self.items if value != self.items[0]]
            return True
        elif self.items[0] == ((pile.items[-1])-1):
            pile.items.append(self.items[0])
            self.items = [value for value in self.items if value != self.items[0]]
            return True
        else:
            print("ERROR: Invalid move!")
            return False

br()
 	
f2 = Foundation()
s = Stock()
s.push_list([4, 8])
print('s:', s, 'f:', f2) #f2 is an empty foundation pile
print(s.move(f2))  #empty pile
print('s:', s, 'f:', f2)

br()
