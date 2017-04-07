
import config
import reports


# Global variables
SOURCE_DATA = config.source
REPORT_FILE = config.target
YEAR = config.year
GENRE = config.genre
TITLE = config.title


# Export functions
def write_to_file_all(source_data, report_file, year, genre, title):
    '''
    Write package 1 reports to a file.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @param    year          int      Year parameter for inside function
        @param    genre         string   Genre parameter for inside function
        @param    title         string   Title parameter for inside function
        @return   bool                   True if successful, otherwise False
    '''
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(str(reports.count_games(source_data)) + '\n')
            f.write(str(reports.decide(source_data, year)) + '\n')
            f.write(str(reports.get_latest(source_data)) + '\n')
            f.write(str(reports.count_by_genre(source_data, genre)) + '\n')
            f.write(str(reports.get_line_number_by_title(source_data, title)) + '\n')
            f.write(str(', '.join(reports.sort_abc(source_data))) + '\n')
            f.write(str(', '.join(reports.get_genres(source_data))) + '\n')
            f.write(str(reports.when_was_top_sold_fps(source_data)))
    except:
        result = False
        raise
    else:
        result = True

    return result


def append_to_file(source_data, report_file, what):
    '''
    Append report to a file.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @param    what          string   The new line to be appended to the report file
        @return                 bool     True if successful, otherwise False
    '''
    try:
        with open(report_file, 'a', encoding='utf-8') as f:
            f.write(str(what) + '\n')
    except:
        result = False
    else:
        result = True

    return result


def export_count_games(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string    Name of the file that contains source data
        @param    report_file   string    Name of the file to be created
        @return   bool                    True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.count_games(source_data)) else False
    return result


def export_decide(source_data, report_file, year):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @param    year          int      Year parameter for inside function
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.decide(source_data, year)) else False
    return result


def export_get_latest(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.get_latest(source_data)) else False
    return result


def export_count_by_genre(source_data, report_file, genre):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @param    genre         string   Genre parameter for inside function
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.count_by_genre(source_data, genre)) else False
    return result


def export_get_line_number_by_title(source_data, report_file, title):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @param    title         string   Title parameter for inside function
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file,
                                    reports.get_line_number_by_title(source_data, title)) else False
    return result


def export_sort_abc(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    data = ', '.join(reports.sort_abc(source_data))
    result = True if append_to_file(source_data, report_file, data) else False
    return result


def export_get_genres(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    data = ', '.join(reports.get_genres(source_data))
    result = True if append_to_file(source_data, report_file, data) else False
    return result


def export_when_was_top_sold_fps(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.when_was_top_sold_fps(source_data)) else False
    return result


def delete_content(file_name):
    '''
    Delete contents of a file
        @param    file_name   string   Name of the file of which content will be deleted
        @result               bool     True if successful, otherwise False
    '''
    try:
        with open(file_name, "w"):
            pass
    except:
        result = False
    else:
        result = True

    return result


def export_reports():
    '''
    Export all reports to file.
        @return   string   Status message
    '''

    if delete_content(REPORT_FILE):

        check_result = []

        check_result.append(export_count_games(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_decide(SOURCE_DATA, REPORT_FILE, YEAR))
        check_result.append(export_get_latest(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_count_by_genre(SOURCE_DATA, REPORT_FILE, GENRE))
        check_result.append(export_get_line_number_by_title(SOURCE_DATA, REPORT_FILE, TITLE))
        check_result.append(export_sort_abc(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_get_genres(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_when_was_top_sold_fps(SOURCE_DATA, REPORT_FILE))

        if all(check_result):
            print('Reports exported successfully!')
        else:
            print('An error occured. Please check your source file or you entered a wrong file name for output.')
    else:
        print('An error occured while deleting previous contents of the report file. \
Please close the file and try again.')


def main():
    export_reports()

if __name__ == '__main__':
    main()
