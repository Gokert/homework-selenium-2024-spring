from base_case import BaseCase
from ui.locators.cabinet_page_locators import CabinetPageLocators


class TestCabinet(BaseCase):
    locators = CabinetPageLocators()

    def test_review(self, cabinet_page):
        assert cabinet_page.check_welcome_vk_panel()
        assert cabinet_page.check_review_company()

    def test_vk_icon(self, cabinet_page):
        assert cabinet_page.click_vk_icon()
        assert cabinet_page.check_panel(self.locators.CABINET_BODY)

    def test_company(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.COMPANY_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.COMPANY_BUTTON)

    def test_auditory(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.AUDITORY_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.AUDITORY_PANEL)

    def test_budget(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.BUDGET_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.BUDGET_PANEL)

    def test_budget(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.ONBOARD_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.ONBOARD_PANEL)

    def test_catalogs(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.CATALOGS_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.CATALOGS_PANEL)

    def test_pixels(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.PIXELS_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.PIXELS_PANEL)

    def test_mobapp(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.MOBAPP_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.MOBAPP_PANEL)

    def test_leaders(self, cabinet_page):
        assert cabinet_page.click_button(self.locators.LEADADS_LEFT_MENU)
        assert cabinet_page.check_panel(self.locators.LEADADS_PANEL)

    def test_control_id(self, cabinet_page):
        assert cabinet_page.click_user_avatar()
        assert cabinet_page.click_control_id()
        assert cabinet_page.check_panel(self.locators.AUTH_PANEL)

    def test_logout(self, cabinet_page):
        assert cabinet_page.click_user_avatar()
        assert cabinet_page.click_logout_button()
        assert cabinet_page.check_panel(self.locators.MAIN_HEADER)
