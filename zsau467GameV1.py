import random
random.seed(30)
from Stock import Stock
from Foundation import Foundation
"""
Compsci130 Assignment 
Student ID
Name: Zachary Saunders
Username: zsau467
Description: 
"""
def main():
    print_banner()
    number_of_cards = 6
    pile1 = Foundation()
    pile2 = Foundation()
    stock = Stock(number_of_cards)
    stock.display()
    is_over = game_over(stock, [pile1, pile2], number_of_cards)
    while not is_over:
        valid_run = True
        source_input = get_pile_number("Enter a source pile: ")
        destination_input = get_pile_number("Enter a destination pile: ")
        if source_input == 0 and destination_input == 0:
            if stock.is_empty():
                print("ERROR: Stock pile is empty")
                valid_run = False
            else:
                rear_item = stock.remove_rear()
                stock.add_front(rear_item)
        elif source_input == 0 and destination_input == 1:
            if stock.is_empty():
                print("ERROR: Stock pile is empty")
                valid_run = False
            else:
                if pile1.is_empty():
                    num_to_add = stock.remove_rear()
                    pile1.add_front(num_to_add)
                elif stock.items[0] == pile1.items[-1]-1:
                    num_to_add = stock.remove_rear()
                    pile1.add_front(num_to_add)
                else:
                    print("ERROR: Invalid move!")
                    valid_run = False
        elif source_input == 0 and destination_input == 2:
            if stock.is_empty():
                print("ERROR: Stock pile is empty")
                valid_run = False
            else:
                if pile2.is_empty():
                    num_to_add = stock.remove_rear()
                    pile2.add_front(num_to_add)
                elif stock.items[0] == pile2.items[-1]-1:
                    num_to_add = stock.remove_rear()
                    pile2.add_front(num_to_add)
                else:
                    print("ERROR: Invalid move!")
                    valid_run = False
        elif source_input == 1 and destination_input == 0:
            print("ERROR: Invalid move!")
            valid_run = False
        elif source_input == 2 and destination_input == 0:
            print("ERROR: Invalid move!")
            valid_run = False
        elif source_input == 1 and destination_input == 1:
            print("ERROR: Invalid move!")
            valid_run = False
        elif source_input == 2 and destination_input == 2:
            print("ERROR: Invalid move!")
            valid_run = False
        elif source_input == 1 and destination_input == 2:
            if pile1.is_empty():
                print("ERROR: Foundation pile is empty")
                valid_run = False
            else:
                pile1.move(pile2)
        elif source_input == 2 and destination_input == 1:
            if pile2.is_empty():
                print("ERROR: Foundation pile is empty")
                valid_run = False
            else:
                pile2.move(pile1)
        if valid_run:
            print_all_piles(stock, [pile1, pile2])
            is_over = game_over(stock, [pile1, pile2], number_of_cards)
    print("Congratulations!")


def print_banner():
    print("CS130 Assignment - Simplified Klondike Solitaire")
    print("================================================")


def print_all_piles(stock, piles):
    stock.display()
    print("1: ", end="")
    print(piles[0])
    print("2: ", end="")
    print(piles[1])

def get_pile_number(prompt):
    valid_list = [0, 1, 2]
    user_input = int(input(prompt))
    if user_input not in valid_list:
        print("Invalid pile number!")
    while user_input not in valid_list:
        user_input = int(input(prompt))
        print("Invalid pile number!")
    return user_input
    

def game_over(stock, piles, number_of_cards):
    foundation_exception = False
    for index in range(len(piles)):
        card_list = piles[index].items
        if (len(card_list) == number_of_cards):
            foundation_exception = True

    if stock.is_empty() and foundation_exception == True:
        return True
    else:
        return False
    
main()
