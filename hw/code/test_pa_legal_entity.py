import pytest
import allure
from base_case import BaseCase
from configs import test_help_button_parameters

@allure.title("Вкладыши: Личный кабинет(юридическое лицо)")
@allure.description("Домашнее задание 3 по курсу 'Обеспечение качества' образовательного проекта VK Education команды Вкладыши.")
@allure.tag("Личный кабинет ЮР. лица")
@allure.label("owner", "AlfaIV")
@allure.link("https://ads.vk.com", name="Website")

@allure.suite("Тестирование личного кабинета юридического лица")
class TestPALegalEntity(BaseCase):
    @allure.sub_suite("Проверка дропбокс меню, на иконке 'Помощь'")
    @pytest.mark.parametrize("link_num, link", test_help_button_parameters)
    def test_help_button(self, legal_entity_page, link_num, link):
        legal_entity_page.click_to_help_button()
        legal_entity_page.redirect_to_help_button(link_num)
        legal_entity_page.change_tab(legal_entity_page.get_tab(-1))
        assert self.is_opened(link)
        legal_entity_page.close_current_tab()
        legal_entity_page.change_tab(legal_entity_page.get_tab(0))

    @allure.sub_suite("Тестирование вкладки 'Клиенты'")
    def test_clients(self, legal_entity_page):
        legal_entity_page.click_to_clients()
        assert self.is_opened("https://ads.vk.com/hq/dashboard")

    @allure.sub_suite("Тестирование вкладки 'Бюджет'")
    def test_budget(self, legal_entity_page):
        legal_entity_page.click_to_budget()
        legal_entity_page.specify_banking_details()

    @allure.sub_suite("Тестирование вкладки 'Права доступа'")
    def test_access_right(self, legal_entity_page):
        legal_entity_page.click_to_access_right()
        legal_entity_page.addManager("123","123")

    @allure.sub_suite("Тестирование меню поддержки")
    def test_support_iframe(self, legal_entity_page):
        legal_entity_page.open_support_iframe(30)
        legal_entity_page.close_support_iframe(10)

    @allure.sub_suite("Тестирование навигационного меню")
    def test_top_navbar(self, legal_entity_page):
        legal_entity_page.click_to_VK_ico()
        assert self.is_opened('https://ads.vk.com/hq/dashboard')
        
        legal_entity_page.click_to_user_name()
        legal_entity_page.click_to_user_name()

        legal_entity_page.click_to_bell()
        empty_text = legal_entity_page.check_bell_text_field()
        assert empty_text[0] == "Уведомления"
        assert empty_text[1] == "Нет уведомлений"
        assert empty_text[2] == "Как только у вас появятся уведомления, они отобразятся здесь"

        legal_entity_page.click_to_bell()

        legal_entity_page.user_log_out()
        assert self.is_opened('https://ads.vk.com/')