import re


def count_games(file_name):
    with open(file_name, 'r') as input_file:
        content = input_file.read()
        lineCount = len(re.split("\n", content))
        words = re.split("\W+", content.lower())
    return lineCount


def decide(file_name, year):
    with open(file_name, "r") as input_file:
        content = input_file.readlines()
        years = list()
        for line in content:
            words = line.split("\t")
            years.append(words[2])
            boolean = False
            if str(year) in years:
                boolean = True
        return boolean


def get_latest(file_name):
    with open(file_name, "r") as input_file:
        content = input_file.readlines()
        latest_year = {}
        for line in content:
            words = line.split("\t")
            latest_year.update({words[0]: words[2]})
        latest_title = str(max(latest_year, key=latest_year.get))
        return latest_title


def count_by_genre(file_name, genre):
    with open(file_name, "r") as input_file:
        content = input_file.readlines()
        all_genres = list()
        for line in content:
            words = line.split("\t")
            all_genres.append(words[3])
        index = 0
        for i in all_genres:
            if i == genre:
                index += 1
    return index


def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as input_file:
        content = input_file.readlines()
        all_titles = list()
        for line in content:
            words = line.split("\t")
            all_titles.append(words[0])
        try:
            title in all_titles
        except ValueError:
            return all_titles
        title_number = all_titles.index(title) + 1
        return title_number


def sort_abc(file_name):
    with open(file_name, "r") as input_file:
        content = input_file.readlines()
        all_titles = list()
        for line in content:
            words = line.split("\t")
            all_titles.append(words[0])
        lenght = len(all_titles)
        for i in range(0, 23):
            for j in range(i + 1, 24):
                if all_titles[j] < all_titles[i]:
                    abc_titles = all_titles[j]
                    all_titles[j] = all_titles[i]
                    all_titles[i] = abc_titles
        return all_titles


def get_genres(file_name):
    with open(file_name, "r") as input_file:
        content = input_file.readlines()
        all_genres = list()
        for line in content:
            words = line.split("\t")
            if words[3] not in all_genres:
                all_genres.append(words[3])
        return sorted(all_genres, key=str.lower)


def when_was_top_sold_fps(file_name):
    with open(file_name, "r") as input_file:
        content = input_file.readlines()
        game = {}
        game_type = "First-person shooter"
        for line in content:
            words = line.split("\t")
            if str(words[3]) == game_type:
                words[1] = float(words[1])
                game.update({words[2]: words[1]})
        year_of_the_release = max(game, key=game.get)
        return int(year_of_the_release)
