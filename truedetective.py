def is_twodigit_odd(number):
    return True if number % 2 == 1 and len(str(number)) == 2 else False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return True if ((user == file_owner) and (writable_by_owner or sudo_mode) or (sudo_mode) or (writable_by_others) or (file_group in users_groups) and writable_by_group) else False


def is_leap_year(year):
    return True if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0) else False


def is_sunday(day, weekday_of_first):
    return True if (weekday_of_first == 'M' and day % 7 == 0) or (weekday_of_first == 'Tu' and (day + 1) % 7 == 0) \
        or (weekday_of_first == 'W' and (day + 2) % 7 == 0) or (weekday_of_first == 'Th' and (day + 3) % 7 == 0) \
        or (weekday_of_first == 'F' and (day + 4) % 7 == 0) or (weekday_of_first == "Sa" and (day + 5) % 7 == 0) \
        or (weekday_of_first == "Su" and (day + 6) % 7 == 0) else False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return True if (rains and (wind_scale < 7)) \
                   or (cloudy and (wind_scale < 7) and (red_sky or strong_flower_smell or spiders_down or lying_cattle)) \
                   or (strong_sunshine and (wind_scale < 7)) else False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass
