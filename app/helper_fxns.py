import json
import numpy as np
import pandas as pd
from os import path

filepath = "../data/daily_data.json"

def initialize_data():
    data = [{}]
    with open(filepath, "w") as write_file:
        json.dump(data, write_file)

def find_date(date:str, json_obj):
    return [obj for obj in json_obj if obj['date'] == date][0]

def add_new_date(date: str, verbose = False):

    # check to see if data exists
    if path.isfile(filepath) is False:
        if verbose:
            print('new data file created')
        initialize_data()

    # load data and write
    with open(filepath) as fp:
        listobj = json.load(fp)
    try:
        find_date(date)
        print(f"Date {date} already exists. Edit to make changes")
        return
    except:
        listobj.append({
            'date': date,
            'food': [],
            'sleep_hours': np.nan,
            'steps' : np.nan,
            'poop_quality': np.nan,
            'physical_feeling': np.nan,
            'mental_feeling': np.nan
            })

        with open(filepath, 'w') as json_file:
            json.dump(listobj, json_file,
                indent = 4,
                separators = (',', ': '))
        if verbose:
            print("Successfully created new date in daily_data.json")

#####################
### rethink these...
#####################

def add_food(food_list: list, new_food: str):
    if path.isfile(filepath) is False:
        if verbose:
            print('new data file created')
        initialize_data()

    with open(filepath) as fp:
        listobj = json.load(fp)

    # find the date
    try:
        entry = find_date()
    except:
        print('Date not found in database')
        return

    entry['food'].append(new_food)
    

def remove_food(food_list: list, food: str):
    try:
        ret_list = food_list.remove(food)
    except:
        print(f"Food {food} was not found")
        ret_list = food_list
    return ret_list

def edit_sleep(sleep_hours: float):
    return sleep_hours

def edit_steps(steps: int):
    return steps

def edit_date(date: str, param, item):
    accepted_params = [
                'food',
                'sleep_hours',
                'steps',
                'poop_quality',
                'physical_feeling',
                'mental_feeling']

    if param not in accepted_params:
        print("Invalid parameter")
        return
    # check to see if data exists
    if path.isfile(filepath) is False:
        if verbose:
            print('new data file created')
        initialize_data()

    with open(filepath) as fp:
        listobj = json.load(fp)

    # find the date
    try:
        entry = find_date()
    except:
        print('Date not found in database')
        return






def remove_date(date: str):
    # something
