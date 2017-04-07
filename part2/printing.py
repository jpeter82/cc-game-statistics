
import config
import reports

# Global variables
SOURCE_FILE = config.source
TITLE = config.title


# Printing functions
def report_get_most_played(filename):
    '''
    Prints out results of Question #1
        @return void
    '''
    print('\nTitle of the most played game:', reports.get_most_played(filename))


def report_sum_sold(filename):
    '''
    Prints out results of Question #2
        @return void
    '''
    print('\nTotal copies sold: {:.2f} million'.format(reports.sum_sold(filename)))


def report_get_selling_avg(filename):
    '''
    Prints out results of Question #3
        @return void
    '''
    print('\nSelling average: {:.2f} million'.format(reports.get_selling_avg(filename)))


def report_count_longest_title(filename):
    '''
    Prints out results of Question #4
        @return void
    '''
    print('\nNumber of characters in the longest title:', reports.count_longest_title(filename))


def report_get_date_avg(filename):
    '''
    Prints out results of Question #5
        @return void
    '''
    print('\nAverage of the release dates:', reports.get_date_avg(filename))


def report_get_game(filename, title):
    '''
    Prints out results of Question #6
        @return void
    '''
    game_details = reports.get_game(filename, title)
    print('\n{} has the following properties:'.format(title))
    [print(detail) for detail in game_details] if isinstance(game_details, list) else print(game_details)


def report_count_grouped_by_genre(filename):
    '''
    Prints out results of Extra Question #1
        @return void
    '''
    games_by_genre = reports.count_grouped_by_genre(filename)
    print('\nGames grouped by genre:')
    [print(game, count) for game, count in games_by_genre.items()] if isinstance(games_by_genre,
                                                                                 dict) else print(games_by_genre)


def report_get_date_ordered(filename):
    '''
    Prints out results of Extra Question #2
        @return void
    '''
    date_ordered = reports.get_date_ordered(filename)
    print('\nDate ordered list of the games:')
    [print(title) for title in date_ordered] if isinstance(date_ordered, list) else print(date_ordered)


def main():

    print('\nREPORT #2 for Judy')
    print('------------------')
    report_get_most_played(SOURCE_FILE)
    report_sum_sold(SOURCE_FILE)
    report_get_selling_avg(SOURCE_FILE)
    report_count_longest_title(SOURCE_FILE)
    report_get_date_avg(SOURCE_FILE)
    report_get_game(SOURCE_FILE, TITLE)
    report_count_grouped_by_genre(SOURCE_FILE)
    report_get_date_ordered(SOURCE_FILE)
    print('\n----------------')
    print('END OF REPORT #2')

if __name__ == '__main__':
    main()
