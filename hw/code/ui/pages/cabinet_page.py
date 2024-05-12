from ui.pages.base_page import BasePage
from ui.locators.cabinet_page_locators import CabinetPageLocators


class CabinetPage(BasePage):
    locators = CabinetPageLocators()
    url = 'https://ads.vk.com/hq/overview'

    def click_left_menu(self, section):
        self.click(self.locators.LEFT_MENU(section))

    def click_vk_icon(self):
        self.click(self.locators.VK_ICON)

    def click_user_avatar(self):
        self.click(self.locators.USER_AVATAR)

    def click_logout_button(self):
        self.click(self.locators.LOGOUT_BUTTON)
