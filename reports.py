
# Report functions

import sorting


def read_from_file(file_name, separator='\t'):
    '''
    Read contents of a file and return it as a list.
    It assumes the file you want to read is in the same directory with this file.
        @param file_name string Name of the file to be read_from_file
        @param separator string Separator character for the file
        @return list Content of the file line by line as a list or False, Error message
    '''
    error = []
    result = []

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            game_list = [line.strip().split(separator) for line in f.readlines()]
    except:
        game_list = False
        error.append('An error occured while opening the file.')
    else:
        if len(game_list) < 1:
            game_list = False
            error.append('Empty file!')

    result.extend([game_list, error])
    return result


def count_games(file_name):
    '''
    Counts number of games in a file assuming there is one and only one game per every line
        @param file_name string Name of the file that contains the data
        @return int Number of games found in the file or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        result = int(len(game_list[0]))
    else:
        result = game_list[1][0]

    return result


def decide(file_name, year):
    '''
    Checks if there is a game from a given year
        @param file_name string Name of the file that contains the data
        @param year int The year to check
        @return bool True if a game is found, otherwise False or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        result = True if sum(line.count(str(year)) for line in game_list[0]) > 0 else False
    else:
        result = game_list[1][0]

    return result


def get_latest(file_name):
    '''
    Find the latest game by release date
        @param file_name string Name of the file that contains the data
        @return string The title of the latest game or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            max_year = max(set(int(line[2]) for line in game_list[0]))
            result = [line[0] for line in game_list[0] if int(line[2]) == max_year][0]
        except:
            result = 'There is at least one invalid value in the source file (possibly in the Year column).'
    else:
        result = game_list[1][0]

    return result


def count_by_genre(file_name, genre):
    '''
    Count games by given genre
        @param file_name string Name of the file that contains the data
        @param genre string Genre
        @return int The count of games by given genre or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        genres = [line[3] for line in game_list[0]]
        genre_dict = {category: genres.count(category) for category in set(genres)}
        result = genre_dict[genre] if genre in genre_dict.keys() else 0
    else:
        result = game_list[1][0]

    return result


def get_line_number_by_title(file_name, title):
    '''
    Find line number by given title
        @param file_name string Name of the file that contains the data
        @param title string Title of the game
        @return int The line number or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        '''
        Alternative long version:
        for count, line in enumerate(game_list):
            if str(title) == line[0]:
                return count + 1
        '''
        '''
        Alternative 2 version
        result = [line[0] + 1 for line in list(enumerate(game_list)) if str(title) == line[1][0]]
        return result[0]
        '''
        try:
            result = [count + 1 for count, line in enumerate(game_list[0]) if str(title) == line[0]][0]
        except:
            result = 'No such title in source file.'
            # raise ValueError
    else:
        result = game_list[1][0]
        # raise ValueError

    return result


def sort_abc(file_name):
    '''
    Create alphabetical ordered list of the titles
        @param file_name string Name of the file that contains the data
        @return list List of titles or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        # Sorted soulution
        # result = sorted([line[0] for line in game_list[0]], key=lambda x: x.lower())

        # Sorting my own way
        result = sorting.bubble_sort_ci([line[0] for line in game_list[0]])
    else:
        result = game_list[1][0]

    return result


def get_genres(file_name):
    '''
    Create a list of distinct genres in alphabetical order
        @param file_name string Name of the file that contains the data
        @return list List of genres or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        result = sorted(set(line[3] for line in game_list[0]), key=lambda x: x.lower())
    else:
        result = game_list[1][0]

    return result


def when_was_top_sold_fps(file_name):
    '''
    Find release date of the top sold "First-person shooter" game
        @param file_name string Name of the file that contains the data
        @return int Year of the release or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            result = sorted([(float(line[1]), int(line[2])) for line in game_list[0]
                            if line[3] == "First-person shooter"], key=lambda x: x[0], reverse=True)[0][1]
        except:
            result = ("Unexpected error occured. Either there is no First-person shooter category or \
at least one value is invalid in the 'year' column or in the 'total copies sold' column.")
            # raise ValueError
    else:
        result = game_list[1][0]

    return result


def main():
    pass

if __name__ == '__main__':
    main()
