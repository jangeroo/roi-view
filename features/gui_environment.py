from behave import use_fixture

from fixtures import splinter_browser
# from features.gui_steps.gui_world import App


def before_all(context):
    use_fixture(splinter_browser, context)
    # context.app = App(context)


def before_scenario(context, scenario):
    context.browser.cookies.delete()
