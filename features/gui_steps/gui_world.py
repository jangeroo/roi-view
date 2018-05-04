from features.gui_steps.page_objects.home import Home


class WebApp():
    def __init__(self, context):
        self.browser = context.browser
        self.home = Home(context.browser)


class App(WebApp):
    def __init__(self, context):
        print(f'GUI: Initializing app...\n')
        super(App, self).__init__(context)

    def open_app_at(self, url):
        print(f'GUI: opening app at {url} in {self.browser.driver_name}\n')
        self.browser.visit(url)

    def get_title(self):
        print(f'GUI: Getting title\n')
        # return self.browser.find_by_css('.App-title').text
        return self.home.title.text
