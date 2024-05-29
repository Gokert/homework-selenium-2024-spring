import time
from base_case import BaseCase


class TestUpvotePage(BaseCase):
    def test_search_by_title(self, upvote_page):
        word = 'видео'
        upvote_page.perform_search(word)
        time.sleep(1)
        assert word in upvote_page.get_first_idea_title()

    def test_search_by_id(self, upvote_page):
        idea_id = '48'
        upvote_page.perform_search(idea_id)
        time.sleep(1)
        assert idea_id == upvote_page.get_first_idea_id()

    def test_open_theme_dropdown(self, upvote_page):
        upvote_page.open_filter_dropdown('Любая тема')
        assert upvote_page.filter_dropdown_contain_items(upvote_page.THEMES)

    def test_open_status_dropdown(self, upvote_page):
        upvote_page.click_cancel_filter_button()
        upvote_page.open_filter_dropdown('Любой статус')
        assert upvote_page.filter_dropdown_contain_items(upvote_page.STATUSES)

    def test_filter_theme(self, upvote_page):
        upvote_page.open_filter_dropdown('Любая тема')

        theme = 'Лидформы'
        upvote_page.select_filter(theme)
        assert upvote_page.get_first_idea_theme() == theme

    def test_filter_status(self, upvote_page):
        upvote_page.click_cancel_filter_button()
        upvote_page.open_filter_dropdown('Любой статус')

        status = 'Уже в работе'
        upvote_page.select_filter(status)
        assert upvote_page.get_first_idea_status() == status