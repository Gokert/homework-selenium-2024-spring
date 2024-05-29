from ui.pages.base_page import BasePage
from ui.locators.catalog_locators import CommerceCenterPageLocators
from selenium.webdriver.support import expected_conditions as EC

class CommerceCenterPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CommerceCenterPageLocators()

    def open_center(self):
        self.click(self.locators.LEFT_MENU_ITEMS_LOCATOR,20)

    def open_catalog_creation(self):
        self.click(self.locators.CREATE_CATALOG_BTN_LOCATOR,20)

    def open_catalog_settings(self):
        self.find(self.locators.CATALOG_NAME_INPUT_LOCATOR, 100)
        
    def rename_catalog(self, new_name):
        self.find(self.locators.CATALOG_NAME_INPUT_LOCATOR).clear()
        self.fill(self.locators.CATALOG_NAME_INPUT_LOCATOR, new_name)
        self.click(self.locators.SUBMIT_CATALOG_SETTINGS_LOCATOR)

    def close_help_modal(self):
        try:
            self.click(self.locators.CLOSE_HELP_MODAL_BTN_LOCATOR)
        except:
            pass
    
    def select_feed_source(self, source):
        self.click(self.locators.get_locator_by_source(source))
    
    def fill_feed_url(self, url):
        self.fill(self.locators.FEED_URL_INPUT_LOCATOR, url)

    def submit_catalog_creation(self):
        self.click(self.locators.SUBMIT_CATALOG_BTN_LOCATOR)

    def wait_for_feed_load(self):
        self.find(self.locators.ROW_LOCATOR, 600)

    def open_commerce_center(self):
        self.click(self.locators.left_menu.COMMERCE_CENTER_BTN_LOCATOR)

    def clear_catalogs(self):
        self.find(self.locators.SUCCESS_CATALOG_REMOVE_NOTIFY_LOCATOR, 100)

    def search_catalog(self, catalog_name):
        self.find(self.locators.CATALOG_SEARCH_INPUT_LOCATOR).clear()
        self.fill(self.locators.CATALOG_SEARCH_INPUT_LOCATOR, catalog_name)

    def wait_for_lens(self):
        self.find(self.locators.LENS_LOCATOR)

    def wait_for_right_menu(self):
        self.fill(self.locators.RIGHT_MENU_LOCATOR)
