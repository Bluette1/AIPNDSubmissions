def readable_timedelta(days):
    """
    Calculates the number of weeks and days, from a given number of days
    :param days: the time change in days
    :return: the time change in readable format
    """
    weeks = days // 7
    remainder = days % 7

    return "{} week(s) and {} day(s)".format(weeks, remainder)

print("readable_timedelta(25):::::::::", readable_timedelta(25))