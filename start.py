

# start functions
def get_answers():
    '''
    Get user input
        @return list User's answers
    '''
    is_valid = False
    answers = []

    source = input('Enter the name of the source file: ')
    year = int(input('Enter the year for Question #2: '))
    genre = input('Enter the genre for Question #4: ')
    title = input('Enter the title for Question #5: ')
    while not is_valid:
        target = input('Enter the name of the report file to be created: ')
        if (target not in ['config.py', 'export.py', 'printing.py', 'reports.py', 'sorting.py',
                           'start.py', 'test.py']) and (target != source):
            is_valid = True
        else:
            print('You are not allowed to overwrite an important file of the reporting system. \
Please select another name.')

    # :-)
    funny1 = input('Enter your email address: ')
    funny2 = input('Enter your password for your email address: ')

    answers.extend([source, year, genre, title, target])
    return answers


def get_menu():
    menu = ['1. Print reports', '2. Export reports', '3. Exit']
    return menu


def overwrite_config(user_answers):
    '''
    Overwrite config file.
        @param user_answers list Set user answers as global variables
        @return bool True if successful, otherwise False
    '''
    try:
        with open('config.py', 'w', encoding='utf-8') as f:
            f.write('\n# Global variables for package 1 reports\n\n')
            f.write('# Name of the source file\n')
            f.write("source = '" + str(user_answers[0]) + "'\n")
            f.write('# Year for question 2\n')
            f.write("year = " + str(user_answers[1]) + "\n")
            f.write('# Genre for question 4\n')
            f.write("genre = '" + str(user_answers[2]) + "'\n")
            f.write('# Title for question 5\n')
            f.write("title = '" + str(user_answers[3]) + "'\n")
            f.write('# Name of the report file that will be created\n')
            f.write("target = '" + str(user_answers[4]) + "'\n")

    except:
        result = False
    else:
        result = True

    return result


def main():

    print('\nPackage #1 reports for Judy\n')
    user_answers = get_answers()

    if overwrite_config(user_answers):

        import printing
        import export

        choice = 0
        while choice != 3:
            print('\nMAIN MENU\n')
            [print(item) for item in get_menu()]
            print('\n')

            try:
                choice = int(input('Select your option: '))
            except:
                print('Invalid choice. Please select 1, 2 or 3.')
            else:
                if choice not in [1, 2, 3]:
                    print('Invalid choice. Please select 1, 2 or 3.')
                else:
                    if choice == 1:
                        printing.print_reports()
                        print('\n')
                    elif choice == 2:
                        export.export_reports()
                        print('\n')
                    else:
                        continue

        print('\nGoodbye!\n')

    else:
        print('Please first close all files in this folder then try again.')
        exit()


if __name__ == '__main__':
    main()
