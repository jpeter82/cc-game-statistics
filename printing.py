
import config
import reports

SOURCE_FILE = config.source
YEAR = config.year
GENRE = config.genre
TITLE = config.title


# Printing functions
def report_count_games(filename):
    '''
    Prints out results of Question #1
        @return void
    '''
    print('\nNumber of games in the file:', reports.count_games(filename))


def report_decide(filename, year):
    '''
    Prints out results of Question #2
        @return void
    '''
    print('\nThere is at least one game from {}: {}'.format(year, reports.decide(filename, year)))


def report_get_latest(filename):
    '''
    Prints out results of Question #3
        @return void
    '''
    print('\nThe latest game is:', reports.get_latest(filename))


def report_count_by_genre(filename, genre):
    '''
    Prints out results of Question #4
        @return void
    '''
    print('\nNumber of games in {} category: {}'.format(str(genre), reports.count_by_genre(filename, str(genre))))


def report_get_line_number_by_title(filename, title):
    '''
    Prints out results of Question #5
        @return void
    '''
    print('\nThe line number for {}: {}'.format(str(title), reports.get_line_number_by_title(filename, title)))


def report_sort_abc(filename):
    '''
    Prints out results of Extra Question #1
        @return void
    '''
    report = reports.sort_abc(filename)
    print('\nThe alphabetical ordered list of titles:\n')
    [print(title) for title in report] if isinstance(report, list) else print(report)


def report_get_genres(filename):
    '''
    Prints out results of Extra Question #2
        @return void
    '''
    report = reports.get_genres(filename)
    print('\nGenres in alphabetical order:\n')
    [print(title) for title in report] if isinstance(report, list) else print(report)


def report_when_was_top_sold_fps(filename):
    '''
    Prints out results of Extra Question #3
        @return void
    '''
    print('\nRelease date of the top sold "First-person shooter" game:', reports.when_was_top_sold_fps(filename))


def print_reports():
    '''
    Print out all reports to the screen.
        @return void
    '''
    print('\nREPORT #1 for Judy')
    print('------------------')
    report_count_games(SOURCE_FILE)
    report_decide(SOURCE_FILE, YEAR)
    report_get_latest(SOURCE_FILE)
    report_count_by_genre(SOURCE_FILE, GENRE)
    report_get_line_number_by_title(SOURCE_FILE, TITLE)
    report_sort_abc(SOURCE_FILE)
    report_get_genres(SOURCE_FILE)
    report_when_was_top_sold_fps(SOURCE_FILE)
    print('\n----------------')
    print('END OF REPORT #1')


def main():
    print_reports()

if __name__ == '__main__':
    main()
