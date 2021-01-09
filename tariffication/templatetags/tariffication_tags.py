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
def is_selected(val1, val2):
    if str(val1) == str(val2):
        return 'selected'
    else:
        return ''


@register.simple_tag
def type_url(type, parent):
    if type == 1:
        resolved_url = reverse('tariffication:tariffication_list',
                               kwargs={'parent': parent})
    elif type == 2:
        resolved_url = reverse(
            'tariffication:compulsory_package_list', kwargs={'parent': parent})
    elif type == 3:
        resolved_url = reverse(
            'tariffication:compulsory_profession_package',
            kwargs={'parent': parent})

    return resolved_url


@register.simple_tag
def access_check(hospital):
    if hospital:
        return ''
    else:
        return 'checked disabled'
