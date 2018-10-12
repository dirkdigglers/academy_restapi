#!/usr/bin/env python3
    
import requests
import json
import urllib
 
apiurl="http://127.0.0.1:5000"

# List items 
#############
def listitems():
    url = apiurl + "/api/item?length=2&offset=3"
    
    headers = {
        'Authorization': "Basic a2liYW5hOk1WLUhoTDBPOWglbHZtT28=",
        'Cache-Control': "no-cache",
        }
        
    response = requests.request("GET", url, headers=headers)
    
    print(response.text) 

# Main Procedure
if __name__ == '__main__':
    listitems()    
