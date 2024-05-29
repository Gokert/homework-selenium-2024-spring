from selenium.webdriver.common.by import By

class CompanyPageLocators:
    CREATE_COMPANY_BUTTON = (By.XPATH, "//*[@data-testid='create-button']")

    SITE_INPUT = (By.XPATH,"//*[contains(@class, 'vkuiFormItem') and .//*[contains(@class, 'FormItem_topText__') and text()='Рекламируемый сайт']]//input",)
    ACTION_SELECT = (By.XPATH, "//*[contains(@data-testid, 'autobidding-mode')]")

    @staticmethod
    def action_cell(sign):
        return (By.XPATH, f"//*[text()='{sign}']")

    STRATEGY_SELECT = (By.XPATH, "//*[contains(@data-testid, 'autobidding-mode')]")
    BUDGET_INPUT = (By.XPATH, "//*[@data-testid='targeting-not-set']")
    START_DATE = (By.XPATH, "//*[@data-testid='start-date']")
    END_DATE = (By.XPATH, "//*[@data-testid='end-date']")

    CONTINUE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text() = 'Продолжить']")
    PUBLISH_BUTTON = (By.XPATH, "//*[contains(@class, 'CreateFooter_footer__')]//*[contains(@class, 'vkuiButton__content') and text() = 'Опубликовать']")
    CREATE_FOOTER = (By.XPATH, "//*[contains(@class, 'CreateFooter_footer__')]")

    @staticmethod
    def REGION_BUTTON(region):
        return (By.XPATH, f"//*[contains(@class, 'vkuiButton__content') and text()='{region}']")

    TITLE_INPUT = (By.XPATH, "//*[contains(@class, 'vkuiFormItem') and .//*[text()='Заголовок']]//input")
    DESCRIPTION_INPUT = (By.XPATH, "//*[contains(@class, 'vkuiFormItem') and .//*[text()='Короткое описание']]//textarea")
    FILE_INPUT = (By.XPATH, "//*[@data-testid='set-global-image']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@data-testid='submit']")

    @staticmethod
    def DROPDOWN_OPTIONS(content):
        return (By.XPATH, f"//*[text()='{content}']")

    ACTIONS_SELECT = (By.XPATH, "//*[@data-testid='select-options']")

    @staticmethod
    def BUDGET_CELL(amount):
        return (By.XPATH, f"//*[contains(@class, 'budget_editable__') and text()='{amount}']")
