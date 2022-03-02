from helper_fxns import *
import os

def main_menu():
    print('Choose an option to get started:')
    print('1 - Add or edit data')
    print('2 - Analyze data')
    print('3 - Exit app')
    resp = input("Choice: ")

    if resp == '1':
        data_menu()
    if resp == '2':
        analysis_menu()
    if resp == '3':
        os._exit(0)

    if resp != '1' or resp != '2' or resp != '3':
        print("Invalid response. Choose 1, 2, or 3.")
        print("")
        print("")
        main_menu()



def analysis_menu():
    print("")
    print("")
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
    resp = int(input('Select an option: '))



    if resp == 1:
        create_new_menu()
    elif resp == 2:
        edit_menu()
    elif resp == 3:
        del_menu()
    elif resp == 4:
        main_menu()
    if resp != 1 or resp != 2 or resp != 3 or resp != 4:
        print("Invalid response. Choose a number 1-4")
        print("")
        print("")
        data_menu()


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

def edit_menu(date=None):
    if date is None:
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

    option = int(input("Choice: "))

    if option not in list(range(1, 12)):
        print("Invalid choice. Choose a number 1-11")
        edit_menu(date)

    if option == 1:
        print_out_date(date)
        print("")
        print("")
        edit_menu(date)

    if option == 2:
        new_food = input("Food to add (only one item at a time): ")
        add_food(new_food, date)
        edit_menu(date)

    if option == 3:
        food_to_remove = input("Food to remove (only one at a time): ")
        remove_food(food, date)
        edit_menu(date)

    if option == 4:
        sleep_hours = input("How many hours of sleep: ")
        edit_sleep(sleep_hours, date)
        edit_menu(date)

    if option == 5:
        steps = input("How many steps: ")
        edit_steps(steps, date)
        edit_menu(date)

    if option == 6:
        poop_menu(date)

    if option == 7:
        physical_menu(date)

    if option == 8:
        mental_menu(date)

    if option == 9:
        vomit_menu(date)

    if option == 10:
        edit_menu(date=None)

    if option == 11:
        data_menu()


def poop_menu(date):
    print("")
    print("""
    Select the option that most fits your poop:
1 - normal
2 - diarrhea
3 - food present
4 - no poop / constipated
5 - blood
    """)
    option = int(input("Choice: "))
    if option not in list(range(1, 6)):
        print("Invalid choice. Choose a number 1-5")
        poop_menu(date)
    poop_list = ['normal', 'diarrhea', 'food present', 'constipated', 'blood']
    edit_poop(date = date, poop_quality = poop_list[option-1])
    edit_menu(date)



def physical_menu(date):
    print("")
    print("""
    Select the option that most fits your physical feeling today:
1 - good
2 - bloated
3 - light
4 - nauseous
    """)
    option = int(input("Choice: "))
    if option not in list(range(1, 5)):
        print("Invalid choice. Choose a number 1-4")
        physical_menu(date)
    physical_list =  ['good', 'bloated', 'light', 'nauseous']
    edit_physical(date = date, physical_feeling = physical_list[option-1])
    edit_menu(date)

def mental_menu(date):
    print("")
    print("""
    Select the option that most fits your mental state:
1 - clear
2 - foggy/tired
3 - stressed
4 - apathetic
    """)
    option = int(input("Choice: "))
    if option not in list(range(1, 5)):
        print("Invalid choice. Choose a number 1-4")
        mental_menu(date)
    mental_list = ['clear', 'foggy/tired', 'stressed', 'apathetic']
    edit_mental(date = date, mental_feeling= mental_list[option-1])
    edit_menu(date)

def vomit_menu(date):
    print("")
    print("""
Did you vomit on this day? (1) Yes (2) No
    """)
    choice = int(input("Choice: "))
    if choice not in list(range(1, 3)):
        print("Invalid choice. Choose a number 1-2")
        vomit_menu(date)
    if choice == 1:
        v = True
    else:
        v = False
    edit_vomit(date = date, vomit = v)
    edit_menu(date)




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
