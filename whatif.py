def is_twodigit_odd(number):
    if number % 2 == 0:
        return False
    else:
        if len(str(number)) == 2:
            return True
        else:
            return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    if user == file_owner:
        if writable_by_owner:
            return True
        elif sudo_mode:
            return True
        return False
    else:
        if sudo_mode:
            return True
        else:
            if writable_by_others:
                return True
            else:
                if file_group in users_groups:
                    if writable_by_group:
                        return True
                return False


def is_leap_year(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        else:
            if year % 400 == 0:
                return True
            else:
                if year % 4 == 0:
                    return True


def is_sunday(day, weekday_of_first):
    if weekday_of_first == 'M':
        first_day = 0
    elif weekday_of_first == 'Tu':
        first_day = 1
    elif weekday_of_first == 'W':
        first_day = 2
    elif weekday_of_first == 'Th':
        first_day = 3
    elif weekday_of_first == 'F':
        first_day = 4
    elif weekday_of_first == 'Sa':
        first_day = 5
    elif weekday_of_first == 'Su':
        first_day = 6

    if (day + first_day) % 7 == 0:
        return True
    else:
        return False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if rains:
        if wind_scale < 7:
            return True
        return False
    if cloudy:
        if wind_scale < 7:
            if red_sky:
                return True
            if strong_flower_smell:
                return True
            if spiders_down:
                return True
            if lying_cattle:
                return True
        return False
    if strong_sunshine:
        if wind_scale < 7:
            return True
        return False
    else:
        return False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if want_to:
        if trouble_sleeping:
            return False
        else:
            if after_4pm:
                return False
            else:
                if at_work:
                    if mad_boss:
                        return False
                    else:
                        if have_30m:
                            return True
                        else:
                            if have_10m:
                                return True
                            return False
                else:
                    if have_30m:
                        return True
                    else:
                        if have_10m:
                            return True
                        return False
    else:
        return False
