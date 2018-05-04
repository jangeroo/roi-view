@given('ROI viewer is running')
def step_impl(context):
    print(f'starting app...\n')


@when('I open \'http://localhost:3000\'')
def step_impl(context):
    print(f'opening localhost:3000\n')


@then('I should see the title \'{expected}\'')
def step_impl(context, expected):
    print(f'verifying title\n')


@then('I should see a percent-sign logo')
def step_impl(context):
    print(f'verifying logo\n')
