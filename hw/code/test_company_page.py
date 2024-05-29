import time
from base_case import BaseCase


class TestCampanyPage(BaseCase):
    def test_create_company(self, company_page):
        company_page.click_create_button()

        assert company_page.has_action_select_content()
        assert company_page.has_action_list_content_cells()

        company_page.click_site_cell()

        assert company_page.site_name_input_became_visible()

        company_page.fill_site_name_with_valid_url()

        assert company_page.budget_became_visible()
        assert company_page.data_inputs_became_visible()
        assert company_page.footer_became_visible()
        assert company_page.continue_button_content()

        company_page.fill_company_settings()
        company_page.click_continue_button()

        assert company_page.has_region_buttons_content()

        company_page.choose_region_button()
        company_page.click_continue_button()

        assert company_page.has_company_title()
        assert company_page.has_company_description()
        assert company_page.file_input_became_visible()

        company_page.click_file_input()
        company_page.fill_inputs()

        assert company_page.submit_button_became_visible()

        company_page.click_submit_button()
        time.sleep(10)
        company_page.click_publish_button()

        assert self.is_opened('https://ads.vk.com/hq/dashboard/ad_plans')
        assert company_page.action_select_became_visible()
        assert company_page.check_company_budget()

        company_page.hover_campany_title()
        company_page.delete_entity()

        assert not company_page.check_company_budget()
