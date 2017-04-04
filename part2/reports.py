
# import math

# Report functions


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


def round_up(number):
    return int(-(-number // 1))


def get_most_played(file_name):
    '''
    Find the title of the most played game. If there is more than one, then it returns the first from the file
        @param file_name string Name of the file that contains the data
        @return string Title of the most played game or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            result = sorted([[float(line[1]), line_num + 1, line[0]] for line_num, line in enumerate(game_list[0])],
                            key=lambda x: (x[0], -x[1]), reverse=True)[0][2]
        except:
            result = 'At least one of the columns contain an invalid format, please check the source file.'
    else:
        result = game_list[1][0]

    return result


def sum_sold(file_name):
    '''
    Sum up copies sold
        @param file_name string Name of the file that contains the data
        @return float Total of copies sold or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            result = sum(float(line[1]) for line in game_list[0])
        except:
            result = 'The total copies sold column contains an invalid format, please check the source file.'
    else:
        result = game_list[1][0]

    return result


def get_selling_avg(file_name):
    '''
    Calculate average selling for the games
        @param file_name string Name of the file that contains the data
        @return float The average or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            selling = [float(line[1]) for line in game_list[0]]
        except:
            result = 'The total copies sold column contains an invalid format, please check the source file.'
        else:
            if len(selling) == 0:
                result = 'Average cannot be calculated (because of division by zero).'
            else:
                result = sum(selling) / len(selling)
    else:
        result = game_list[1][0]

    return result


def count_longest_title(file_name):
    '''
    Counts how many characters the longest title has
        @param file_name string Name of the file that contains the data
        @return int Number of characters or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        result = sorted([[line[0], len(line[0])] for line in game_list[0]], key=lambda x: x[1], reverse=True)[0][1]
    else:
        result = game_list[1][0]

    return result


def get_date_avg(file_name):
    '''
    Calculate the average of the release dates, rounded up
        @param file_name string Name of the file that contains the data
        @return int Average year rounded up or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            years = [int(line[2]) for line in game_list[0]]
        except:
            result = 'The year column contains at least one invalid format, please check the source file.'
        else:
            if len(years) == 0:
                result = 'Average cannot be calculated (because of division by zero).'
            else:
                result = round_up(sum(years) / len(years))
                # result = math.ceil(sum(years) / len(years))
    else:
        result = game_list[1][0]

    return result


def get_game(file_name, title):
    '''
    Create a list of game properties
        @param file_name string Name of the file that contains the data
        @param title string Title of the game
        @return list List of all the properties of the game or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            result = [[line[0], float(line[1]), int(line[2]), line[3], line[4]]
                      for line in game_list[0] if line[0] == str(title)][0]
        except:
            result = ('At least one of the columns contain an invalid format (probably total sold or years), \
                        please check the source file.')
    else:
        result = game_list[1][0]

    return result


def count_grouped_by_genre(file_name):
    '''
    Count number of games grouped by genre
        @param file_name string Name of the file that contains the data
        @return dict Dictionary of games where key is genre, value is number of games or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        result = {category: [line[3] for line in game_list[0]].count(category)
                  for category in set(line[3] for line in game_list[0])}
    else:
        result = game_list[1][0]

    return result


def get_date_ordered(file_name):
    '''
    Create ordered list of the games, date desc then title asc
        @param file_name string Name of the file that contains the data
        @return list List of titles or error message
    '''
    game_list = read_from_file(file_name)

    if game_list[0] is not False:
        try:
            result = [item[1] for item in
                      sorted([[int(line[2]), line[0]] for line in game_list[0]],
                             key=lambda x: (-x[0], str(x[1]).lower()))]
        except:
            result = ('At least one of the columns contain an invalid format (probably years), \
                        please check the source file.')
    else:
        result = game_list[1][0]

    return result


def main():
    pass

if __name__ == '__main__':
    main()
