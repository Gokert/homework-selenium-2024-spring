from base_case import BaseCase


class TestMainPage(BaseCase):
    def test_go_to_main_page_nav(self, main_page):
        main_page.click_vk_logo()
        assert self.is_opened("https://ads.vk.com/")

    def test_go_to_news_page_nav(self, main_page):
        main_page.click_nav_button("VK_NEWS_BTN")
        assert self.is_opened("https://ads.vk.com/news")

    def test_go_to_cases_page_nav(self, main_page):
        main_page.click_nav_button("CASES_BTN")
        assert self.is_opened("https://ads.vk.com/cases")

    def test_go_to_ideas_forum_page_nav(self, main_page):
        main_page.click_nav_button("IDEAS_FORUM_BTN")
        assert self.is_opened("https://ads.vk.com/upvote")

    def test_go_to_monetization_page_nav(self, main_page):
        main_page.click_nav_button("MONETIZATION_BTN")
        main_page.switch_to_new_tab()
        assert self.is_opened("https://ads.vk.com/partner")

    def test_go_to_help_page_nav(self, main_page):
        main_page.click_nav_button("INFORMATION_BTN")
        assert self.is_opened("https://ads.vk.com/help")

    def test_go_to_insights_nav(self, main_page):
        main_page.open_education_dropdown_menu()
        main_page.click_dropdown_menu_button("INSIGHTS_BTN")
        assert self.is_opened("https://ads.vk.com/insights")

    def test_go_to_events_nav(self, main_page):
        main_page.open_education_dropdown_menu()
        main_page.click_dropdown_menu_button("EVENTS_BTN")
        assert self.is_opened("https://ads.vk.com/events")

    def test_go_to_videocourses_nav(self, main_page):
        main_page.open_education_dropdown_menu()
        main_page.click_dropdown_menu_button("VIDEO_COURSES_BTN")
        main_page.switch_to_new_tab()
        assert self.is_opened("https://expert.vk.com/catalog/courses/")

    def test_go_to_certification_nav(self, main_page):
        main_page.open_education_dropdown_menu()
        main_page.click_dropdown_menu_button("CERTIFICATION_BTN")
        main_page.switch_to_new_tab()
        assert self.is_opened("https://expert.vk.com/certification/")

    def test_go_to_auth_page_nav(self, main_page):
        main_page.click_cabinet_nav_button()
        assert self.is_opened("https://id.vk.com/auth")

    def test_go_to_all_case_page(self, main_page):
        main_page.click_view_all_cases()
        assert self.is_opened("https://ads.vk.com/cases")

    # def test_go_to_example_case_page(self, main_page):
    #     raw_title = main_page.get_case_title_text(new_page=False)
    #     main_page.click_case_link()
    #     new_title = main_page.get_case_title_text(new_page=True)
    #     print(new_title, raw_title)
    #     assert self.is_opened("https://ads.vk.com/cases")
    #     assert raw_title == new_title

    def test_go_to_webinar(self, main_page):
        main_page.click_webinar_button()
        assert self.is_opened("https://ads.vk.com/events")

    def test_go_to_news(self, main_page):
        main_page.click_news_button()
        assert self.is_opened("https://ads.vk.com/news")

    def test_go_to_auth_page_footer(self, main_page):
        main_page.click_footer_cabinet_button()
        assert self.is_opened("https://id.vk.com/auth")

    def test_go_to_news_page_footer(self, main_page):
        main_page.click_footer_section_button("VK_NEWS_BTN")
        assert self.is_opened("https://ads.vk.com/news")

    def test_go_to_insights_page_footer(self, main_page):
        main_page.click_footer_section_button("INSIGHTS_BTN")
        assert self.is_opened("https://ads.vk.com/insights")

    def test_go_to_events_page_footer(self, main_page):
        main_page.click_footer_section_button("EVENTS_BTN")
        assert self.is_opened("https://ads.vk.com/events")

    def test_go_to_documents_page_footer(self, main_page):
        main_page.click_footer_section_button("DOCUMENTS_BTN")
        assert self.is_opened("https://ads.vk.com/documents")

    def test_go_to_business_education_page_footer(self, main_page):
        main_page.click_footer_section_button("BUSINESS_EDUCATION_BTN")
        main_page.switch_to_new_tab()
        assert self.is_opened("https://expert.vk.com/")

    def test_go_to_cases_page_footer(self, main_page):
        main_page.click_footer_section_button("CASES_BTN")
        assert self.is_opened("https://ads.vk.com/cases")

    def test_go_to_help_page_footer(self, main_page):
        main_page.click_footer_section_button("HELP_BTN")
        assert self.is_opened("https://ads.vk.com/help")

    def test_go_to_monetization_page_footer(self, main_page):
        main_page.click_footer_section_button("MONETIZATION_BTN")
        main_page.switch_to_new_tab()
        assert self.is_opened("https://ads.vk.com/partner")
