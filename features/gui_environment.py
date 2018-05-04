# -- FILE: features/environment.py
from behave import use_fixture

from fixtures import splinter_browser


def before_all(context):
    use_fixture(splinter_browser, context)
# -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.


def before_scenario(context, scenario):
    context.browser.cookies.delete()
