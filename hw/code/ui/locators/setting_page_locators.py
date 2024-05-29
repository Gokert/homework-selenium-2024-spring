from selenium.webdriver.common.by import By


class SettingPageLocators():
    NOTIF_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings.notifications')]")
    GENERAL_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings')]")
    LOGS_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings.logs')]")
    SETTINGS_LEFT_MENU = (By.XPATH, '//*[@data-entityid="settings"]')
    SETTINGS_PANEL = (By.XPATH, "//*[contains(@class, 'layout_mainContainer__')]")

    SETTINGS_MAIN_HEADER = (By.XPATH, '//*[@aria-controls="settings"]')
    SETTINGS_MAIN_PANEL = (By.XPATH, "//*[contains(@class, 'layout_mainContainer__')]")

    NOTIF_PANEL = (By.XPATH, "//*[contains(@class, 'Notifications_content__')]")
    SETTINGS_MAIN_HEADER = (By.XPATH, '//*[@aria-controls="settings"]')

    ACCESS_HEADER = (By.XPATH, "//*[contains(@id, 'tab-settings.access')]")
    ACCESS_PANEL = (By.XPATH, "//*[contains(@class, 'EmptyView_content__')]")

    LOG_PANEL = (By.XPATH, "//*[contains(@class, 'ChangeLogs_layout__')]")
