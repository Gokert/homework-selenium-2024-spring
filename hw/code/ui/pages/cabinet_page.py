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

    def click_education_modal_exit(self):
        self.click(self.locators.EDUCATION_EXIT)

    def click_control_id(self):
        self.click(self.locators.CONTROL_ID_BUTTON)

    def click_logout_button(self):
        self.click(self.locators.LOGOUT_BUTTON)

    def click_help(self):
        self.click(self.locators.HELP_ICON)

    def check_modal_page_help(self):
        return self.became_visible(self.locators.HELP_MODAL, 5)

    def click_help_menu(self):
        self.click(self.locators.HELP_MENU())

    def check_modal_page_education(self):
        return self.became_visible(self.locators.EDUCATION_MODAL, 5)

    def click_modal_page_education(self):
        self.click(self.locators.EDUCATION_BUTTON)