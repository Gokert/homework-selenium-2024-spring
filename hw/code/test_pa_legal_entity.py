import time
import pytest
import allure
from base_case import BaseCase

@allure.title("Вкладыши: Личный кабинет(юридическое лицо) ")
@allure.description("Домашнее задание 3 по курсу 'Обеспечение качества' образовательного проекта VK Education команды Вкладыши.")
@allure.link("https://ads.vk.com", name="Website")

class TestPALegalEntity(BaseCase):
    @pytest.mark.parametrize("link_num, link", [
            (1, 'https://ads.vk.com/cases'),
            (2, 'https://ads.vk.com/help/subcategories/agency'),
            (3, 'https://ads.vk.com/upvote')
            ])
    def test_help_button(self, legal_entity_page, link_num, link):
        legal_entity_page.click_to_help_button()
        legal_entity_page.redirect_to_help_button(link_num)
        legal_entity_page.change_tab(legal_entity_page.get_tab(-1))
        assert self.is_opened(link)
        legal_entity_page.close_current_tab()
        legal_entity_page.change_tab(legal_entity_page.get_tab(0))


    def test_clients(self, legal_entity_page):
        legal_entity_page.click_to_clients()
        assert self.is_opened("https://ads.vk.com/hq/dashboard")

    def test_budget(self, legal_entity_page):
        legal_entity_page.click_to_budget()
        legal_entity_page.specify_banking_details()


    def test_access_right(self, legal_entity_page):
        legal_entity_page.click_to_access_right()
        legal_entity_page.addManager("123","123")

    # def test_support_iframe(self, legal_entity_page):
    #     legal_entity_page.open_support_iframe(20)

    def test_top_navbar(self, legal_entity_page):
        legal_entity_page.click_to_VK_ico()
        assert self.is_opened('https://ads.vk.com/hq/dashboard')
        
        legal_entity_page.click_to_user_name()
        legal_entity_page.click_to_user_name()

        legal_entity_page.click_to_bell()
        legal_entity_page.check_bell_text_field()
        legal_entity_page.click_to_bell()

        legal_entity_page.user_log_out()
        assert self.is_opened('https://ads.vk.com/')