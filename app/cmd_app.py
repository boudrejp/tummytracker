from helper_fxns import *

def main_menu():
    print('Choose an option to get started:')
    print('1 - Add or edit data')
    print('2 - Analyze data')
    print('3 - Exit app')
    resp = input("Choice: ")

    if resp == 1:
        data_menu()
    if resp == 2:
        analysis_menu()
    if resp == 3:
        quit()

    if resp != 1 or resp != 2:
        print("Invalid response. Choose 1, 2, or 3.")
        print("")
        print("")
        main_menu()

def analysis_menu():
    print("Sorry, analysis is still a work in progress!")
    print("Returning to main menu")
    print("")
    print("")
    main_menu()

def data_menu():
    print("""
    Select an option:
    1 - Create database / add new date to database
    2 - Edit existing date in database
    3 - Remove data in database
    4 - Main menu
    """)
    resp = input('Select an option: ')

    if resp != 1 or resp != 2 or resp != 3 or resp != 4:
        print("Invalid response. Choose a number 1-4")
        print("")
        print("")
        data_menu()

    if resp == 1:
        create_new_menu()
    elif resp == 2:
        edit_menu()
    elif resp == 3:
        del_menu()
    elif resp == 4:
        main_menu()

def create_new_menu():
    print('Select a date in yyyy-mm-dd format to initialize or add to DB')
    date = input('Date: ')
    add_new_date(date = date)

    print("Date added in data file")
    data_menu()

def del_menu():
    print("Select a date in yyyy-mm-dd format to remove from DB")
    date = input('Date: ')
    delete_date(date = date)
    print("Date deleted from DB")
    data_menu()

def edit_menu():
    print("Select a date in yyyy-mm-dd format to edit: ")
    date = input("Date: ")
    print("")
    print("")
    print(f"Currently editing: {date}")
    print("""
        Select an option:
        1 - Print current date data
        2 - Add food
        3 - Remove food
        4 - Edit sleep hours
        5 - Edit steps
        6 - Edit poop quality
        7 - Edit physical feeling
        8 - Edit mental feeling
        9 - Edit vomit
        10 - Edit date
        11 - Data menu
    """)

    option = input("Choice :")

    if option not in list(range(1, 12)):
        print("Invalid choice. Choose a number 1-11")
        edit_menu()
    
    if option == 1:
        print_out_date(date)
        print("")
        print("")
        edit_menu()

    if option == 2:
        new_food = input("Food to add (only one item at a time): ")
        add_food(new_food, date)
        edit_menu()

    if option == 3:
        food_to_remove = input("Food to remove (only one at a time): ")
        remove_food(food, date)
        edit_menu()

    if option == 4:
        sleep_hours = input("How many hours of sleep: ")
        edit_sleep(sleep_hours, date)
        edit_menu()

    if option == 5:
        steps = input("How many steps: ")
        edit_steps(steps, date)
        edit_menu()

    if option == 6:
        poop_menu()
    
    if option == 7:
        physical_menu()

    if option == 8:
        mental_menu()

    if option == 9:
        vomit_menu()

    if option == 10:
        edit_menu()

    if option == 11:
        data_menu()


def poop_menu():
    




print("""

████████╗██╗░░░██╗███╗░░░███╗███╗░░░███╗██╗░░░██╗  ████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
╚══██╔══╝██║░░░██║████╗░████║████╗░████║╚██╗░██╔╝  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░░░██║░░░██║░░░██║██╔████╔██║██╔████╔██║░╚████╔╝░  ░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░░██║░░░██║░░░██║██║╚██╔╝██║██║╚██╔╝██║░░╚██╔╝░░  ░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░░██║░░░╚██████╔╝██║░╚═╝░██║██║░╚═╝░██║░░░██║░░░  ░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")

print('- a way to track your food and see how it affects your well-being -')

print('')
print('')

main_menu()