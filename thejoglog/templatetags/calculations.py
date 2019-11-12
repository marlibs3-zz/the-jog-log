from django import template

register = template.Library()


def calculate_kph(distance, time):
    time_in_hours = time / 60
    return distance / time_in_hours


# VO2~= 2.209 + 3.1633 * kph
def calculate_vo2(distance, time):
    kph = calculate_kph(distance, time)
    return 2.209 + 3.1633 * kph


# Kcal/Min ~= 4.86 * massKg * VO2 / 1000
@register.simple_tag
def calculate_total_calories(distance, time, weight):
    vo2 = calculate_vo2(distance, time)
    kcal_per_minute = 4.86 * weight * vo2 / 1000
    return kcal_per_minute * time
