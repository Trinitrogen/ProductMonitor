import requests

class Website:
    def __init__(self, storename, storeurl, productname, instockstring):
        self.storename = storename
        self.storeurl = storeurl
        self.productname = productname
        self.instockstring = instockstring

    def checkstock(self):
        print(f'Checking {self.storename} for {self.productname}')
        website = requests.get(self.storeurl)
        return (self.instockstring in website.text)

    def returnzero(self):
        return 0

if __name__ == "__main__":
    site = Website('GitHub', 'https://github.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
    site.checkstock()

