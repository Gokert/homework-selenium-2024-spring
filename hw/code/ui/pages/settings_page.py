from ui.pages.base_page import BasePage
from ui.locators.setting_page_locators import SettingPageLocators

class SettingsPage(BasePage):
    locators = SettingPageLocators()
    url = 'https://ads.vk.com/hq/settings'

    def click_header_notif(self):
        return self.click(self.locators.NOTIF_HEADER)

    def click_button(self, section):
        return self.click(section)

    def check_panel(self, section):
        return self.became_visible(section)