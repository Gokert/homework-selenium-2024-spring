import time
import allure

from ui.locators import basic_locators

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.select import Select

class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=4):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        # fix it
        # self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator, timeout=None):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def find_multiple(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Search')
    def search(self, query):
        elem = self.find(self.locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
        go_button.click()

    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()
        return elem

    @allure.step('Check')
    def became_visible(self, locator, timeout=None):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    @allure.step('Get text')
    def get_text(self, locator):
        return self.find(locator).text
    
    @allure.step('Change Tab')
    def change_tab(self, window):
        return self.driver.switch_to.window(window)
    
    @allure.step('Change iFrame')
    def switch_to_iframe(self, iframe):
        return self.driver.switch_to.frame(iframe)

    @allure.step('Close current tab')
    def close_current_tab(self):
        return self.driver.close()

    @allure.step('Get tab')
    def get_tab(self, tab_num):
        return self.driver.window_handles[tab_num]
    
    @allure.step('Type Text')
    def type_text(self, LOCATOR, text):
        return self.find(LOCATOR, 10).send_keys(text)
    
    @allure.step('Type Text')
    def dropbox_select(self, LOCATOR, value):
        select = Select(self.find(LOCATOR))
        if (type(value) == str):
            return select.select_by_visible_text(value)
            # select.select_by_value('value1')
        if (type(value) == int):
            return select.select_by_index(value)


    def fill(self, locator, keys):
        self.find(locator).send_keys(keys)

