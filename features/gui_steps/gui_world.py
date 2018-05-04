class App():
    def __init__(self, context):
        print(f'GUI: Initializing app...\n')
        self.browser = context.browser

    def open_app_at(self, url):
        print(f'GUI: opening app at {url} in {self.browser.driver_name}\n')
        self.browser.visit(url)

    def get_title(self):
        print(f'GUI: Getting title\n')
        return self.browser.find_by_css('.App-title').text
