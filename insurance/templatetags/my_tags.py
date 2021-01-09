from urllib.parse import urlencode
from django import template
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def is_selected(val1, val2):
    if str(val1) == str(val2):
        return 'selected'
    else:
        return ''


@register.simple_tag
def get_insur_tarif(user, tariffication, insur_tarif):
    insur_tarif_q = insur_tarif.filter(
        insurance=user.profile.insurance, tariffication=tariffication)
    if insur_tarif_q.exists():
        return insur_tarif_q.last()
    else:
        return {'omo_price': 0, 'opmo_price': 0}


@register.simple_tag
def get_insur_drug(user, drug, insur_drug):
    insur_drug_q = insur_drug.filter(
        insurance=user.profile.insurance, drug=drug)
    if insur_drug_q.exists():
        return insur_drug_q.last()
    else:
        return {'omo_price': 0, 'opmo_price': 0}


def construct_query_string(context, query_params):
    # empty values will be removed
    query_string = context["request"].path
    if len(query_params):
        encoded_params = urlencode([
            (key, force_str(value))
            for (key, value) in query_params if value
        ]).replace("&", "&amp;")
        query_string += f"?{encoded_params}"
    return mark_safe(query_string)


@register.simple_tag(takes_context=True)
def modify_query(context, *params_to_remove, **params_to_change):
    """Renders a link with modified current query parameters"""
    query_params = []
    for key, value_list in context["request"].GET.lists():
        if key not in params_to_remove:
            # don't add key-value pairs for params_to_remove
            if key in params_to_change:
                # update values for keys in params_to_change
                query_params.append((key, params_to_change[key]))
                params_to_change.pop(key)
            else:
                # leave existing parameters as they were
                # if not mentioned in the params_to_change
                for value in value_list:
                    query_params.append((key, value))
                    # attach new params
    for key, value in params_to_change.items():
        query_params.append((key, value))
    return construct_query_string(context, query_params)


@register.simple_tag(takes_context=True)
def add_to_query(context, *params_to_remove, **params_to_add):
    """Renders a link with modified current query parameters"""
    query_params = []
    # go through current query params..
    for key, value_list in context["request"].GET.lists():
        if key not in params_to_remove:
            # don't add key-value pairs which already
            # exist in the query
            if (key in params_to_add and params_to_add[key] in value_list):
                params_to_add.pop(key)
            for value in value_list:
                query_params.append((key, value))
    # add the rest key-value pairs
    for key, value in params_to_add.items():
        query_params.append((key, value))
    return construct_query_string(context, query_params)


@register.simple_tag(takes_context=True)
def remove_from_query(context, *args, **kwargs):
    """Renders a link with modified current query parameters"""
    query_params = []
    # go through current query params..
    for key, value_list in context["request"].GET.lists():
        # skip keys mentioned in the args
        if key not in args:
            for value in value_list:
                # skip key-value pairs mentioned in kwargs
                if not (key in kwargs and str(value) == str(kwargs[key])):
                    query_params.append((key, value))
    return construct_query_string(context, query_params)
