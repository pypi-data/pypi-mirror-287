from django import template

from ..utils import get_breadcrumbs_settings

register = template.Library()
settings = get_breadcrumbs_settings()


@register.inclusion_tag(settings['template'], takes_context=True)
def show_breadcrumbs(context):
    return {'breadcrumbs': context.get('breadcrumbs', [])}
