#!/usr/bin/python
from pprint import pprint
import json
import sys

try:
    ElementDescription = sys.argv[4]
except IndexError:
    raise SystemExit("You have to define the element you are adding.")

try:
    ElementName = sys.argv[3]
except IndexError:
    raise SystemExit("You have to specifiy an element to add.")

try:
    ElementType = sys.argv[2]
except IndexError:
    raise SystemExit("You have to specify what type of element you are adding.")

try:
    datafile = sys.argv[1]
except IndexError:
    raise SystemExit("You have to specify a dictionary file in json format")

def updateDictionary():
    
    try:
            with open(datafile, "r") as Dictionary:
                DictFile = json.load(Dictionary)
    except Exception as e:
        raise SystemExit("Error loading dictionary file: {}".format(e))
    
    DictFile.append({ElementType:{ElementName:ElementDescription}})    
 
    try:
            with open(datafile, "w") as Dictionary:
                json.dump(DictFile, Dictionary)
    except Exception as e:
        raise SystemExit("Error loading dictionary file: {}".format(e))

updateDictionary()
