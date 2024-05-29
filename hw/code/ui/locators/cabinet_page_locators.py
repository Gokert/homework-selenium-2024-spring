from selenium.webdriver.common.by import By

class CabinetPageLocators():
    @staticmethod
    def CLICK_BUTTON(section):
        return By.XPATH, f"//*[contains(@class, '{section}')]"

    NOTIFICATIONS_MODAL_PAGE = (By.XPATH, "//*[(@class, 'vkuiModalPage__in-wrap')]")
    USER_AVATAR = (By.XPATH, "//*[contains(@class, 'userMenu_avatar__')]")
    CONTROL_ID_BUTTON = (By.XPATH, "//*[contains(@class, 'userMenu_connectButton__')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'userMenu_logoutButton__')]")
    VK_ICON = (By.XPATH, "//*[contains(@class, 'header_logo__')]")
    EDUCATION_BUTTON = (By.XPATH, "//*[contains(@data-route, 'onboarding')]")
    EDUCATION_MODAL = (By.XPATH, "//*[contains(@class, 'ModalRoot_componentWrapper__')]")
    EDUCATION_EXIT = (By.XPATH, "//*[contains(@class, 'vkuiModalDismissButton')]")
    HELP_MODAL = (By.XPATH, "//*[contains(@class, 'Tooltip_tooltipContainer__')]")
    WELCOME_VK_PANEL = (By.XPATH, "//*[contains(@class, 'WelcomePanel_wrapper__')]")
    REVIEW_COMPANY = (By.XPATH, "//*[contains(@class, 'StatisticsPanel_wrapper__')]")
    COMPANY_BUTTON = (By.XPATH, "//*[contains(@class, 'EmptyView_fullViewContent__')]")
    COMPANY_LEFT_MENU = (By.XPATH, "//*[contains(@data-entityid, 'dashboardV2')]")
    AUDITORY_LEFT_MENU = (By.XPATH, '//*[@data-entityid="audience"]')
    AUDITORY_PANEL = (By.XPATH, "//*[contains(@class, 'tableLayout_table__')]")
    BUDGET_LEFT_MENU = (By.XPATH, '//*[@data-entityid="budget"]')
    BUDGET_PANEL = (By.XPATH, "//*[contains(@class, 'EmptyView_fullViewContent__')]")
    ONBOARD_LEFT_MENU = (By.XPATH, '//*[@data-entityid="onboarding"]')
    ONBOARD_PANEL = (By.XPATH, "//*[contains(@class, 'ModalRoot_componentWrapper__')]")
    CATALOGS_LEFT_MENU = (By.XPATH, '//*[@data-entityid="catalogs"]')
    CATALOGS_PANEL = (By.XPATH, "//*[contains(@class, 'CatalogsPlaceholder_placeHolderWrapper__')]")
    PIXELS_LEFT_MENU = (By.XPATH, '//*[@data-entityid="pixels"]')
    PIXELS_PANEL = (By.XPATH, "//*[contains(@class, 'EmptyView_fullViewContent__')]")
    MOBAPP_LEFT_MENU = (By.XPATH, '//*[@data-entityid="mobApps"]')
    MOBAPP_PANEL = (By.XPATH, "//*[contains(@class, 'EmptyView_fullViewContent__')]")
    LEADADS_LEFT_MENU = (By.XPATH, '//*[@data-entityid="leadads"]')
    CABINET_BODY = (By.XPATH, "//*[contains(@class, 'layout_content__')]")
    LEADADS_PANEL = (By.XPATH, "//*[contains(@class, 'EmptyView_fullViewContent__')]")
    AUTH_PANEL = (By.XPATH, "//*[contains(@class, 'vkc__AuthRoot__wrapper')]")
    MAIN_HEADER = (By.XPATH, "//*[contains(@class, 'Header_wrapper__')]")
