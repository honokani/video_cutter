import datetime as dttm

DEFAULT_TIME_FORMAT = "%H:%M:%S.%f"

def timeStr2frameCustom(s, fps, f):
    t = dttm.datetime.strptime(s, f)
    delta = dttm.timedelta( hours=t.hour
                          , minutes=t.minute
                          , seconds=t.second
                          , microseconds=t.microsecond
                          )
    return delta.total_seconds() * fps

def timeStr2frame(s, fps):
    return timeStr2frameCustom(s, fps, DEFAULT_TIME_FORMAT)

#
# def main():
#     print(timeStr2frame("0:0:3.456",10))
#
# if __name__ == '__main__':
#     main()
#

