"""
This is the organization module and supports all the ReST actions for the
Organization collection
"""
# Necessary modules for calling an module from ansible
import json
import shutil

# System modules
from datetime import datetime
#form src/module_utils import devops_organization
# 3rd party modules
from flask import (
    make_response,
    abort
)

# Static Data to serve with API
ITEMS = {
    "DE000A1EWWW0" : {
        "description":"addidas",
        "price":"192,65",
        "timestamp":"2018-10-11 17:35:00"
    },   
    "DE0008404005" : {
        "description":"Allianz",
        "price":"182,28",
        "timestamp":"2018-10-11 17:35:00"
    },
    "DE000BASF111" : {
        "description":"BASF",
        "price":"70,00",
        "timestamp":"2018-10-11 17:35:00"
    },   
    "DE000BAY0017" : {
        "description":"Bayer",
        "price":"77,32",
        "timestamp":"2018-10-11 17:35:00"
    },   
    "DE0005200000" : {
        "description":"Beiersdorf",
        "price":"89,62",
        "timestamp":"2018-10-11 17:35:00"
    },   
    "DE0005190003" : {
        "description":"BMW",
        "price":"74,30",
        "timestamp":"2018-10-11 17:35:00"
    },  
    "DE0005439004" : {
        "description":"Continental",
        "price":"137,00",
        "timestamp":"2018-10-11 17:35:00"
    },  
    "DE0006062144" : {
        "description":"Covestro",
        "price":"61,72",
        "timestamp":"2018-10-11 17:35:00"
    }      
}
 
# Function to generate Timestamp 
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all(length=0, offset=0):
    """
    This function responds to a request for /api/item
    with the complete lists of items

    :return:        json string of list of items
    """
    
    # Load Items 
    dictItem = json.load(ITEMS)
    
    # Test if Ansible has worked correct
    if len(dictItem) < 1 :
        print("ERROR item.py - read_all: The item list has length 0. ")
        abort(500, 'temp.py - read_all(): Error reading item list.')

    # Control, if function attributes are set correct
    if offset is 0:
        offset = len(dictItem)

    # Cut list
    if (length < len(dictItem) ):
       resultItem = dictItem[length: offset + length]
       
        # Return Value
    return [resutItem[key] for key in sorted(resultItem.keys())]
    




