from base_case import BaseCase
from ui.locators.catalog_locators import FeedSources

class TestCommerceCenter(BaseCase):
    def test_open_side_menu(self, catalog_page):
        catalog_page.open_center()
        catalog_page.close_help_modal()
        catalog_page.open_catalog_creation()
        catalog_page.select_feed_source(FeedSources.URL)
        catalog_page.fill_feed_url(self.config['feed_url'])
        catalog_page.submit_catalog_creation()
        catalog_page.wait_for_feed_load()
        catalog_page.open_commerce_center()
        catalog_page.open_catalog_settings()
        catalog_page.wait_for_right_menu()
    
    def test_rename_catalog(self, catalog_page):
        catalog_page.open_center()
        catalog_page.close_help_modal()
        catalog_page.open_catalog_creation()
        catalog_page.select_feed_source(FeedSources.URL)
        catalog_page.fill_feed_url(self.config['feed_url'])
        catalog_page.submit_catalog_creation()
        catalog_page.wait_for_feed_load()
        catalog_page.open_commerce_center()
        catalog_page.open_catalog_settings()
        catalog_page.rename_catalog("new_catalog")
        
        assert "new_catalog" in catalog_page.driver.page_source
        catalog_page.clear_catalogs()
    
    def test_search_catalog_positive(self, catalog_page):
        catalog_page.open_center()
        catalog_page.close_help_modal()
        catalog_page.open_catalog_creation()
        catalog_page.select_feed_source(FeedSources.URL)
        catalog_page.fill_feed_url(self.config['feed_url'])
        catalog_page.submit_catalog_creation()
        catalog_page.wait_for_feed_load()
        catalog_page.open_commerce_center()
        catalog_page.open_catalog_settings()
        catalog_page.rename_catalog("new_catalog")
        catalog_page.search_catalog("new_catalog")

        assert "new_catalog" in catalog_page.driver.page_source
        catalog_page.clear_catalogs()

    def test_search_catalog_negative(self, catalog_page):
        catalog_page.open_center()
        catalog_page.close_help_modal()
        catalog_page.open_catalog_creation()
        catalog_page.select_feed_source(FeedSources.URL)
        catalog_page.fill_feed_url(self.config['feed_url'])
        catalog_page.submit_catalog_creation()
        catalog_page.wait_for_feed_load()
        catalog_page.open_commerce_center()
        catalog_page.open_catalog_settings()
        catalog_page.rename_catalog("new_catalog")
        catalog_page.search_catalog("not_existing_catalog")
        catalog_page.wait_for_lens()

        assert "Ничего не найдено" in catalog_page.driver.page_source

        catalog_page.search_catalog("")
        catalog_page.clear_catalogs()
