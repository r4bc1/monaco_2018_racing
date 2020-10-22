from datetime import datetime, timedelta
from collections import OrderedDict
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def encrypt_abbreviations(file_path):
    '''Creating the dictionary from the file with abbreviations
that describes the driver`s shortcut: his name and team.
'''
    abbreviations_dict = dict()
    with open(file_path, "r", encoding="utf-8") as abbreviations:
        for line in abbreviations:
            line = line.strip().split("_")
            if len(line) != 3:
                raise ValueError("You are missing one or more required\
                    parameters, check the data files!")

            abbreviations_dict[line[0]] = {
                "name": line[1],
                "team": line[2]
            }
        if abbreviations_dict == {}:
            raise ValueError("The abbreviations.txt file is empty!")
        return abbreviations_dict


def encrypt_log(file_path, error_message):
    '''Creating the dictionary from the file
that associate the drivers shortcut and his time of the best lap.'''
    with open(file_path, "r", encoding="utf-8") as log_file:
        log_dict = dict()
        for line in log_file:
            line = line.strip()
            if line == "":
                continue
            time = f"{line[17:]}"
            log_dict[line[:3]] = datetime.strptime(time, '%M:%S.%f')
        if log_dict:
            return log_dict
        raise ValueError(error_message)


def build_dict_for_database():
    '''Takes dictionaries with drivers start and end of best laps
using encryption_of_start() and encryption_of_end() functions, using
encryption_of_abbreviations() makes the final dictionary that contains
information about each driver and his lap time.'''
    start_dict = encrypt_log(os.path.join(BASE_DIR, "data_files/start.log"),
                             "The start.log file is empty!")
    end_dict = encrypt_log(os.path.join(BASE_DIR, "data_files/end.log"),
                           "The end.log file is empty!")
    res = encrypt_abbreviations(os.path.join(BASE_DIR,
                                             "data_files/abbreviations.txt"))
    for abb in res.keys():
        if end_dict[abb] > start_dict[abb]:
            res[abb]["time"] = (end_dict[abb] - start_dict[abb])
        else:
            res[abb]["time"] = timedelta(0)
    return res
