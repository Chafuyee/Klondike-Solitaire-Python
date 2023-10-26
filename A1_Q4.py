
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
            return list_str
        else:
            return ""

    def push_list(self, values):
        for item in values:
            self.items.append(item)

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
        if self.is_empty():
            raise IndexError("ERROR: The foundation pile is empty!")
        else:
            removed_item = self.items[-1]
            self.items = self.items[:-1]
            return removed_item

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("ERROR: The foundation pile is empty!")
        else:
            removed_item = self.items[0]
            self.items = self.items[1:]
            return removed_item
    
    def peek_front(self):
        if self.is_empty():
            raise IndexError("ERROR: The foundation pile is empty!")
        else:
            return self.items[-1]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("ERROR: The foundation pile is empty!")
        else:
            return self.items[0]


br()

try:
    f = Foundation()
    print(f.remove_front())
except IndexError as e:
    print(e)

br()