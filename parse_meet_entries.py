import sys
from athlete import Athlete
from util import 



# line_entry_keys = {'line_type': 0, 'lastname': 1, 'firstname': 2, 'initial': 3, 
#                    'gender': 4,'birthdate': 5, 'team_code': 6, 'team_name': 7, 
#                    'age': 8, 'school_year': 9, 'reg_num': 21, 'comp_num': 22}



def parse_athlete_information(tokens):
    """
    side effects: modifies tokens (adds empty string items to index 8 & 9)

    Only the first 8 fields (including the record type) are required from 
    the data file, but even for these lines the provided value can be the 
    empty string.  We only require non-empty string values for last_name, 
    first_name, and gender.
    'age' and 'school_year' are optional attributes at position 8 & 9.
    If the line read from the file doesn't contain fields for position 8 and/or
    position 9, just add these two items (empty strings) to the end of the tokens
    list.
    """
    print(f"I-Line: {tokens}")  
    num_line_fields = len(tokens)
    if num_line_fields < 8: 
        raise Exception(f"I-Line doesn't have enough fields. Fields are: {tokens}")
    elif num_line_fields < 10:
        tokens.extend((10-num_line_fields)*[""])
    assert len(tokens[1:10] == 9)

    (last_name,
     first_name,
     middle,
     gender,
     birth_date,
     team_code,
     team_name,
     age, 
     school_year) = tokens[1:10]

    [lastn, firstn, middle] = tokens[1:4]
    fulln = create_full_name(first_name=firstn, middle=middle, last_name=lastn) 

    athlete = { 'full_name': fulln,
                'gender': tokens[4],
                'birth_date': tokens[5],
                'team': (tokens[6], tokens[7])
               }
    return athlete

    


def parse_event_entry(tokens):
    event_entry = {}
    # TODO - fill in
    return event_entry

def open_hytek_file(filename):
    """
    """
    athletes = {}
    entries = {}

    with open(filename) as file:
        for line in file:
            tokens = line.strip().split(';')
            if tokens[0] == "I":
                athlete = parse_athlete_information(tokens)
                athletes[athlete.full_name] = athlete
            elif tokens[0] == "D" or tokens[0] == "E":
                entry = parse_event_entry(tokens)       
    return athletes  #TODO return meet


def get_athletes_names():
    pass

def get_teams(athletes):
    teams = []
    for athlete in athletes.values():
        teams.append(athlete['team'])
    return sorted(set(teams))



############  MAIN *********

if len(sys.argv) > 1:
    athletes = open_hytek_file(sys.argv[1])
else:
    print "Please provide the filename that contains athelete and event entry information."