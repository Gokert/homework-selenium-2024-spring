from selenium.webdriver.common.by import By


class MainPageLocators():
    PAGE_ELEMENTS = {
        "VK_NEWS_BTN": ("Новости", "/news"),
        "CASES_BTN": ("Кейсы", "/cases"),
        "IDEAS_FORUM_BTN": ("Форум идей", "/upvote"),
        "MONETIZATION_BTN": ("Монетизация", "/partner"),
        "INFORMATION_BTN": ("Справка", "/help"),
        "HELP_BTN": ("Помощь", "/help"),
        "INSIGHTS_BTN": ("Полезные материалы", "/insights"),
        "EVENTS_BTN": ("Мероприятия", "/events"),
        "VIDEO_COURSES_BTN": ("Видеокурсы", "https://expert.vk.com/catalog/courses/"),
        "CERTIFICATION_BTN": ("Сертификация", "https://expert.vk.com/certification/"),
        "DOCUMENTS_BTN": ("Документы", "/documents"),
        "BUSINESS_EDUCATION_BTN": ("Обучение для бизнеса", "https://expert.vk.com/"),
    }

    VK_LOGO = (By.XPATH, "//*[contains(@class, 'HeaderLeft_home__')]")
    CABINET_NAV_BTN = (By.XPATH, "//*[contains(@class, 'NavigationVKAds_right__')]//*[contains(@class, 'ButtonCabinet_primary__')]")
    VIEW_ALL_CASES_BTN = (By.XPATH, "//*[contains(@class, 'styles_all__') and contains(@href, '/cases')]")
    CASE_LINK_LOCATOR = (By.XPATH, "//*[contains(@class, 'Case_link__')]")
    CASE_TITLE_LOCATOR = (By.XPATH, "//*[contains(@class, 'Case_title__')]")
    NEW_CASE_TITLE_LOCATOR = (By.XPATH, "//*[contains(@class, 'Summary_title__')]")
    WEBINARS_BTN = (By.XPATH, "//*[contains(@class, 'GetStarted_button__')]")
    NEWS_BTN = (By.XPATH, "//*[contains(@class, 'News_button__')]")
    FOOTER_CABINET_BTN = (By.XPATH, "//*[contains(@class, 'Footer_leftContent__')]//*[contains(@class, 'ButtonCabinet_primary__')]")
    EDUCATION_DROPDOWN_BTN = (By.XPATH, "//*[contains(@class, 'NavigationVKAdsItem_item__') and text()='Обучение']")

    @staticmethod
    def nav_item_locator(href):
        return (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_link__') and contains(@href, '{href}')]")

    @staticmethod
    def dropdown_menu_item_locator(href):
        return (By.XPATH, f"//*[contains(@class, 'SubNavigationItem_content__') and contains(@href, '{href}')]")

    @staticmethod
    def footer_section_locator(href):
        return (By.XPATH, f"//*[contains(@class, 'Footer_item__')]//*[contains(@href, '{href}')]")

    @staticmethod
    def get_button_locator(button_name):
        button_text, href = MainPageLocators.PAGE_ELEMENTS[button_name]
        return (By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_link__') and contains(@href, '{href}') and text()='{button_text}']")

    @staticmethod
    def get_dropdown_item_locator(button_name):
        _, href = MainPageLocators.PAGE_ELEMENTS[button_name]
        return (By.XPATH, f"//*[contains(@class, 'SubNavigationItem_content__') and contains(@href, '{href}')]")
