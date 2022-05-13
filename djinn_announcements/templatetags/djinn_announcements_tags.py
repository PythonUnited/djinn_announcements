from django.template import Library
from djinn_announcements.settings import STATUS_CLASSES, STATUS_CLASSES_v3

register = Library()


@register.filter
def statusclass(status, version=None):

    if version == 'v3':
        return STATUS_CLASSES_v3.get(status, "")
    return STATUS_CLASSES.get(status, "")
