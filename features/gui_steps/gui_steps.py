@given('ROI viewer is running')
def step_impl(context):
    print(f'starting app...\n')


@when('I open \'http://localhost:3000\'')
def step_impl(context):
    print(f'opening localhost:3000\n')
    context.browser.visit('http://localhost:3000')


@then('I should see the title \'{expected}\'')
def step_impl(context, expected):
    print(f'verifying title\n')
    title = context.browser.find_by_css('.App-title').text
    assert title == expected


@then('I should see a percent-sign logo')
def step_impl(context):
    print(f'verifying logo\n')
