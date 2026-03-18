
import time
from pages.homePage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.click_galaxy_s6()
    product = ProductPage(browser)
    product.check_title_is('Samsung galaxy s6')



def test_open_s7(browser):
    home_page = HomePage(browser)
    home_page.open()
    time.sleep(3)
    home_page.click_monitor()
    time.sleep(3)
    home_page.check_products_count(2)
