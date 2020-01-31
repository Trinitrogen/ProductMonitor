import unittest
from ProductMonitor import Website

class TestWebsiteClass(unittest.TestCase):
    def test_baseline(self):
        self.assertEqual(0,0)
   
    def test_WebsiteReturnZero(self):
        #Arrange
        site = Website('Github Test - In Stock', 'https://GitHub.com/Trinitrogen/ProductMonitor/blob/master/test/InStockExample.html', 'Test - In Stock', 'The Product is IN STOCK')
        #Act
        result = site.returnzero()
        #Assert
        self.assertEqual(result, 0)

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