from django import template

register = template.Library()

@register.filter
def star_rating(value):
    """
    Возвращает список: ['full', 'full', 'half', 'empty', 'empty']
    """
    try:
        value = float(value)
    except (ValueError, TypeError):
        return ['empty'] * 5

    stars = []
    for i in range(1, 6):
        if value >= i:
            stars.append('full')
        elif value >= i - 0.5:
            stars.append('half')
        else:
            stars.append('empty')
    return stars
