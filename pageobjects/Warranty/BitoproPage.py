from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pageobjects.BasePage import BasePage

class BitoproPage(BasePage):
    """Get google page"""

    # Funtion Field
    
    # assert check
    
    # other
    
   
    
    def _is_acceptcookies(self):
        
        self.find_element(*self.accept_allcookies_locator).click()
    
    def get_bitoprovip(self):
        ''' bitoprovip
        '''

        self.find_element(*self.search_locator).click()
    
    

    
    
