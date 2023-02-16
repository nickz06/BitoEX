from selenium.webdriver.common.by import By

from pageobjects.BasePage import BasePage

class GetWarrantyPage(BasePage):
    """Get info warranty page"""

    # Funtion Field
    serialnumber_locator  = (By.XPATH, "//*[@id='SerialNumber']")
    getinfo_locator       = (By.XPATH, "//*[@class='form-row']/div[2]/button")
    

    # assert check
    errorstring_special_locator = (By.XPATH, "//*[@class='form-row']/div[1]/span[3]")
    errorstring_invaild_locator = (By.XPATH, "//*[@class='col-sm-12']/div/div/div/p")
    errorstring_nserial_locator = (By.XPATH, "//*[@class='form-row']/div[1]/span[1]")
    
    # other
    accept_allcookies_locator  = (By.XPATH, "//*[@id='onetrust-accept-btn-handler']")
    
    
    def _is_acceptcookies(self):
        
        self.find_element(*self.accept_allcookies_locator).click()
    
    def getinfo_function(self):
        '''click Get info button
        '''
        self._is_acceptcookies()

        self.find_element(*self.getinfo_locator).click()
    
    def dogetinfo_function(self):
        '''click Get info button
        '''

        self.find_element(*self.getinfo_locator).click()
        
    def clearserialnumber(self):
        '''clear serial number filed
        '''
        self.find_element(*self.serialnumber_locator).clear()
    
    def noinputany_serialnumber(self):
        """no input any serialnumber
        """
        self.find_element(*self.serialnumber_locator).send_keys("")

    def addblank_serialnumber(self):
        """Add blank characters before serial number
        """
        self.find_element(*self.serialnumber_locator).send_keys(" 1863552437")

    def morethanten_serialnumber(self):
        """input more than ten serial number
        """
        self.find_element(*self.serialnumber_locator).send_keys("18635524372423423")
    
    def specialcharacters_serialnumber(self):
        """input special characters
        """
        self.find_element(*self.serialnumber_locator).send_keys("!#@#$@#323423")
        
    def encharacters_serialnumber(self):
        """input English characters
        """
        self.find_element(*self.serialnumber_locator).send_keys("Asdw123124")
        
    def errorstring_noanyserialnumber(self):
        '''Please specify a serial number
        '''
        self.find_element(*self.errorstring_nserial_locator).text
    
    def errorstring_specialchar(self):
        '''Please enter a valid serial number
        '''
        self.find_element(*self.errorstring_special_locator).text
        
    def errorstring_invaild_serialnumber(self):
        '''We couldn't find a product with this serial number. Please double-check the serial number and try again.
        '''
        self.find_element(*self.errorstring_invaild_locator).text

    
