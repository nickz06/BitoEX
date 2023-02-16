import time
from typing import List

from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.remote.webelement import WebElement
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    """
    BasePage 封裝所有頁面的共用方法，例如 driver, url, find_element等
    """

    def __init__(self, selenium_driver: webdriver):
        self.driver = selenium_driver


    def on_page(self, pagetitle) -> bool:
        return pagetitle in self.driver.title

    """define open method，use_open() openurl"""
    def open(self, url)  -> None :
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, *loc) -> WebElement :
        """found HTML Element

        :param loc:
        :return:
        :rtype: WebElement
        :raises WebDriverException can not found element
        """
        time.sleep(0.1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)

    def find_elements(self, *loc) -> List[WebElement] :
        """found HTML Element

        :param loc:
        :return:
        :rtype: List[WebElement]
        :raises WebDriverException can not found element
        """
        time.sleep(0.1)
        WebDriverWait(self.driver, 90).until(EC.visibility_of_element_located(loc))
        return self.driver.find_elements(*loc)

    def find_page(self, *loc):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(loc))
            return True
        except WebDriverException:
            return False

    def switch_frame(self, loc):
        self.driver.switch_to.frame(loc)

    def switch_to_frame(self):
        # self.switch_to_company_frame()
        self.driver.switch_to.frame('')

    def switch_to_company_frame(self):
        self.driver.switch_to.default_content()

    def script(self, src):
        self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(f"{self} page can not found {loc} element")

    def move_mouse(self, loc):
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(*loc)).perform()
