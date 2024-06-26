from base_case import BaseCase


class TestSetting(BaseCase):
    def test_header_general(self, settings_page):
        settings_page.click_header_general()
        assert self.is_opened('https://ads.vk.com/hq/settings')

    def test_header_notif(self, settings_page):
        settings_page.click_header_notif()
        assert self.is_opened('https://ads.vk.com/hq/settings/notifications')

    def test_header_access(self, settings_page):
        settings_page.click_header_access()
        assert self.is_opened('https://ads.vk.com/hq/settings/access')

    def test_header_logs(self, settings_page):
        settings_page.click_header_logs()
        assert self.is_opened('https://ads.vk.com/hq/settings/logs')
