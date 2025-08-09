import time

def get_time_parts():
    """Return hours, minutes, seconds, am_pm"""
    t = time.localtime()
    hours = t.tm_hour % 12
    minutes = t.tm_min
    seconds = t.tm_sec
    am_pm = "AM" if t.tm_hour < 12 else "PM"
    return hours, minutes, seconds, am_pm

def time_string():
    """Return formatted time string in 12-hour format"""
    return time.strftime("%I:%M:%S")
