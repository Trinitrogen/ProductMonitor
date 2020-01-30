class Website:
    def __init__(self, storename, storeurl, productname, instockstring):
        self.storename = storename
        self.storeurl = storeurl
        self.productname = productname
        self.instockstring = instockstring

    def checkstock(self):
        print(f'Checking {self.storename} for {self.productname}')

    def returnzero(self):
        return 0

if __name__ == "__main__":
    site = Website('Natchezz', 'www.google.com', 'Varget 8#', '<p class="availability in-stock">Availability: <span>In stock</span></p>')
    site.checkstock()

