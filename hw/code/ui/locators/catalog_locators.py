from selenium.webdriver.common.by import By
from enum import Enum

class FeedSources(Enum):
    URL = 'url'
    FILE = 'file'

class CommerceCenterPageLocators:
    LEFT_MENU_ITEMS_LOCATOR = (By.CSS_SELECTOR, '[data-testid=left-menu]')
    COMMERCE_CENTER_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-entityid=catalogs]')
    AUDIENCE_BTN = (By.CSS_SELECTOR, '[data-entityid=audience]')
    COMPANIES_BTN = (By.CSS_SELECTOR, '[data-entity=dashboardV2]')

    RIGHT_MENU_LOCATOR = (By.CSS_SELECTOR, '.ModalRoot_componentWrapper__uzHTL')

    CREATE_CATALOG_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid=create-catalog]')

    CATALOG_MENU_BTNS_LOCATOR = (By.XPATH, '//*[@id="catalogs"]/div/div/section/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/div/div')
    MENU_ITEM_BTNS_LOCATOR = (By.CSS_SELECTOR, '[data-testid=dropdown-item]')
    CATALOG_NAME_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid=catalogName-input]')
    SUBMIT_CATALOG_SETTINGS_LOCATOR = (By.CSS_SELECTOR, '[data-testid=submit]')

    CATALOG_SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, '[type=search][data-testid=search]')
    LENS_LOCATOR = (By.CSS_SELECTOR, 'svg.vkuiIcon[width="56"]')

    REMOVE_CATALOG_MODAL_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-testid=button-remove]')
    CLOSE_HELP_MODAL_BTN_LOCATOR = (By.CSS_SELECTOR, '[role=button][aria-label=Закрыть]')

    SUCCESS_CATALOG_REMOVE_NOTIFY_LOCATOR = (By.CSS_SELECTOR, '.vkuiSnackbar')

    FEED_FROM_URL_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-entityid=url]')
    FEED_FROM_FILE_BTN_LOCATOR = (By.CSS_SELECTOR, '[data-entityid=file]')

    FEED_URL_INPUT_LOCATOR = (By.CSS_SELECTOR, '[data-testid=catalogUrl-input]')

    SUBMIT_CATALOG_BTN_LOCATOR = (By.CSS_SELECTOR, '[type=submit][title="Создать каталог"]')

    ROW_LOCATOR = (By.CSS_SELECTOR, '.BaseTable__row[role=row]')

    def get_locator_by_source(self, source):
        if source == FeedSources.URL:
            return self.FEED_FROM_URL_BTN_LOCATOR
        elif source == FeedSources.FILE:
            return self.FEED_FROM_FILE_BTN_LOCATOR
        else:
            raise TypeError('unknown source')