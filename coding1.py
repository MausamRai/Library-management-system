from datetime import datetime, date


def getDate():
    Date = date.today()
    return Date

def time():
    time = datetime.today()
    return str(time.strftime("%H: %M: %S"))


