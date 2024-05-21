from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    locators = MainPageLocators()
    url = "https://ads.vk.com/"

    def switch_to_new_tab(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def click_vk_logo(self):
        self.click(self.locators.VK_LOGO)

    def click_nav_button(self, button_name: str):
        self.click(self.locators.get_button_locator(button_name))

    def click_webinar_button(self):
        self.scroll_and_click(self.locators.WEBINARS_BTN)

    def click_news_button(self):
        self.scroll_and_click(self.locators.NEWS_BTN)

    def click_footer_cabinet_button(self):
        self.scroll_and_click(self.locators.FOOTER_CABINET_BTN)

    def click_footer_section_button(self, button_name: str):
        href = self.locators.PAGE_ELEMENTS[button_name][1]
        self.scroll_and_click(self.locators.footer_section_locator(href))

    def click_cabinet_nav_button(self):
        self.click(self.locators.CABINET_NAV_BTN)

    def open_education_dropdown_menu(self):
        self.click(self.locators.EDUCATION_DROPDOWN_BTN, timeout=1)

    def click_case_link(self):
        # self.click(self.locators.CASE_LINK_LOCATOR)
        case_link = self.find(self.locators.CASE_LINK_LOCATOR)
        self.scroll_into_view(case_link)
        case_link.click()

    def get_case_title_text(self, new_page: bool):
        if new_page:
            return self.find(self.locators.NEW_CASE_TITLE_LOCATOR).text
        return self.find(self.locators.CASE_TITLE_LOCATOR).text

    def click_dropdown_menu_button(self, button_name: str):
        self.click(self.locators.get_dropdown_item_locator(button_name))

    def click_view_all_cases(self):
        self.click(self.locators.VIEW_ALL_CASES_BTN)

    def scroll_and_click(self, locator):
        element = self.find(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        element.click()
