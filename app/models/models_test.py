import unittest
import quote

Quote = quote.Quote

class QuoteTest(unittest.TestCase):

    def setUp (self):
        self.new_quote = Quote(123,'i am wise', 'Angela Mutyota')

    def test_instance(self):
            self.assertTrue(isinstance(self.new_quote,Quote))

if __name__ == '__main__':
    unittest.main()