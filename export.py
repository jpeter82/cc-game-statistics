
import config
import reports


# Global variables
SOURCE_DATA = config.source
REPORT_FILE = config.target
YEAR = config.year
GENRE = config.genre
TITLE = config.title


# Export functions
def write_to_file(source_data, report_file, year, genre, title):
    '''
    Write package 1 reports to a file.
        @param report_file string Name of the file to be created
        @return bool True if successful, otherwise False
    '''
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(str(reports.count_games(source_data)) + '\n')
            f.write(str(reports.decide(source_data, year)) + '\n')
            f.write(str(reports.get_latest(source_data)) + '\n')
            f.write(str(reports.count_by_genre(source_data, genre)) + '\n')
            f.write(str(reports.get_line_number_by_title(source_data, title)) + '\n')
            f.write(str(reports.sort_abc(source_data)) + '\n')
            f.write(str(reports.get_genres(source_data)) + '\n')
            f.write(str(reports.when_was_top_sold_fps(source_data)))
    except:
        result = False
        raise
    else:
        result = True

    return result


def main():
    print(write_to_file(SOURCE_DATA, REPORT_FILE, YEAR, GENRE, TITLE))

if __name__ == '__main__':
    main()
