from behave import given, when, then


@given('{app_title} is running')
def step_impl(context, app_title):
    context.app_title = app_title


@when('I open \'{url}\'')
def step_impl(context, url):
    context.app.open_app_at(url)


@then('I should see the title \'{title}\'')
def step_impl(context, title):
    actual = context.app.get_title()
    assert actual == title


@then('I should see a percent-sign logo')
def step_impl(context):
    print(f'verifying logo\n')
