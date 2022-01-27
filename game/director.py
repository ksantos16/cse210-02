from game.card import Card


class Director:
    """Director is going to direct the game and control the sequence of the play.

    Attibutes:
    List = self.card = [] : this will create a list from the card_generator and hold the values
    Boolean = self.is_playing = True : This is saying the game will continue till the user says (n or NO)
    Int = self.score = 300 : This is the amount you start off with, based on user input the anount will either increase or decrease
    Boolean = self.playerchoice = None : This will hold false till the user inputs a choice."""

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        # sets default values
        self.cards = []
        self.is_playing = True
        self.total_score = 300

        card = Card()
        self.cards.append(card)

    def start_game(self):
        """Method/Function:
        Starts running the game and will continue till the user answer no (n) to continue.

         Args:
        self (game_master): An instance of game_master"""
        # central control function/switchboard

        while self.is_playing:

            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        print()
        print("Thanks for playing!")

    def get_inputs(self):
        """Method/Function:
        Asks the user if the card that is not displayed yet is y or n

        Args:
        self (game_master): An instance of game_master"""
        # gets user inputs
        draw_card = input("Play? [y/n] ")
        self.is_playing = (draw_card == "y")
        print(self.is_playing)

    def do_updates(self):
        """Method/Function:
        Analyzes if current_car_position is greater than or lesser than self.card
        and updates current_card.value score based on the users choice of higher or lower and will display 
        a message and display the current score..

         Args:
        self (game_master): An instance of game_master"""
        # analyzes score using player input

        print(f"Your score is: {self.total_score}\n")
        if not self.is_playing:
            return

        current_card_position = len(self.cards) - 1

        current_card = self.cards[current_card_position]

        print(f"Current card is: {current_card.value}")

        choice = input("Is the next card higher or lower? [higher/lower] ")

        new_card = Card()
        new_card.draw(current_card.value, choice)

        self.cards.append(new_card)

        self.new_card = new_card.value
        self.total_score += new_card.points

    def do_outputs(self):
        """Method/Function:
        Will display the new card drawn and your score, else: game is over if user has run out point and chose to end the game.

         Args:
        self (game_master): An instance of game_master
        """
        if not self.is_playing:
            return

        print(f"The new card drawn was: {self.new_card}")
        print(f"Your score is: {self.total_score}\n")
        if self.total_score > 0:
            self.is_playing = True
        else:
            self.is_playing = False
        print(self.is_playing)
