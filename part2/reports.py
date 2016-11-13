
def get_most_played(file_name):
    with open(file_name, 'r') as input_file:
        content = input_file.readlines()
        most_played = ''
        most_copied_sold = 0
        for line in content:
            title, copies, _, _, _ = line.split('\t')
            copies = float(copies)
            if copies > most_copied_sold:
                most_copied_sold = copies
                most_played = title
    return most_played


def sum_sold(file_name):
    with open(file_name, 'r') as input_file:
        content = input_file.readlines()
        total_copies = 0
        for line in content:
            _, copies, _, _, _ = line.split('\t')
            copies = float(copies)
            total_copies = total_copies + copies
    return total_copies


def get_selling_avg(file_name):
    with open(file_name, 'r') as input_file:
        total_copies = sum_sold(file_name)
        content = input_file.readlines()
        number_of_games = len(content)
        average = total_copies / number_of_games
    return average


def count_longest_title(file_name):
    with open(file_name, 'r') as input_file:
        content = input_file.readlines()
        length_of_titles = []
        for line in content:
            title, _, _, _, _ = line.split('\t')
            length_of_titles.append(len(title))
    return max(length_of_titles)


def get_date_avg(file_name):
    with open(file_name, 'r') as input_file:
        content = input_file.readlines()
        release_dates = []
        for line in content:
            _, _, release_date, _, _ = line.split('\t')
            release_date = int(release_date)
            release_dates.append(release_date)
        average = sum(release_dates) / len(release_dates)
    return round(average)


def get_game(file_name, title):
    games = {}
    with open(file_name, 'r') as input_file:
        content = input_file.readlines()
        for line in content:
            line = line.strip()
            game_title, copies, release_date, genre, label = line.split('\t')
            games[game_title] = [game_title, float(copies), int(release_date), genre, label]
    return games[title]
