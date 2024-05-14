from ui.pages.base_page import BasePage
from ui.locators.setting_page_locators import SettingPageLocators

class SettingsPage(BasePage):
    locators = SettingPageLocators()
    url = 'https://ads.vk.com/hq/settings'

    def click_header_general(self):
        self.click(self.locators.GENERAL_HEADER)

    def click_header_logs(self):
        self.click(self.locators.LOGS_HEADER)

    def click_header_notif(self):
        self.click(self.locators.NOTIF_HEADER)

    def click_header_access(self):
        self.click(self.locators.ACCESS_HEADER)