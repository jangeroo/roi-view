class App():
    def __init__(self, context):
        print(f'DEFAULT: Initializing app...\n')
        self.context = context

    def open_app_at(self, url):
        print(f'DEFAULT: opening app at {url}\n')

    def get_title(self):
        print(f'DEFAULT: Getting title\n')
        return f'Welcome to {self.context.app_title}!'
