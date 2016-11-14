from reports import *

with open("game_answers.txt", "w+") as input_file:
    input_file.write("1. " + get_most_played("game_stat.txt") + "\n")
    input_file.write("2. " + str(sum_sold("game_stat.txt")) + "\n")
    input_file.write("3. " + str(get_selling_avg("game_stat.txt")) + "\n")
    input_file.write("4. " + str(count_longest_title("game_stat.txt")) + "\n")
    input_file.write("5. " + str(get_date_avg("game_stat.txt")) + "\n")