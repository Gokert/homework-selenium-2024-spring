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