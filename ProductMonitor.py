import requests
import json
import sys
import config
import os
import glob
import logging
import shutil
import random

from twilio.rest import Client
from logging.handlers import TimedRotatingFileHandler

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
            top_user_agents = [
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
                                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15",
                                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
                                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
                                ]
            user_agent = random.choice(top_user_agents)
            logger.info(f'User Agent: {user_agent}')
            headers = {'User-Agent': user_agent}

            website = requests.get(current_url,headers=headers)

            if website.status_code != 200:
                logger.error(f'Return Code {website.status_code} from {current_url}')

            if current_instock_string in website.text:
                self.instockalert(current_site, current_url)
                returnvalue = True
        
        return returnvalue

    def instockalert(self, current_site, current_url):
        '''If product is found, iterate through product numbers and send SMS'''
        for key,value in self.productnumbers.items():
            print(f'Messaging {key} at {value} here is the link {current_url}')
            SendTwilioMessage(config.account_sid, config.auth_token, config.source, value,self.productname, current_url)
    
    def disableproduct(self):
        '''Legacy Method of disabling products '''
        f= open("trigger","w+")
        f.close()

def SendTwilioMessage(account_sid, auth_token, source, destination, productname, url):
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            to=destination, 
            from_=source,
            body=productname + " Found " + url)
    except:
        e = sys.exc_info()[0]
        logger.critical(f"{e}")
    
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

def DisableProduct(filename):
    source = os.getcwd() + filename
    destination = os.path.dirname(os.path.abspath(__file__)) + '/products/disabled/'
    shutil.move(filename, destination)
    logger.info(f'Moving {filename} to {destination}')

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler('log.txt', when='d',interval=1,backupCount=7)
    logger.addHandler(handler)


    if os.path.isfile('trigger'):
        print ("STOPPING - Trigger File Exists")
        logger.error("STOPPING - Trigger File Exists")
        quit()

    products = OpenProductDir('/products')

    for filename in products:
        if ValidateJSON(filename):
            data = ImportJSON(filename)
            logger.info(f'Imported {filename}')
            productname = data['Product']
            urls = data['URLs']
            numbers = data['Numbers']
            product = Product(productname, urls, numbers)
            result = product.checkstock()
            logger.info(f'Result of CheckStock() for {productname}: {result}')

            if result:
                DisableProduct(filename)

        else:
            logger.error(f'{filename} is not valid json format, quitting')
            quit()
