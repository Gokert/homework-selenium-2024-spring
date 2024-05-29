import time

from base_case import BaseCase

class TestAudiencePage(BaseCase):
    def test_is_create_audience_modal_page_opened(self, audience_page):
        audience_page.click_create_audience_button()
        assert audience_page.create_audience_modal_page_became_visible()
        assert audience_page.audience_name_input_became_visible()
        assert audience_page.has_sidebar_sign_content()
        assert audience_page.add_source_button_became_visible()
        assert audience_page.footer_buttons_became_visible()
        assert audience_page.cross_button_became_visible()

    def test_is_create_audience_modal_page_closed(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_cross_button()
        assert audience_page.create_audience_modal_page_became_invisible()
        audience_page.click_create_audience_button()
        audience_page.click_cancel_button()
        assert audience_page.create_audience_modal_page_became_invisible()

    def test_error_long_audience_name(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.enter_audience_name(
            "a" * (audience_page.MAX_LENGTH_OF_AUDIENCE_NAME + 1)
        )
        assert audience_page.get_error() == audience_page.ERROR_TOO_LONG_AUDIENCE_NAME

    def test_is_add_source_modal_page_became_visible(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        assert audience_page.add_source_modal_page_became_visible()
        assert audience_page.source_items_became_visible()

    def test_add_source_by_key_phrases(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(audience_page.SOURCE_NAME)
        audience_page.enter_key_phrases(audience_page.KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        source_card_content = audience_page.get_source_card_content()
        for key_phrase in audience_page.KEY_PHRASES:
            assert key_phrase in source_card_content

    def test_create_audience(self, audience_page):
        audience_page.click_create_audience_button()
        audience_page.click_add_source_button()
        audience_page.select_source(audience_page.SOURCE_NAME)
        audience_page.enter_key_phrases(audience_page.KEY_PHRASES)
        audience_page.click_modal_page_submit_button()
        audience_page.enter_audience_name(audience_page.CUSTOM_AUDIENCE_NAME)
        audience_page.click_modal_page_submit_button()
        assert (
                audience_page.get_created_audience_title()
                == audience_page.CUSTOM_AUDIENCE_NAME
        )
        audience_page.delete_audience()