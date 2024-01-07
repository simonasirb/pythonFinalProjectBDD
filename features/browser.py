from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
