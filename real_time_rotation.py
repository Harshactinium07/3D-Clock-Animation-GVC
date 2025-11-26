import maya.cmds as cmds
import datetime

hour_pivot = "hour_pivot"
minute_pivot = "minute_pivot"
second_pivot = "second_pivot"

def update_clock(*args):
    now = datetime.datetime.now()

    hr = now.hour % 12
    min = now.minute
    sec = now.second

    hr_angle = -(hr*30 + min*0.5)
    min_angle = -(min*6)
    sec_angle = -(sec*6)

    cmds.rotate(0, hr_angle, 0, hour_pivot)
    cmds.rotate(0, min_angle, 0, minute_pivot)
    cmds.rotate(0, sec_angle, 0, second_pivot)

    cmds.scriptJob(runOnce=True, idleEvent=update_clock)

update_clock()
