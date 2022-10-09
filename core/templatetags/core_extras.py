from django import template

from core.utils import get_rqworker_count

register = template.Library()


@register.simple_tag
def rqworker_count():
    count = get_rqworker_count()
    return count
