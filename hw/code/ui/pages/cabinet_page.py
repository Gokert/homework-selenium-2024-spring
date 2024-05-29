from ui.pages.base_page import BasePage
from ui.locators.cabinet_page_locators import CabinetPageLocators


class CabinetPage(BasePage):
    locators = CabinetPageLocators()
    url = 'https://ads.vk.com/hq/overview'

    def click_button(self, section):
        return self.click(section)

    def check_panel(self, section):
        return self.became_visible(section)

    def click_vk_icon(self):
        return self.click(self.locators.VK_ICON)

    def click_user_avatar(self):
        return self.click(self.locators.USER_AVATAR)

    def click_control_id(self):
        return self.click(self.locators.CONTROL_ID_BUTTON)

    def click_logout_button(self):
        return self.click(self.locators.LOGOUT_BUTTON)

    def check_welcome_vk_panel(self):
        return self.became_visible(self.locators.WELCOME_VK_PANEL)

    def check_review_company(self):
        return self.became_visible(self.locators.REVIEW_COMPANY)