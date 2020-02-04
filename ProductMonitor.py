import requests
import json
import sys
from twilio.rest import Client

class Product:
    def __init__(self, productname, producturls, productnumbers):
        self.productname = productname
        self.producturls = producturls
        self.productnumbers = productnumbers

    def checkstock(self):
        '''Iterates through product URLs, downloads site, and checks for instock'''
        returnvalue = False
        for key,value in self.producturls.items():
            current_site = key
            current_url = value[0]
            current_instock_string = value[1]

            website = requests.get(current_url)
            if current_instock_string in website.text:
                self.instockalert(current_site, current_url)
                returnvalue = True
        
        return returnvalue

    def instockalert(self, current_site, current_url):
        '''If product is found, iterate through product numbers and send SMS'''
        for key,value in self.productnumbers.items():
            print(f'Messaging {key} at {value} here is the link {current_url}')

class Website:
    def __init__(self, storename, storeurl, productname, instockstring):
        self.storename = storename
        self.storeurl = storeurl
        self.productname = productname
        self.instockstring = instockstring

    def checkstock(self):
        '''Requests site, searches html and returns True if instockstring is found'''
        website = requests.get(self.storeurl)
        return (self.instockstring in website.text)

def SendTwilioMessage(account_sid, auth_token, source, destination, prodcut, url):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=destination, 
        from_=source,
        body="Product Found At " + url)


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
    filename = 'test/valid.json'
    if ValidateJSON(filename):
        data = ImportJSON(filename)
        print(f'Imported {filename}')
    else:
        print(f'{filename} is not valid json format, quitting')
        quit()

    product = data['Product']
    urls = data['URLs']
    numbers = data['Numbers']

    product = Product(product, urls, numbers)
    product.checkstock()

