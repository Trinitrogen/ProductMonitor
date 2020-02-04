import unittest
import json
import ProductMonitor
from ProductMonitor import Website
from ProductMonitor import Product
import config


class TestSendTwilioMessage(unittest.TestCase):
    def test_Baseline(self):
        result = ProductMonitor.SendTwilioMessage(config.test_account_sid, config.test_auth_token, config.test_source, config.test_destination, 'Test Product', 'www.github.com')
        self.assertEqual(result.error_code, None)

class TestProductClass(unittest.TestCase):
    def test_WebsiteInStockAlertPositive(self):
        data = ProductMonitor.ImportJSON('test/in_stock_test.json')
        product = data['Product']
        urls = data['URLs']
        numbers = data['Numbers']

        product = Product(product, urls, numbers)

        self.assertEqual(product.checkstock(), True)

    def test_WebsiteInStockAlertNegative(self):
        data = ProductMonitor.ImportJSON('test/out_of_stock_test.json')
        product = data['Product']
        urls = data['URLs']
        numbers = data['Numbers']

        product = Product(product, urls, numbers)

        self.assertEqual(product.checkstock(), False)
    


class TestValidateJSON(unittest.TestCase):
    def test_ValidateJson_Valid_Input(self):
        '''Test validatejson method on valid json'''
        test_json = 'test/valid.json'
        result = ProductMonitor.ValidateJSON(test_json)
        self.assertEqual(result, True)

    def test_ValidateJson_Invalid_Input(self):
        '''Test validatejson method on invalid json'''
        test_json = 'test/invalid.json'
        result = ProductMonitor.ValidateJSON(test_json)
        self.assertEqual(result, False)

class TestImportJSON(unittest.TestCase):
    def test_JSONImportProduct(self):
        '''Import JSON, test the Product Field'''
        test_json = 'test/valid.json'
        data = ProductMonitor.ImportJSON(test_json)
        self.assertEqual(data['Product'], 'Test Product')

    def test_JSONImportEnabled(self):
        '''Import JSON, test the Product Field'''
        test_json = 'test/valid.json'
        data = ProductMonitor.ImportJSON(test_json)
        self.assertEqual(data['Enabled'], True)

    def test_JSONImportURLs(self):
        '''Import JSON, make sure the URLs Dictionary is correct'''
        urls = {'Github - In Stock': ['https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html','The Product is IN STOCK'],'Github Test - Out Of Stock': ['https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/OutOfStockExample.html','The Product is IN STOCK']}
        test_json = 'test/valid.json'
        data = ProductMonitor.ImportJSON(test_json)
        self.assertEqual(data['URLs'], urls)
    
    def test_JSONImportNumbers(self):
        '''Import JSON, make sure the Numbers Dictionary is correct'''
        numbers = {'Alice': '123456789', 'Bob': '987654321'}
        test_json = 'test/valid.json'
        data = ProductMonitor.ImportJSON(test_json)
        self.assertEqual(data['Numbers'], numbers)


class TestWebsiteClass(unittest.TestCase):
    def test_WebsiteInStockAlert(self):
        data = ProductMonitor.ImportJSON('test/in_stock_test.json')
        product = data['Product']
        urls = data['URLs']
        numbers = data['Numbers']

        product = Product(product, urls, numbers)

        self.assertEqual(product.checkstock(), True)

    def test_WebsiteStoreName(self):
        #Arrange
        site = Website('Github Test - In Stock', 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
        #Act
        result = site.storename
        #Assert
        self.assertEqual(result, 'Github Test - In Stock')

    def test_WebsiteStoreUrl(self):
        #Arrange
        site = Website('Github Test - In Stock', 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
        #Act
        result = site.storeurl
        #Assert
        self.assertEqual(result, 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html')

    def test_WebsiteProductName(self):
        #Arrange
        site = Website('Github Test - In Stock', 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
        #Act
        result = site.productname
        #Assert
        self.assertEqual(result, 'Test - In Stock')

    def test_WebsiteInStockString(self):
        #Arrange
        site = Website('Github Test - In Stock', 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
        #Act
        result = site.instockstring
        #Assert
        self.assertEqual(result, 'The Product is IN STOCK')

    def test_WebsiteCheckInStock(self):
        #Arrange
        site = Website('Github Test - In Stock', 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
        #Act
        result = site.checkstock()
        #Assert
        self.assertEqual(result, True)

    def test_WebsiteCheckOutOfStock(self):
        #Arrange
        site = Website('Github Test - Out Of Stock', 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/OutOfStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
        #Act
        result = site.checkstock()
        #Assert
        self.assertEqual(result, False)

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()