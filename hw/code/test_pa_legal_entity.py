from ui.pages.cabinet_page import CabinetPage
import time
import pytest
import allure
from base_case import BaseCase

@allure.title("Вкладыши: Личный кабинет(юридическое лицо) ")
@allure.description("Домашнее задание 3 по курсу 'Обеспечение качества' образовательного проекта VK Education команды Вкладыши.")
@allure.link("https://ads.vk.com", name="Website")

class TestPALegalEntity(BaseCase):
    # @pytest.mark.parametrize("link_num, link", [
    #         (1, 'https://ads.vk.com/cases'),
    #         (2, 'https://ads.vk.com/help/subcategories/agency'),
    #         (3, 'https://ads.vk.com/upvote')
    #         ])
    # def test_help_button(self, cabinet_page, link_num, link):
    #     cabinet_page.click_to_help_button()
    #     cabinet_page.redirect_to_help_button(link_num)
    #     cabinet_page.change_tab(cabinet_page.get_tab(-1))
    #     assert self.is_opened(link)
    #     cabinet_page.close_current_tab()
    #     cabinet_page.change_tab(cabinet_page.get_tab(0))


    def test_clients(self, cabinet_page):
        # cabinet_page.go_to_page("https://ads.vk.com/hq/dashboard")
        cabinet_page.click_to_clients()

    def test_budget(self, cabinet_page):
        # cabinet_page.go_to_page("https://ads.vk.com/hq/dashboard")
        cabinet_page.click_to_budget()
        cabinet_page.specify_banking_details()


    def test_access_right(self, cabinet_page):
        # cabinet_page.go_to_page("https://ads.vk.com/hq/dashboard")
        cabinet_page.click_to_access_right()
        cabinet_page.addManager("123","123")

    # def test_support_iframe(self, cabinet_page):
    #     cabinet_page.open_support_iframe(20)

    def test_top_navbar(self, cabinet_page):
        # cabinet_page.go_to_page("https://ads.vk.com/hq/dashboard")
        cabinet_page.click_to_VK_ico()
        assert self.is_opened('https://ads.vk.com/hq/dashboard')
        
        cabinet_page.click_to_user_name()
        cabinet_page.click_to_user_name()

        cabinet_page.click_to_bell()
        cabinet_page.check_bell_text_field()
        cabinet_page.click_to_bell()

        cabinet_page.user_log_out()
        assert self.is_opened('https://ads.vk.com/')