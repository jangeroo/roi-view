from features.steps.default_world import App


def before_all(context):
    context.app = App(context)
