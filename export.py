from reports import *

with open("game_answers.txt", "w+") as input_file:
    input_file.write("1. " + str(count_games("game_stat.txt")) + "\n")
    input_file.write("2. " + str(decide("game_stat.txt", "2000")) + "\n")
    input_file.write("3. " + get_latest("game_stat.txt") + "\n")
    input_file.write("4. " + str(count_by_genre("game_stat.txt", "First-person shooter")) + "\n")
    input_file.write("5. " + str(get_line_number_by_title("game_stat.txt", "Counter-Strike")) + "\n")
    input_file.write("6. " + str(sort_abc("game_stat.txt")) + "\n")
    input_file.write("7. " + str(get_genres("game_stat.txt")) + "\n")
    input_file.write("8. " + str(when_was_top_sold_fps("game_stat.txt")) + "\n")
