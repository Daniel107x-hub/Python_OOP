from Deck import Deck
from Player import Player
from Game import WarCardGame

player = Player("Daniel", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(player, computer, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    # answer = input("\nAre you ready for the next round?\nPress enter to continue or x to stop the game.")
    #
    # if answer.lower() == "x":
    #     break


