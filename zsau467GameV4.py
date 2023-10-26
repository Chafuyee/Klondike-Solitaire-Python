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
This program simulates a simplified version of Klondike Solitaire using
using imported Foundation and Stock classes. The program will loop until
the user wins at the game, there is no instance where the program will
terminate otherwise. 
"""
def main():
    print_banner()
    number_of_cards = 6
    pile1 = Foundation()
    pile2 = Foundation()
    stock = Stock(number_of_cards)
    stock.display()
    is_over = False
    while not is_over:
        valid_run = True
        source_input = get_pile_number("Enter a source pile: ")
        destination_input = get_pile_number("Enter a destination pile: ")
        if source_input == 0 and destination_input == 0:
            stock.move()
        elif source_input == 0 and destination_input == 1:
            valid_run = stock.move(pile1)
        elif source_input == 0 and destination_input == 2:
            valid_run = stock.move(pile2)
        elif source_input == 1 and destination_input == 2:
            valid_run = pile1.move(pile2)
        elif source_input == 2 and destination_input == 1:
            valid_run = pile2.move(pile1)
        else:
            print("ERROR: Invalid move!")
            valid_run = False
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
    valid_list = ["0", "1", "2"]
    valid_input = False
    while not valid_input:
        user_input = input(prompt)
        if user_input not in valid_list:
            print("Invalid pile number!")
        else:
            valid_input = True
    return int(user_input)

def game_over(stock, piles, number_of_cards):
    foundation1_size = piles[0].size()
    foundation2_size = piles[1].size()
    if stock.is_empty() and ((foundation1_size == number_of_cards) or (foundation2_size == number_of_cards)):
        return True
    else:
        return False
    
main()
