class Hangman:
    def __init__(self):

        self._board = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ','-','-','-','-',' ',' '],
                       [' ',' ',' ',' ','|',' ',' ','|',' ',' '],
                       [' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
                       [' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
                       [' ',' ','_','_','_','_','_',' ',' ',' '],
                       [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        self._wrong_guess = 0
        self._try_again = False
        self._end_game = False
        
    def display_board(self):

        for row in self._board:
            for element in row:
                print(element, end=' ')
            print()
    def add_body_part(self):
        self._wrong_guess += 1
        if self._wrong_guess == 1:
            self.add_head()
        if self._wrong_guess == 2:
            self.add_torso()
        if self._wrong_guess == 3:
            self.add_left_arm()
        if self._wrong_guess == 4:
            self.add_right_arm()
        if self._wrong_guess == 5:
            self.add_left_leg()
        if self._wrong_guess == 6:
            self.add_right_leg()
        if self._wrong_guess >= 7:
            self.end_game()
        
            
    def end_game(self):
        self._end_game = True
        print("You have lost at hangman")
        choice = input("Try again? Press 'y' for yes 'n' for no")
        if choice == 'y':
            self._try_again = True
        if choice == 'n':
            self._try_agian = False
            
    def add_head(self):

        self._board[5][7] = '0'

    def add_torso(self):
        self._board[6][7] = '|'
        self._board[7][7] = '|'

    def add_left_arm(self):

        self._board[6][6] = '\\'

    def add_right_arm(self):

        self._board[6][8] = '/'

    def add_left_leg(self):

        self._board[8][6] = '/'

    def add_right_leg(self):

        self._board[8][8] = '\\'
        
