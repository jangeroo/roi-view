from behave import fixture
from splinter import Browser


@fixture
def splinter_browser(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    context.browser = Browser(context.config.userdata.get('browser', 'chrome'))
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()
