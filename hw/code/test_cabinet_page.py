import time

import pytest
from base_case import BaseCase


class TestCabinet(BaseCase):
    def test_cabinet(self, cabinet_page):
        assert self.is_opened('https://ads.vk.com/hq/overview')

