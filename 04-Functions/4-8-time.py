"""
Given the number of hours (0..23) and the number of minutes (0..59), returns a string specifying the time
in the given format ('24' for 24-hour time and '12' for 12-hour time)
"""


def time_string(hours, minutes, time_format):
    if time_format == '12':
        _time_string_12(hours, minutes)
    elif time_format == '24':
        _time_string_24(hours, minutes)
    else:
        raise ValueError('Time format must be either `12` or `24`.')


def _time_string_12(hours, minutes):
    if hours > 12:
        hours_am_pm = hours - 12
        am_pm = 'pm'
    elif 0 < hours <= 12:
        hours_am_pm = hours
        am_pm = 'am'
    else:
        hours_am_pm = 12
        am_pm = 'am'
    hours_str = str(hours_am_pm)
    minutes_str = str(minutes).zfill(2)

    print(f'{hours_str}:{minutes_str}{am_pm}')


def _time_string_24(hours, minutes):
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    print(f'{hours_str}:{minutes_str}')



time_string(15, 38, '24')  # returns '15:38'
time_string(8, 3, '24')  # returns '08:03'
time_string(0, 5, '24')  # returns '00:05'
time_string(11, 15, '12')  # returns '11:15am'
time_string(0, 7, '12')  # returns '12:07am'
time_string(7, 30, '12')  # returns '7:30am'
time_string(12, 46, '12')  # returns '12:46pm'
time_string(13, 10, '12')  # returns '1:10pm'
time_string(19, 2, '12')  # returns '7:02pm'
