import requests
import json
import sys

class Website:
    def __init__(self, storename, storeurl, productname, instockstring):
        self.storename = storename
        self.storeurl = storeurl
        self.productname = productname
        self.instockstring = instockstring

    def checkstock(self):
        '''Requests site, searches html and returns True if instockstring is found'''
        print(f'Checking {self.storename} for {self.productname}')
        website = requests.get(self.storeurl)
        return (self.instockstring in website.text)

def ImportJSON(filename):
    ''' Imports the JSON File and returns the object'''
    file = open(filename)
    data = json.load(file)
    return data

def ValidateJSON(filename):
    '''Confirm JSON is valid before doing anything else'''
    file = open(filename)
    try:
        json_object = json.load(file)
    except ValueError as e:
        return False
    return True

if __name__ == "__main__":
    site = Website('GitHub', 'https://github.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
    site.checkstock()

