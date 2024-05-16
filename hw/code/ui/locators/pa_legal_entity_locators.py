from selenium.webdriver.common.by import By

class PALegalEntityLocators:
    LOCATOR_VK_ICO = (By.CLASS_NAME, "header_left__cv9bp")
    LOCATOR_USER_NAME = (By.CLASS_NAME, "AccountSwitch_changeAccountButton__o5T9V")
    LOCATOR_BELL = (By.CLASS_NAME, "header_bellNotifications__vAHeR")
    LOCATOR_USER_ICO = (By.CLASS_NAME, "userMenu_avatar__oCUFq")
    LOCATOR_LOG_OUT = (By.XPATH, "//div[@class='vkuiPopover__in']/div[1]/div[@role='button']")
    LOCATOR_BUDGET = (By.XPATH, "//a[@data-route='budget']/div[2]")
    LOCATOR_ACCESS_RIGHT = (By.XPATH, "//a[@data-route='access_rights']/div[2]")
    LOCATOR_ADD_MANAGER = (By.XPATH, "//div[@data-testid='add-manager']/div[2]")
    LOCATOR_CLIENTS = (By.XPATH, "//a[@data-route='dashboardV2']/div[2]")
    LOCATOR_HELP_BUTTON = (By.CLASS_NAME, "Hint_hintTrigger__ixYRu")
    LOCATOR_SUPPORT_IFRAME = (By.XPATH, "//div[@id='vk_community_messages']/iframe")
    LOCATOR_BELL_NOTIFICATION = (By.XPATH, ".//div[contains(@class, 'vkuiHeader__main')]/h2/span[1]/span[1]")
    LOCATOR_BELL_NOT_NOTIFICATION = (By.XPATH, ".//div[contains(@class, 'EmptyPlaceholder_wrapper__8LcAC')]/div[1]/h2")
    LOCATOR_BELL_TEXT = (By.XPATH, ".//h4/span[1]/span[1]")
    @staticmethod
    def LOCATOR_HELP_BUTTON_REDIRECT(link_num):
        return (By.XPATH, f".//div[@class='Tooltip_tooltipContainer__P1b-O']/section[1]/a[{link_num}]/div[1]")
    LOCATOR_BUDGET_SPECIFY_DETAILS = (By.XPATH, "//div[@class='vkuiPlaceholder__action']")
    LOCATOR_BUDGET_SPECIFY_DETAILS_CLOSE = (By.XPATH, "//div[@aria-label='Закрыть']")
    LOCATOR_ADD_MANAGER_FIO = (By.XPATH, ".//input[@name='managerFio']")
    LOCATOR_ADD_MANAGER_MAIL = (By.XPATH, ".//input[@name='managerEmail']")
    LOCATOR_ADD_MANAGER_NEXT_BUTTON = (By.XPATH, ".//div[@class='ModalFooterSimple_container__rteom']/button[2]")
    LOCATOR_ADD_MANAGER_CLOSE = (By.XPATH, "//div[@aria-label='Закрыть']")