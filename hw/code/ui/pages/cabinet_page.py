from ui.pages.base_page import BasePage
from ui.locators.cabinet_page_locators import CabinetPageLocators


class CabinetPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = CabinetPageLocators()

    def click_left_menu(self, section):
        self.click(self.locators.LEFT_MENU(section))

