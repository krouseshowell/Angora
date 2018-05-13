from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #go to browser
        self.browser.get('http://localhost:8000')
        #Is 'To-Do' in the title?
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')



#Invited to enter To-Do item
#types "Buy Peacock feathers"
#Pages updates when hits enter
#1:Buy Peacock feathers is listed
#still a enter box
#enter "Use peackock feathers" as an item in todo list.
#updates, shows both list items
#Site generates unique url
#explanitary text
#visit unique url, sees list.
#Leaves site.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
