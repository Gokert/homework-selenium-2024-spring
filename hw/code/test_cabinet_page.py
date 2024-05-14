import pytest
from base_case import BaseCase
from configs import left_menu_clicked


class TestCabinet(BaseCase):
    def test_cabinet_home(self, cabinet_page):
        assert self.is_opened('https://ads.vk.com/hq/overview')

    @pytest.mark.parametrize("name,url", left_menu_clicked)
    def test_menu(self, cabinet_page, name, url):
        cabinet_page.click_left_menu(name)
        assert self.is_opened(url)

    def test_help(self, cabinet_page):
        cabinet_page.click_help()
        assert cabinet_page.check_modal_page_help()

    def test_control_id(self, cabinet_page):
        cabinet_page.click_user_avatar()
        cabinet_page.click_control_id()
        assert self.is_opened('https://id.vk.com/auth')

    def test_logout(self, cabinet_page):
        cabinet_page.click_user_avatar()
        cabinet_page.click_logout_button()
        assert self.is_opened('https://ads.vk.com/')
