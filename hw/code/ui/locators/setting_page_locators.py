from selenium.webdriver.common.by import By

class SettingPageLocators():
    ACCESS_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings.access')]")
    NOTIF_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings.notifications')]")
    GENERAL_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings')]")
    LOGS_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings.logs')]")