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
