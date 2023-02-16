import time
import pytest
from pageobjects.Warranty.GooglePage import GooglePage

@pytest.fixture(scope="class")
def google_url(driver,frontend_url):
    google_url = GooglePage(driver) # driver reference conftest.py
    return google_url
    
class TestWarrantyFunctions:
    """Warranty Test
    """

    def test_inputwords(self, google_url):
        """input BitoPro words"""

        # arrange

        # act
        googleserch=google_url.get_search()
        inputwords = google_url.input_words()
        

    def test_wordscorrect(self, google_url):
        """words correct"""

        strings = google_url.bitopro_words()
        text_words = google_url.assert_words()
        
        # assert 
        assert strings == text_words

         
        
    