from base_case import BaseCase
from ui.locators.setting_page_locators import SettingPageLocators

class TestSetting(BaseCase):
    locators = SettingPageLocators()

    def test_settings(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.SETTINGS_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.SETTINGS_PANEL)

    def test_header_notif(self, settings_page):
        assert settings_page.click_header_notif()
        assert settings_page.check_panel(self.locators.NOTIF_PANEL)

    def test_header_access(self, settings_page):
        assert settings_page.click(self.locators.ACCESS_HEADER)
        assert settings_page.check_panel(self.locators.ACCESS_PANEL)

    def test_header_logs(self, settings_page):
        assert settings_page.click(self.locators.LOGS_HEADER)
        assert settings_page.check_panel(self.locators.LOG_PANEL)
