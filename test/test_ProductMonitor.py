import unittest
from ProductMonitor import Website

class TestWebsiteClass(unittest.TestCase):
    def test_baseline(self):
        self.assertEqual(0,0)
   
    def test_WebsiteReturnZero(self):
        #Arrange
        site = Website('Natchezz', 'https://www.natchezss.com/hodgdon-extreme-varget-rifle-powder-8-lbs.html', 'Varget 8#', '<p class="availability in-stock">Availability: <span>In stock</span></p>')
        #Act
        result = site.returnzero()
        #Assert
        self.assertEqual(result, 0)

    def test_WebsiteStoreName(self):
        #Arrange
        site = Website('Natchezz', 'https://www.natchezss.com/hodgdon-extreme-varget-rifle-powder-8-lbs.html', 'Varget 8#', '<p class="availability in-stock">Availability: <span>In stock</span></p>')
        #Act
        result = site.storename
        #Assert
        self.assertEqual(result, 'Natchezz')

    def test_WebsiteStoreUrl(self):
        #Arrange
        site = Website('Natchezz', 'https://www.natchezss.com/hodgdon-extreme-varget-rifle-powder-8-lbs.html', 'Varget 8#', '<p class="availability in-stock">Availability: <span>In stock</span></p>')
        #Act
        result = site.storeurl
        #Assert
        self.assertEqual(result, 'https://www.natchezss.com/hodgdon-extreme-varget-rifle-powder-8-lbs.html')

    def test_WebsiteProductName(self):
        #Arrange
        site = Website('Natchezz', 'https://www.natchezss.com/hodgdon-extreme-varget-rifle-powder-8-lbs.html', 'Varget 8#', '<p class="availability in-stock">Availability: <span>In stock</span></p>')
        #Act
        result = site.productname
        #Assert
        self.assertEqual(result, 'Varget 8#')

    def test_WebsiteInStockString(self):
        #Arrange
        site = Website('Natchezz', 'https://www.natchezss.com/hodgdon-extreme-varget-rifle-powder-8-lbs.html', 'Varget 8#', '<p class="availability in-stock">Availability: <span>In stock</span></p>')
        #Act
        result = site.instockstring
        #Assert
        self.assertEqual(result, '<p class="availability in-stock">Availability: <span>In stock</span></p>')

    def test_WebsiteCheckInStock(self):
        #Arrange
        site = Website('Natchezz', 'https://www.natchezss.com/hodgdon-extreme-varget-rifle-powder-8-lbs.html', 'Varget 8#', '<p class="availability in-stock">Availability: <span>In stock</span></p>')
        #Act
        result = site.checkstock()
        #Assert
        self.assertEqual(result, True)

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()