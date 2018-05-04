class Home():
    def __init__(self, browser):
        self.browser = browser

    @property
    def title(self):
        return self.browser.find_by_css('.App-title')
