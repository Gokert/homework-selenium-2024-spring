import time
import pytest
from base_case import BaseCase

left_menu_clicked = [
    ('Сайты', 'https://ads.vk.com/hq/pixels'),
    ('Мобильные приложения', 'https://ads.vk.com/hq/apps'),
    ('Аудитории', 'https://ads.vk.com/hq/audience'),
    ('Бюджет', 'https://ads.vk.com/hq/budget/transactions'),
    ('Центр коммерции', 'https://ads.vk.com/hq/ecomm/catalogs'),
    ('Лид-формы', 'https://ads.vk.com/hq/leadads/leadforms'),
    ('Настройки', 'https://ads.vk.com/hq/settings'),
    ('Обзор', 'https://ads.vk.com/hq/overview'),
]


class TestCabinet1(BaseCase):
    def test_cabinet_home(self, cabinet_page):
        assert self.is_opened('https://ads.vk.com/hq/overview')

    @pytest.mark.parametrize("name,url", left_menu_clicked)
    def test_menu(self, cabinet_page, name, url):
        cabinet_page.click_left_menu(name)
        assert self.is_opened(url)

    def test_VkIcon(self, cabinet_page):
        cabinet_page.click_vk_icon()
        assert self.is_opened('https://ads.vk.com/hq/overview')

    def test_logout(self, cabinet_page):
        cabinet_page.click_user_avatar()
        cabinet_page.click_logout_button()
        assert self.is_opened('https://ads.vk.com/')

