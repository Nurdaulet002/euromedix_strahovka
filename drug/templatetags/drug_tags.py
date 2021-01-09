from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def condition_url(view_name, parent):
    url = 'tariffication:{0}'.format(view_name)
    if parent:
        resolved_url = reverse(url, kwargs={'parent': parent})
    else:
        resolved_url = reverse(url)
    return resolved_url


@register.simple_tag
def is_selected(base_id, specified_id):
	if str(base_id) == specified_id:
		return 'selected'
	else:
		return specified_id