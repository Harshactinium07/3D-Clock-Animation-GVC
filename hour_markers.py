import maya.cmds as cmds
import math

if cmds.objExists("hour_markers_grp"):
    cmds.delete("hour_markers_grp")

grp = cmds.group(empty=True, name="hour_markers_grp")
radius = 5.0

for i in range(12):
    angle = math.radians(i * 30)
    x = radius * math.sin(angle)
    z = radius * math.cos(angle)

    marker = cmds.polyCube(w=0.15, h=0.3, d=0.15, name=f"hour_marker_{i}")[0]
    cmds.move(x, 0.31, z, marker)
    cmds.rotate(0, -(i * 30), 0, marker)
    cmds.parent(marker, grp)
