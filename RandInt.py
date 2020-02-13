import random
import json
import sys

##
## This is the main function of the program. It takes arguments of (list, quantity), and outputs a list of 'quantity' random elements from 'list'.
##

def random_list(arg_list, quantity):
    random_output_list = []
 
    for i in range(quantity):
        if (quantity == high):
            temp_random = random.choice(arg_list)
            random_output_list.append(temp_random)
            arg_list.pop(arg_list.index(temp_random))
        else:
            temp_random = random.choice(arg_list)
            random_output_list.append(temp_random)
            arg_list.pop(arg_list.index(temp_random))
    return (random_output_list)
 
##
## This is a dictionary of common error messages.
##
def error(errornum):
    errorstate = True
    errordict = {
    1: "Please enter a valid input for 'x', the number of random integers to generate.",
    2: "Please enter 'Low', the lower bound of random integers.",
    3: "Please enter 'High', the upper bound of random integers.",
    4: "Please ensure that 'High' is larger than 'Low', and that 'High - Low' does not exceed 'X'.",
    }
    raise SystemExit(errordict.get(errornum, "Error : Unknown Error"))
 
##
## Explains to the user what the program does.
##
print("This program will generate 'x' amount of random numbers from a list of integers, with a domain starting at 'Low' and ending at 'High'. It will not repeat values.")
 
##
## The following Try/Except and If/Else statements catch logistical and input errors.
##

try:
    dict_file = sys.argv[1]
except:
    dict_file = ""

try:
    generator_num = int(input("\tX : "))
except Exception as e:
    error(1)
 
try:
    low = int(input("\tLow : "))
except Exception as e:
    error(2)
 
try:
    high = int(input("\tHigh : "))
except Exception as e:
    error(3)
 
random_range = high - low
if (random_range < generator_num) or (random_range < 0):
    error(4)
if (random_range > 0):
    int_list = [low]
 
for i in range(random_range):
    int_list.append(i+low+1)
 
 
##
### This runs the iterative function.
##

final_list = random_list(int_list, generator_num)
print(final_list)

def updateDictionary(in_list):
 
     try:
         with open(dict_file, "r") as Dictionary:
            data_file  = json.load(Dictionary)
     except Exception as e:
         raise SystemExit("Error loading file : {}".format(e))
 
     for number in in_list:
        data_file.append({"Random Number":number})

     try:
        with open(dict_file, "w") as Dictionary:
            json.dump(data_file, Dictionary)
     except Exception as e:
        raise SystemExit("Error loading dictionary file : {}".format(e))

if (len(dict_file) > 0):
    updateDictionary(final_list)

