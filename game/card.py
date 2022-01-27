import random


class Card:
    """ The card generator will produce a randome card from 1 to 13 that 
    will be used for the game.

    Attributes:
    self.card sets the card value"""
    # generates a card to be used at call point, returns INT

    def __init__(self):
        """ Constructs a new instance of car_generator."""
        # sets default card value

        self.value = random.randint(1, 13)
        self.points = 0

    def draw(self, current_card, choice):
        """Method/Function:   
        This will generate a card from 1 to 13"""
        # randomly draws a card with values between 1 to 13

        self.value = random.randint(1, 13)

        if choice == "higher":
            self.points = 100 if self.value > current_card else 0 if self.value == current_card else -75

        elif choice == "lower":
            self.points = 100 if self.value < current_card else 0 if self.value == current_card else -75
