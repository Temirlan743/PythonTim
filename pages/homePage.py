from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        wait = WebDriverWait(self.browser, 10)
        self.browser.get("https://demoblaze.com/index.html")



    def click_galaxy_s6(self):
        wait = WebDriverWait(self.browser, 10)
        galaxy_s6 = self.browser.find_element(By.XPATH,'//a[text()="Samsung galaxy s6"]')
        galaxy_s6.click()

    def check_products_count(self, count):
         wait = WebDriverWait(self.browser, 10)
         monitors = self.browser.find_elements(By.XPATH, '//div[@class="card h-100"]')
         assert len(monitors) == count

    def click_monitor(self):
        wait = WebDriverWait(self.browser, 10)
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitor_link.click()
