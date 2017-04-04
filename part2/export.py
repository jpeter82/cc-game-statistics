
import config
import reports


# Global variables
SOURCE_DATA = config.source
REPORT_FILE = config.target
TITLE = config.title


# Export functions
def write_to_file(source_data, report_file, title):
    '''
    Write package 1 reports to a file.
        @param report_file string Name of the file to be created
        @return bool True if successful, otherwise False
    '''
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(str(reports.get_most_played(source_data)) + '\n')
            f.write(str(reports.sum_sold(source_data)) + '\n')
            f.write(str(reports.get_selling_avg(source_data)) + '\n')
            f.write(str(reports.count_longest_title(source_data)) + '\n')
            f.write(str(reports.get_date_avg(source_data)) + '\n')
            f.write(', '.join(str(item) for item in reports.get_game(source_data, title)) + '\n')
            f.write(', '.join((str(key) + ': ' + str(value)) for key, value
                    in reports.count_grouped_by_genre(source_data).items()) + '\n')
            f.write(str(', '.join(reports.get_date_ordered(source_data))))
    except:
        result = False
        raise
    else:
        result = True

    return result


def main():
    # print(write_to_file(SOURCE_DATA, REPORT_FILE, TITLE))
    write_to_file(SOURCE_DATA, REPORT_FILE, TITLE)

if __name__ == '__main__':
    main()
