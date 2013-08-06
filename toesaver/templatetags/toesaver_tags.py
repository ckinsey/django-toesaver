from django import template
from django.core.urlresolvers import reverse
from django.conf import settings

register = template.Library()

@register.inclusion_tag('toesaver/toesaver.js.html', takes_context=True)
def save_those_toes(context):
    request = context['request']
    new_context = {
        'current_view': request.path,
        'post_url': reverse('toesaver-ajax-report-view'),
        'get_url': reverse('toesaver-ajax-get-views'),
        'poll_frequency': (settings.TOESAVER_POLL_FREQUENCY * 1000),
        'view_timeout': (settings.TOESAVER_VIEW_TIMEOUT * 1000),
    }

    context.update(new_context)
    return context
