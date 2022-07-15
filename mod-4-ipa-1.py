'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    a_follows_b = to_member in social_graph[from_member]["following"]
    b_follows_a = from_member in social_graph[to_member]["following"]
    
    if a_follows_b != False and b_follows_a != False:
        return "friends"
    else: 
        if a_follows_b != False: 
            return "follower"
        else: 
            if b_follows_a != False:
                return "followed by"
            else:
                return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    board_proportions = len(board)

    topbottom = [board[i][i] for i in range(board_proportions)]
    x_topbottom_diagonal = topbottom.count("X")
    o_topbottom_diagonal = topbottom.count("O")
    
    bottomtop = [board[i][board_proportions-i-1] for i in range(board_proportions)]
    x_bottomtop_diagonal = bottomtop.count("X")
    o_bottomtop_diagonal = bottomtop.count("O")
    
    vertical = [z for z in zip(*board)]
    x_vertical_win = [vertical[i].count("X") == board_proportions for i in range(board_proportions)] 
    o_vertical_win = [vertical[i].count("O") == board_proportions for i in range(board_proportions)]

    x_horizontal_win = [board[i].count("X") == board_proportions for i in range(board_proportions)]
    o_horizontal_win = [board[i].count("O") == board_proportions for i in range(board_proportions)]
    
    if x_topbottom_diagonal == board_proportions or x_bottomtop_diagonal == board_proportions or True in x_vertical_win or True in x_horizontal_win:
        return "X"

    elif o_topbottom_diagonal == board_proportions or o_bottomtop_diagonal == board_proportions or True in o_vertical_win or True in o_horizontal_win:
        return "O"
    
    else:
        return "NO WINNER"
    
    ___
#[board[i][board_proportions-i-1] for i in range(board_length)]

#for space in zip(*board) #vertical lengths

#for x in board #horizontal match 

#[board[i][i] for i in range(board_length)] traverse upper left to lower right

#[board[3-1-i][i] for i in range(board_length)] traverse upper right to lower left

#use later for TIC TAC TOE thing, to validate 2.) vertical objects are the same

#horizontal_win = space == 'X' or space == 'O' for space in board1


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    travel_time = 0
    current_stop = first_stop
    
    if first_stop == second_stop:
        legs_times = [t['travel_time_mins'] for t in route_map.values()]
        return sum(legs_times)
        
    else:
        while current_stop != second_stop:
            for leg, travel_time_mins in legs.items():
                if leg[0] == current_stop:
                    travel_time += travel_time_mins['travel_time_mins']
                    current_stop = leg[1]    
                if current_stop == second_stop:
                    break
        return(travel_time)
