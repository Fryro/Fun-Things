#!/usr/bin/python
from pprint import pprint
import json
import sys

try:
    datafile = sys.argv[1]
except:
    raise IndexError("You must specificy a Json Dictionary.\nError Encountered : {}".format(e))

def add_to_dictionary(element_name, element_description, element_category):

    update_dictionary(element_name, element_category, element_description, datafile)
    print("Entry '''{} : {}'''\nappended successfully, under category {}.".format(element_name, element_description, element_category))



def update_dictionary(name, category, description, jsonfile):        

    try:
        with open(jsonfile, "r") as Dictionary:
            DictFile = json.load(Dictionary)
    except Exception as e:
        raise SystemExit("Error loading dictionary file: {}".format(e))
    
    DictFile.append({category:{name:description}})    
 
    try:
        with open(datafile, "w") as Dictionary:
            json.dump(DictFile, Dictionary)
    except Exception as e:
        raise SystemExit("Error loading dictionary file: {}".format(e))

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    NAMEKEY = '\033[35m'
    NAMEVALUE = '\033[31m'
    ENDC = '\033[0m'
    PRETTY = '\033[36m'

def search_dictionary(search1, search2):

    try:
        with open(datafile, "r") as dictfile:
            dictionary = json.load(dictfile)
    except Exception as e:
        raise SystemExit("Error loading file : {}".format(e))

    dict_search_main(dictionary, search1, search2)
    print("\n\n-----")

#This function is used to print the key,value pairs within the dictionary.
################
def print_dictionary(dictionary, KeySearch):
    if len(KeySearch) > 0:
        for key,value in dictionary.items():
            for key2,value2 in value.items():
                if KeySearch in str(key):
                    print("\t{} {} : {} {}".format(bcolors.OKBLUE, key2, bcolors.OKGREEN, value2))
                    print(" {} Completed via categorical search.".format(bcolors.NAMEKEY))

    else:
        for key,value in dictionary.items():
            print("\t{} {} : {} {}".format(bcolors.OKBLUE, key, bcolors.OKGREEN, value))
            print(" {} Completed via basic query".format(bcolors.NAMEKEY))
            print("")
################


#This section is used exclusively if the input 'KeysList' is entered in sys.argv[2]#
################
def print_keys(dictionary):
    for index in dictionary:
        print(dictionary.keys())
        print(" {} Completed via KeysList search.{}".format(bcolors.NAMEKEY, bcolors.ENDC))
################


#This section is the main loop in the program. It iterates through the dictionary, makes checks, and calls functions.#
################
def dict_search_main(dictionary, search, search2):
    for index in dictionary:
        if (search == "KeysList"):
            print_keys(index)
        elif len(search) > 0:
            for key in index.keys():
                if search in str(index[key]):
                    if len(search2) > 0:
                        key = search2
                        print_dictionary(index, key)
                        break
                    else:
                        key = ""
                        print_dictionary(index, key)
                        break
                elif len(search2) > 0:
                    for key in index.keys():
                        if search2 in str(index[key]):
                            key = search2
                            print_dictionary(index, key)
                            break
        else:
            key = ""
            print_dictionary(index, key)

            print(" {} ## END OF FILE ## {}\n\n\n-----".format(bcolors.ENDC, bcolors.ENDC))
################
in_command = ""
running = True
initial_input = True

while (running):
    if ((len(in_command) == 0) and (initial_input)):
        print("{} ### START ### {}".format(bcolors.ENDC, bcolors.ENDC))
        print("{} Add Index : {} Add an entry.{}".format(bcolors.OKBLUE, bcolors.OKGREEN, bcolors.ENDC))
        print("{} Search Index : {} Search for an entry.{}".format(bcolors.OKBLUE, bcolors.OKGREEN, bcolors.ENDC))
        print("{} 'exit' : {} Close this instance.{}".format(bcolors.OKBLUE, bcolors.OKGREEN, bcolors.ENDC))
        in_command = input("{}Enter the input corresponding to the action you wish to perform : ".format(bcolors.ENDC))
        initial_input = False

    if (in_command == "Add Index"):
        try:
            in_name = input("{}\n\tEnter the title of this entry : {}".format(bcolors.PRETTY, bcolors.ENDC))
        except Exception as e:
            raise SystemExit("You have to specifiy an element to add.\n\tError Encountered : {}".format(e))
	

        try:
            in_description = input("{}\tEnter the entry/definition for {} : {}".format(bcolors.PRETTY, in_name, bcolors.ENDC))
        except Exception as e:    		
            raise SystemExit("You have to define the element you are adding.\n\tError Encountered : {}".format(e))
	

        try:
            in_category = input("{}\tEnter the category in which [{}] falls, or a noteworthy keyword : {}".format(bcolors.PRETTY, in_name, bcolors.ENDC))
        except Exception as e:
            raise SystemExit("You have to specify what type of element you are adding.\n\tError Encountered : {}".format(e))

        add_to_dictionary(in_name, in_description, in_category)
        initial_input = True
        in_command = ""

    elif (in_command == "Search Index"):
        try:
            in_search = input("{}\n\tEnter a keyword or phrase to search for : {}".format(bcolors.PRETTY, bcolors.ENDC))
        except Exception as e:
            raise SystemExit("Error Encountered : {}".format(e))

        try:
            in_search2 = input("\t{}You may also enter a category to fetch all entries within that category : {}".format(bcolors.PRETTY, bcolors.ENDC))
        except Exception as e:
            raise SystemExit("Error Encountered : {}".format(e))
        
        search_dictionary(in_search, in_search2)
        initial_input = True
        in_command = ""

    elif (in_command == "exit"):
        print("{}Quitting...{}".format(bcolors.PRETTY, bcolors.ENDC))
        running = False

    else:
        print("Please enter a valid command.")
        in_command = ""
        initial_input = False
        running = False
