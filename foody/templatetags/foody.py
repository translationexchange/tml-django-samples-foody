from django.template.library import Library

register = Library()


@register.filter(is_safe=True)
def to_int(value, default='0'):
    try:
        return int(value)
    except ValueError:
        # quotient
        if not '/' in value:
            return default
        try:
            num, denom = map(int, value.split('/'))
            return float(num) / denom
        except ValueError:
            return default
        