import json
import numpy as np
import pandas as pd
from os import path

filepath = "../data/daily_data.json"

def initialize_data():
    data = {}
    with open(filepath, "w") as write_file:
        json.dump(data, write_file)

def find_date(date:str, json_obj):
    return json_obj[date]

def write_out(obj, filepath = filepath, verbose = False):
    with open(filepath, 'w') as json_file:
        json.dump(obj, json_file,
            indent = 4,
            separators = (',', ': '))
    if verbose:
        print("Successfully wrote out to daily_data.json")
    
def access_date_procedure(date:str, filepath = filepath):
    if path.isfile(filepath) is False:
        if verbose:
            print('new data file created')
        initialize_data()

    with open(filepath) as fp:
        listobj = json.loads(fp.read())
    # find the date
    try:
        entry = find_date(date, listobj)
        return listobj, entry
    except:
        print('Date not found in database')
        return

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
        listobj[date] = {
            'date': date,
            'food': [],
            'sleep_hours': np.nan,
            'steps' : np.nan,
            'poop_quality': np.nan,
            'physical_feeling': np.nan,
            'mental_feeling': np.nan,
            'vomit': False
            }

        write_out(listobj, verbose = verbose)

        if verbose:
            print("Successfully created new date in daily_data.json")


def add_food(new_food: str, date: str, verbose = False):

    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    # append the new food and put back into dict
    entry['food'].append(new_food)
    listobj[date] = entry
    
    # now write out dict to json
    write_out(listobj, verbose = verbose)

    

def remove_food(food: str, date: str, verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    # remove the food from the list
    try:
        entry['food'].remove(food)
    except:
        print(f'Food {food} not found in current list')
        return
    
    listobj[date] = entry
    
    # now write out dict to json
    write_out(listobj, verbose = verbose)

     
def edit_sleep(sleep_hours: float, date: str, verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    entry['sleep_hours'] = sleep_hours

    listobj['date'] = entry

    write_out(listobj, verbose = verbose)

    

def edit_steps(steps: int, date:str, verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    entry['steps'] = steps

    listobj['date'] = entry

    write_out(listobj, verbose = verbose)

def edit_poop(date:str, poop_quality = ['normal', 'diarrhea', 'food present', 'constipated', 'blood'][0], verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    entry['poop_quality'] = poop_quality

    listobj['date'] = entry

    write_out(listobj, verbose = verbose)

def edit_physical(date:str, physical_feeling = ['good', 'bloated', 'light', 'nauseous'][0], verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    entry['physical_feeling'] = physical_feeling

    listobj['date'] = entry

    write_out(listobj, verbose = verbose) 

def edit_mental(date:str, mental_feeling = ['clear', 'foggy', 'stressed', 'apathetic'][0], verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    entry['mental_feeling'] = mental_feeling

    listobj['date'] = entry

    write_out(listobj, verbose = verbose)    

def edit_vomit(vomit:bool, date:str, verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    entry['vomit'] = vomit

    listobj['date'] = entry

    write_out(listobj, verbose = verbose)        

  
def print_out_date(date:str):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return
    
    print(f"|- - - - - {date} - - - - -|")
    print(f"Food: {', '.join(entry['food'])}")
    print(f"Sleep hours: {entry['sleep_hours']}")
    print(f"Steps: {entry['steps']}")
    print(f"Poop quality: {entry['poop_quality']}")
    print(f"Physical feeling: {entry['physical_feeling']}")
    print(f"Mental feeling: {entry['mental_feeling']}")
    print(f"Vomit?: {entry['vomit']}")
    print(f"| - - - - - - - - - - - - - - - - |")

def delete_date(date:str, verbose = False):
    try:
        listobj, entry = access_date_procedure(date)
    except:
        return

    listobj.pop(date, None)

    write_out(listobj, verbose = verbose) 
