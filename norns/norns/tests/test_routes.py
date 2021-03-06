"""
Core app tests.
"""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class HomeViewUnitTests(TestCase):
    """
    Test for Unit Profile.
    """

    def test_get_about_page(self):
        """
        Test about page.
        """
        response = self.client.get(reverse_lazy('about'))
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_home_page(self):
        """
        Test home page.
        """
        response = self.client.get(reverse_lazy('home'))
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_get_store_page(self):
        """
        Test store page.
        """
        response = self.client.get(reverse_lazy('store'))
        self.assertTemplateUsed(response, 'store.html')
        self.assertTemplateUsed(response, 'base.html')


class LiveServerTests(StaticLiveServerTestCase):
    """
    Test live server rendering.
    """

    @classmethod
    def setUpClass(cls):
        """
        Initialize a selenium driver.
        """
        super().setUpClass()
        options = Options()
        options.headless = True
        cls.selenium = WebDriver(options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        """
        Destroy a selenium driver.
        """
        cls.selenium.quit()
        del cls.selenium
        super().tearDownClass()

    def test_about(self):
        """
        Test a browser rendering of about page.
        """
        self.selenium.get('{}/about'.format(self.live_server_url))

    def test_home(self):
        """
        Test a browser rendering of home page.
        """
        self.selenium.get('{}/'.format(self.live_server_url))

    def test_store(self):
        """
        Test a browser rendering of store page.
        """
        self.selenium.get('{}/store'.format(self.live_server_url))
