from django.templatetags.static import static
from django.urls import reverse
import builtins
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        "g": builtins
    })
    return env