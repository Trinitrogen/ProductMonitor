import requests
import json
import sys
import config
import os
import glob
import logging
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
                self.disableproduct()
                returnvalue = True
        
        return returnvalue

    def instockalert(self, current_site, current_url):
        '''If product is found, iterate through product numbers and send SMS'''
        for key,value in self.productnumbers.items():
            print(f'Messaging {key} at {value} here is the link {current_url}')
            SendTwilioMessage(config.account_sid, config.auth_token, config.source, value,self.productname, current_url)
    
    def disableproduct(self):
        '''If product is found in stock, disable it to prevent future notification'''
        f= open("trigger","w+")
        f.close()

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

def SendTwilioMessage(account_sid, auth_token, source, destination, product, url):
    client = Client(account_sid, auth_token)
    notification = product + " Found at " + url

    message = client.messages.create(
        to=destination, 
        from_=source,
        body="Product Found " + url)
    
    return message


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

def OpenProductDir(directory):
    product_dir = os.path.abspath(os.path.dirname(sys.argv[0])) + directory
    product_jsons = glob.glob(product_dir + '/*.json')
    return product_jsons


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG,filename='log.txt',filemode='w', format='%(levelname)s - %(message)s')
    
    if os.path.isfile('trigger'):
        print ("STOPPING - Trigger File Exists")
        logging.error("STOPPING - Trigger File Exists")
        quit()


    products = OpenProductDir('/products')

    for filename in products:
        if ValidateJSON(filename):
            data = ImportJSON(filename)
            logging.info(f'Imported {filename}')
            productname = data['Product']
            urls = data['URLs']
            numbers = data['Numbers']
            product = Product(productname, urls, numbers)
            result = product.checkstock()
            #print(f'Result of CheckStock() for {productname}: {result}')
            logging.info(f'Result of CheckStock() for {productname}: {result}')
        else:
            #print(f'{filename} is not valid json format, quitting')
            logging.error(f'{filename} is not valid json format, quitting')
            quit()

