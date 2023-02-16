import time
import pytest
from pageobjects.Warranty.BitoproPage import BitoproPage

@pytest.fixture(scope="class")
def bitoprovip_url(driver,bitopro_url):
    bitoprovip_url = BitoproPage(driver) # driver reference conftest.py
    return bitoprovip_url
    
class TestBitoproVipFunctions:
    """VIP Test
    """

    def test_bitoprovip(self, bitoprovip_url):
        """bitoprovip"""

        # arrange

        # act
        get_bitopro_url = bitoprovip_url
        
        


        
    