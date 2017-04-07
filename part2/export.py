
import config
import reports


# Global variables
SOURCE_DATA = config.source
REPORT_FILE = config.target
TITLE = config.title


# Export functions
def write_to_file(source_data, report_file, title):
    '''
    Write package 2 reports to a file.
        @param    source_data   string    Name of the file that contains source data
        @param    report_file   string    Name of the file to be created
        @param    title         string    Title parameter for inside function
        @return                 bool      True if successful, otherwise False
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


def append_to_file(source_data, report_file, what):
    '''
    Append report to a file.
        @param    source_data   string    Name of the file that contains source data
        @param    report_file   string    Name of the file to be created
        @param    what          string    The new line to be appended to the report file
        @return                 bool      True if successful, otherwise False
    '''
    try:
        with open(report_file, 'a', encoding='utf-8') as f:
            f.write(str(what) + '\n')
    except:
        result = False
    else:
        result = True

    return result


def export_get_most_played(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.get_most_played(source_data)) else False
    return result


def export_sum_sold(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.sum_sold(source_data)) else False
    return result


def export_get_selling_avg(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string    Name of the file that contains source data
        @param    report_file   string    Name of the file to be created
        @return                 bool      True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.get_selling_avg(source_data)) else False
    return result


def export_count_longest_title(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.count_longest_title(source_data)) else False
    return result


def export_get_date_avg(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    result = True if append_to_file(source_data, report_file, reports.get_date_avg(source_data)) else False
    return result


def export_get_game(source_data, report_file, title):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @param    title         string   Title parameter for inside function
        @return                 bool     True if successful, otherwise False
    '''
    data = ', '.join(str(item) for item in reports.get_game(source_data, title))
    result = True if append_to_file(source_data, report_file, data) else False
    return result


def export_count_grouped_by_genre(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    data = ', '.join((str(key) + ': ' + str(value)) for key, value
                     in reports.count_grouped_by_genre(source_data).items())
    result = True if append_to_file(source_data, report_file, data) else False
    return result


def export_get_date_ordered(source_data, report_file):
    '''
    Append actual report to report file. Check out reports.py for content of actual report.
        @param    source_data   string   Name of the file that contains source data
        @param    report_file   string   Name of the file to be created
        @return                 bool     True if successful, otherwise False
    '''
    data = ', '.join(reports.get_date_ordered(source_data))
    result = True if append_to_file(source_data, report_file, data) else False
    return result


def delete_content(file_name):
    '''
    Delete contents of a file
        @param   file_name   string   Name of the file of which content will be deleted
        @result              bool     True if successful, otherwise False
    '''
    try:
        with open(file_name, "w"):
            pass
    except:
        result = False
    else:
        result = True

    return result


def main():

    if delete_content(REPORT_FILE):
        check_result = []

        check_result.append(export_get_most_played(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_sum_sold(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_get_selling_avg(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_count_longest_title(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_get_date_avg(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_get_game(SOURCE_DATA, REPORT_FILE, TITLE))
        check_result.append(export_count_grouped_by_genre(SOURCE_DATA, REPORT_FILE))
        check_result.append(export_get_date_ordered(SOURCE_DATA, REPORT_FILE))

        if all(check_result):
            print('Reports exported successfully!')
        else:
            print('An error occured. Please check your source file.')
    else:
        print('An error occured while deleting previous contents of the report file. \
Please close the file and try again.')

if __name__ == '__main__':
    main()
