import random
from reconchess import *

# Settings for the opponent
class RandomBot(Player):

    """"
    This function is for the start of the game, lowercase color, board, and opponent_name
    are all function annotations. Color is a boolean variable that refers to the
    color of the bot's piece. True means white and vice versa. chess.Board sets the
    chess board with all the pieces in their starting position. The argument labeled
    opponent_name takes the opponent's name as a string.
    """
    def handle_game_start(self, color: Color, board: chess.Board, opponent_name: str):
        pass

    """
    This function responds to the players move. captured_my_piece is a boolean variable.
    True means that the bot's piece was captured and vice versa. If the boolean is true the
    function will take the optional argument capture_square. This refers to the square where
    the bot's piece was captured. Altogether, this function removes the piece that was captured
    from the board.
    """
    def handle_opponent_move_result(self, captured_my_piece: bool, capture_square: Optional[Square]):
        pass

    """
    This function senses the possible moves the bot has in the 3x3 square area in front of it. 
    sense_actions is a list of the possible squares the function can sense over. move_actions is
    a list of the valid moves within the 3x3 area. seconds_left is a float of how many seconds
    The Optional[Square] in this case is a function annotation that tells us the function has the
    option of returning a square. This function can either return a square to give you more 
    information about or it will return a None type variable and move on.
    """
    def choose_sense(self, sense_actions: List[Square], move_actions: List[chess.Move], seconds_left: float) -> \
            Optional[Square]:
        return random.choice(sense_actions)

    """
    This function takes the information from choose_sense and makes a list of tuples, where the 
    first value in the tuple is a square that has been sensed and the second value is the piece 
    that is on it. If there is no piece on any of the sensed squares, the tuple will just have 
    a None type variable, which is why chess.Piece is optional. 
    """
    def handle_sense_result(self, sense_result: List[Tuple[Square, Optional[chess.Piece]]]):
        pass

    """
    This function takes a list of the possible moves the bot can take (move_actions) and the 
    seconds the bot has left in the game as a float (seconds_left). The function annotation tells 
    us that the function has the option of returning a chosen move for the bot or it can return
    None and pass its turn.
    """
    def choose_move(self, move_actions: List[chess.Move], seconds_left: float) -> Optional[chess.Move]:
        return random.choice(move_actions + [None])

    """
    requested_move is the move that was chosen in the last function, and its optional because the 
    bot can choose to pass its turn. Taken move is the move that the bot actually takes and its 
    optional in the case that the bot passes or that the chosen move is invalid. 
    captured_opponent_piece is boolean variable which tell the function whether or not the bot 
    captured a piece with its taken moved. If captured_opponent_piece is True, the function 
    has the optional parameter capture_square, which is the square where the opponents piece was 
    captured. Basically returns information about the outcome of the bot's chosen move.
    """
    def handle_move_result(self, requested_move: Optional[chess.Move], taken_move: Optional[chess.Move],
                           captured_opponent_piece: bool, capture_square: Optional[Square]):
        pass

    """
    Gives results of the game, which color won, how they won, and the game history. The color and 
    reason are optional because it's possible that the game was a draw.
    """
    def handle_game_end(self, winner_color: Optional[Color], win_reason: Optional[WinReason],
                        game_history: GameHistory):
        pass