from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pageobjects.BasePage import BasePage

class GooglePage(BasePage):
    """Get google page"""

    # Funtion Field
    search_locator   = (By.NAME, 'q')
    

    # assert check
    string_locator = (By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3")
    
    # other
    words_bitopro = "BitoPro 台灣幣託交易所"
   
    
    def _is_acceptcookies(self):
        
        self.find_element(*self.accept_allcookies_locator).click()
    
    def get_search(self):
        '''click Get search field
        '''

        self.find_element(*self.search_locator).click()
    
    def input_words(self):
        """input words and enter
        """
        self.find_element(*self.search_locator).send_keys("BitoPro")
        self.find_element(*self.search_locator).send_keys(Keys.RETURN)

    def bitopro_words(self):
        """check bitopro words
        """

        self.find_element(*self.string_locator).text

    def assert_words(self):
        """bitopro words
        """
        string =self.words_bitopro 

    
    
