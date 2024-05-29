from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.campaign_page_locators import CompanyPageLocators


class CompanyPage(BasePage):
    locators = CompanyPageLocators()
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'

    TARGET_ACTIONS_LIST = ['Сайт', 'Сообщество и профиль', 'VK Mini Apps и игры', 'Дзен', 'Каталог товаров', 'Одноклассники', 'Музыка', 'Мобильное приложение', 'Лид-формы и опросы', 'Видео и трансляции']
    REGION_BUTTON_LIST = ['Россия', 'Москва', 'Санкт-Петербург']
    REGION = 'Москва'
    TITLE = 'EyeScreen'
    DESC = 'Best films ever'
    SITE = 'https://hooli-smotrim.ru/'

    def has_action_select_content(self):
        return self.became_visible(self.locators.ACTION_SELECT)

    def has_action_list_content_cells(self):
        for t in self.TARGET_ACTIONS_LIST:
            if not self.became_visible(self.locators.ACTION_CELL(t)):
                return False
        return True

    def site_name_input_became_visible(self):
        return self.became_visible(self.locators.SITE_INPUT)

    def footer_became_visible(self):
        return self.became_visible(self.locators.CREATE_FOOTER)

    def continue_button_content(self):
        return self.became_visible(self.locators.CONTINUE_BUTTON)

    def publish_button_content(self):
        return self.became_visible(self.locators.PUBLISH_BUTTON)

    def click_continue_button(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def click_publish_button(self):
        self.click(self.locators.PUBLISH_BUTTON)

    def fill_site_name_with_valid_url(self):
        name = self.find(self.locators.SITE_INPUT)
        name.clear()
        name.send_keys(self.URL)

    def site_url_is_correct(self):
        name = self.find(self.locators.SITE_INPUT)
        name.clear()
        name.send_keys(self.SITE)

    def strategy_became_visible(self):
        return self.became_visible(self.locators.STRATEGY_SELECT)

    def budget_became_visible(self):
        return self.became_visible(self.locators.BUDGET_INPUT)

    def data_inputs_became_visible(self):
        return self.became_visible(self.locators.START_DATE) and self.became_visible(self.locators.END_DATE)

    def click_site_cell(self):
        self.click(self.locators.CATEGORY_CELL(self.TARGET_ACTIONS_LIST[0]))

    def fill_company_settings(self):
        budget = self.find(self.locators.BUDGET_INPUT)
        budget.send_keys(100500)
        self.click(self.locators.CREATE_FOOTER_CONTINUE)

    def check_company_budget(self):
        return self.became_visible(self.locators.BUDGET_CELL('100500'))

    def has_region_buttons_content(self):
        for r in self.REGION_BUTTON_LIST:
            if not self.became_visible(self.locators.REGION_BUTTON(r)):
                return False
        return True

    def choose_region_button(self):
        self.click(self.locators.REGION_BUTTON(self.REGION_BUTTON_NAME_LIST[1]))

    def has_company_title(self):
        return self.became_visible(self.locators.TITLE_INPUT)

    def has_company_description(self):
        return self.became_visible(self.locators.DESCRIPTION_INPUT)

    def file_input_became_visible(self):
        return self.became_visible(self.locators.FILE_INPUT)

    def fill_inputs(self):
        title = self.find(self.locators.TITLE_INPUT)
        title.clear()
        title.send_keys(self.TITLE)
        desc = self.find(self.locators.DESCRIPTION_INPUT)
        desc.clear()
        desc.send_keys(self.DESC)

    def click_file_input(self):
        self.click(self.locators.FILE_INPUT)

    def submit_button_became_visible(self):
        return self.became_visible(self.locators.SUBMIT_BUTTON)

    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    def delete_company(self):
        self.click(self.locators.ACTIONS_SELECT)
        self.click(self.locators.DROPDOWN_OPTIONS('Удалить'))

    def click_group_tabs(self):
        self.click(self.locators.ADS_PAGE_TABS(self.CAMPAIGN_PAGE_TABS_LIST[1]))

    def check_group_title(self):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(self.GROUP_NAME))

    def check_description(self):
        return self.find(self.locators.DESCRIPTION_INPUT).text == self.DESC

    def click_create_button(self):
        self.click(self.locators.CREATE_COMPANY_BUTTON)

    def action_select_became_visible(self):
        return self.became_visible(self.locators.ACTIONS_SELECT)

    def check_company_title(self):
        return self.became_visible(self.locators.ENTITY_NAME_CELL(self.CAMPAIGN_NAME))
