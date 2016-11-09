from reports import count_games
from reports import decide
from reports import get_latest
from reports import count_by_genre
from reports import get_line_number_by_title

with open("game_answers.txt", "w+") as input_file:
    print("1. ", count_games("game_stat.txt"), file=input_file)
    print("2. ", decide("game_stat.txt", "2000"), file=input_file)
    print("3. ", get_latest("game_stat.txt"), file=input_file)
    print("4. ", count_by_genre("game_stat.txt", "First-person shooter") file=input_file)
    print("5. ", get_line_number_by_title("game_stat.txt"), file=input_file
