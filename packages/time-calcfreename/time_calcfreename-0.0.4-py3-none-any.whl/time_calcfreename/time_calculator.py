from datetime import datetime, timedelta


def add_seconds(secs: float) -> datetime:
    """Calculates the exact time after a specified number of seconds have passed
    secs: number of seconds to add"""
    current_time = datetime.now()
    return current_time + timedelta(seconds=secs)
