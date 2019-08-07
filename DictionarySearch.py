#!/nmonk/bin/env python3
import pprint
import sys
import json

#color setup
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    NAMEKEY = '\033[35m'
    NAMEVALUE = '\033[31m'
    ENDC = '\033[0m'
    PRETTY = '\033[36m'

try:
    datafile = sys.argv[1]
    try:
        with open(datafile, "r") as dictfile:
            dictionary = json.load(dictfile)
    except Exception as e:
        raise SystemExit("Error loading file : {}".format(e))
except IndexError:
        raise SystemExit("You have to specific a dictionary.json file.")

try:
    search = sys.argv[2]
except:
    search = ""

try:
    search2 = sys.argv[3]
except:
    search2 = ""

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
################

print(" {} ## END OF FILE ## {}\n\n\n-----".format(bcolors.ENDC, bcolors.ENDC))
