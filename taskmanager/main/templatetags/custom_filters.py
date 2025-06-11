from django import template

register = template.Library()

@register.filter
def star_rating(value):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return []

    stars = []
    full_stars = int(value)
    half_star = value - full_stars >= 0.5
    empty_stars = 5 - full_stars - int(half_star)

    stars.extend(['full'] * full_stars)
    if half_star:
        stars.append('half')
    stars.extend(['empty'] * empty_stars)

    return stars
