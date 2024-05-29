from selenium.webdriver.common.by import By

class PALegalEntityLocators:
    LOCATOR_VK_ICO = (By.XPATH, ".//header[@id='header']/div/div/button")
    LOCATOR_USER_NAME = (By.XPATH, ".//header[@id='header']/div/div[2]/div[1]")
    LOCATOR_BELL = (By.XPATH, ".//header[@id='header']/div/div[2]/div[3]")
    LOCATOR_USER_ICO = (By.XPATH, ".//header[@id='header']/div/div[2]/div[4]")
    LOCATOR_LOG_OUT = (By.XPATH, "//div[@class='vkuiPopover__in']/div[1]/div[@role='button']")
    LOCATOR_BUDGET = (By.XPATH, "//a[@data-route='budget']/div[2]")
    LOCATOR_ACCESS_RIGHT = (By.XPATH, "//a[@data-route='access_rights']/div[2]")
    LOCATOR_ADD_MANAGER = (By.XPATH, "//div[@data-testid='add-manager']/div[2]")
    LOCATOR_CLIENTS = (By.XPATH, "//a[@data-route='dashboardV2']/div[2]")
    LOCATOR_HELP_BUTTON = (By.XPATH, ".//a[@data-route='settings']/../div[1]")
    LOCATOR_BELL_NOTIFICATION = (By.XPATH, ".//div[contains(@class, 'vkuiHeader__main')]/h2/span[1]/span[1]")
    LOCATOR_BELL_NOT_NOTIFICATION = (By.XPATH, ".//div[contains(@class, 'EmptyPlaceholder_wrapper__8LcAC')]/div[1]/h2")
    LOCATOR_BELL_TEXT = (By.XPATH, ".//h4/span[1]/span[1]")
    @staticmethod
    def LOCATOR_HELP_BUTTON_REDIRECT(link_num):
        return (By.XPATH, f".//div[@class='Tooltip_tooltipContainer__P1b-O']/section[1]/a[{link_num}]/div[1]")
    LOCATOR_BUDGET_SPECIFY_DETAILS = (By.XPATH, ".//div[@id='budget']//button")
    @staticmethod
    def LOCATOR_BUDGET_SPECIFY_DETAILS_COMPANY(field):
        return (By.XPATH, f".//input[@name='{field}']")
    LOCATOR_BUDGET_SPECIFY_DETAILS_NEXT = (By.XPATH, ".//button[@type='submit']/span[@class='vkuiButton__in']")
    LOCATOR_BUDGET_SPECIFY_DETAILS_DROPBOX_CLICK = (By.XPATH, ".//div[@class='vkuiCustomSelectInput__input-group']//input")
    LOCATOR_BUDGET_SPECIFY_DETAILS_DROPBOX = (By.XPATH, ".//select[@name='addressRegion']")
    LOCATOR_BUDGET_SPECIFY_DETAILS_CLOSE = (By.XPATH, "//div[@aria-label='Закрыть']")
    LOCATOR_ADD_MANAGER_FIO = (By.XPATH, ".//input[@name='managerFio']")
    LOCATOR_ADD_MANAGER_MAIL = (By.XPATH, ".//input[@name='managerEmail']")
    LOCATOR_ADD_MANAGER_NEXT_BUTTON = (By.XPATH, ".//div[@class='ModalFooterSimple_container__rteom']/button[2]")
    LOCATOR_ADD_MANAGER_CLOSE = (By.XPATH, "//div[@aria-label='Закрыть']")