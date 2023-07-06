##############################################################
    #  Computer Project #10
    #
    #  innit game function
    #   returns and intializes varibles
    #  Deal to tableau function
    #   deals card to tableau
    #  Validate to move foundation function
    #   Returns false if condtions are not met to move
    #   Returns true if it is a vaild move and satifying the condtions met
    #  Move to foundations function
    #   If vailidate returns True
    #       Adds card to founation and remove from tableau
    #  Validate to move within tableau function
    #   Returns false if condtions are not met to move
    #   Returns true if it is a vaild move and satifying the condtions met
    #  Move within tableau function
    #   If validate returns true
    #   Move card from tableau column to inputted column and remove from orginal
    #  Check for win function
    #   If all aces are in the foundation
    #       Return True
    #   Other wise return False
    #  Display function
    #   Prints and correctly formats cards
    #  Get option function
    #   Asks for input 
    #   If the input is vaild 
    #       return the input in a list
    #  Main function
    #   Define menu options 
    #   Call necessary functions
    #   Intiate while loop for when the option is not Q
    #       Initiate while loop for every option
    #           Call necessay functions to the main function in each option
    #           Print statemenets for options
    #           Print menu options 
    #    Display closing message
##############################################################

import cards  # required !!!
RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    """
    Initializes game values

    Returns
    -------
    stock : Class
        is the stock of cards in the game.
    tableau : List
        Lists of lists of card that get dealed to.
    foundation : List
        List that is empty but cards are moved to.

    """
    foundation = []
    stock = cards.Deck()
    stock.shuffle()
    tableau = []
    #Append stock.deal 4 times
    for i in range(4):
       tableau.append([stock.deal()])
    return stock, tableau, foundation
    
def deal_to_tableau( tableau, stock):
    """
    Deals cards to the tableau

    Parameters
    ----------
    tableau : Lists
        Lists of lists of card that get dealed to.
    stock : Class
        is the stock of cards in the game.

    Returns
    -------
    None.

    """
    #Iterate through tableau to deal more crads
    for lists in tableau:
        lists.append(stock.deal())
           
def validate_move_to_foundation( tableau, from_col ):
    """
    Checks to see if the move is vaild from tableau to foundation

    Parameters
    ----------
    tableau : Lists
        Lists of lists of card that get dealed to.
    from_col : int
        The column in the tableau to look at and move.

    Returns
    -------
    bool
        True or false returned, true if card can be moved.

    """
    if 0 <= from_col <= 3:
        #Error checking, print and return False
        if len(tableau[from_col]) == 0:
            print("\nError, empty column:")
            return False
        card = tableau[from_col][-1]
        if card.rank() == 1:
            print("\nError, cannot move {}.".format(card))
            return False
        #If these conditions are met return True
        for lists in tableau:
            if len(lists) > 0:
                new_card = lists[-1]
                if (new_card.suit() == card.suit()) and (new_card.rank() > card.rank() or new_card.rank()==1):
                    return True
        else:
            print("\nError, cannot move {}.".format(card))
            return False

def move_to_foundation(tableau, foundation, from_col):
    """
    Moves the card from tableau to foundation

    Parameters
    ----------
    tableau : List
        Lists of lists of card that get dealed to.
    foundation : List
        The list tthat the cards are moved to.
    from_col : int
        The column in the tableau to look at and move.

    Returns
    -------
    None.

    """
    #If the validate function is true, append to foundation and removed from tableau
    if validate_move_to_foundation(tableau, from_col) == True:
        foundation.append(tableau[from_col][-1])
        tableau[from_col].pop()

def validate_move_within_tableau( tableau, from_col, to_col ):
    """
    Checks to see if the cards can be moved around in the tableau

    Parameters
    ----------
    tableau : Lists
        Lists of lists of card that get dealed to.
    from_col : int
        The column in the tableau to look at and move.
    to_col : int
        The column to move card too.

    Returns
    -------
    bool
        True or false returned, true if card can be moved.

    """
    #Error checking, print and return False
    if len(tableau[to_col]) != 0:
        column = to_col + 1
        print("\nError, target column is not empty: {}".format(column))
        return False
    elif len(tableau[from_col]) == 0:
        column = from_col + 1
        print("\nError, no card in column: {}".format(column))
        return False
    #If these condtions are met return true
    elif len(tableau[to_col]) == 0:
        if len(tableau[from_col]) != 0:
            return True

def move_within_tableau( tableau, from_col, to_col ):
    """
    Moves the cards around in tableau.

    Parameters
    ----------
    tableau : Lists
        Lists of lists of card that get dealed to.
    from_col : int
        The column in the tableau to look at and move.
    to_col : int
        The column to move card too.

    Returns
    -------
    None.

    """
    #if vaildate is true, pop in tableau for that column and move to correct column
    if validate_move_within_tableau(tableau, from_col, to_col) == True:
        tableau[to_col].append(tableau[from_col][-1])
        tableau[from_col].pop()
        
def check_for_win( tableau, stock ):
    """
    See if player won the game

    Parameters
    ----------
    tableau : List
        Lists of lists of card that get dealed to.
    stock : Class
        is the stock of cards in the game.

    Returns
    -------
    bool
        Returns True or False, True if win game

    """
    #Intilize counter to see how many aces are in the foundation
    ace_num = 0
    for lists in tableau:
        #If anything other than ace is in the foundation return False
        for card in lists:
            if card.value() == 1:
                ace_num += 1
            else:
                return False
    #If four aces are in the foundation return True
    if len(stock)==0:
        if ace_num <= 4:
            return True
    else:
        return False
            
                
def display( stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')
                
        print()

def get_option():
    """
    Aquires input from user

    Returns
    -------
    list
        Returns list of the option chosen by player.

    """
    #Gather input from user
    inp = input("\nInput an option (DFTRHQ): ")
    option = inp.strip().upper()
    #If any of thse options are selected return corresponding letter
    if option == "D" or option == "R" or option == "H" or option == "Q":
        return [option]
    #If "F" or "T" selected return corresponding letter and numbers
    if option[0] == "F" and len(option) == 3 and 0 < int(option[2]) < 5:
        return ["F", int(option[2])-1]
    if option[0] == "T" and len(option) == 5 and 0 < int(option[2]) < 5 and 0 < int(option[4]) < 5:
        return ["T", int(option[2])-1, int(option[4])-1]
    else:
        print("\nError in option: {}".format(inp))
        return []

def main():
    """
    Prints respective option    
    
    Returns
    -------
    None.
    
    """  
    #Prints game rules and menu
    #Calls all necessary function
    #Prints respective data based on option selected
    print(RULES)
    print(MENU)
    tuplex = init_game()
    stock = tuplex[0]
    tableau = tuplex[1]
    foundation = tuplex[2]
    display(stock, tableau, foundation)
    option = get_option()
    while len(option) == 0 or option[0] != "Q":
        if len(option) == 0:
            option = get_option()
            continue
        if option[0] == "D":
            deal_to_tableau(tableau, stock)
                
        if option[0] == "F":
            move_to_foundation(tableau, foundation ,option[1])
                
        if option[0] == "T":
            move_within_tableau(tableau, option[1], option[2])
                    
        if option[0] == "R":
            print("\n=========== Restarting: new game ============")
            print(RULES)
            print(MENU)
            stock, tableau, foundation = init_game()
        if option[0] == "H":
            print(MENU)
        if check_for_win(tableau, stock):
            print("\nYou won!")
            break
        else:
            display(stock, tableau, foundation)
            option = get_option()
    #if chosen to quit the game
    if option[0] == "Q":
        print("\nYou have chosen to quit.")
   
if __name__ == '__main__':
     main()
