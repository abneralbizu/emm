"""EMM logo mark: a stone arch held together by a gold keystone that carries a cross.
The keystone is the stone that locks an arch in place, the way sound administration holds a ministry together.
Run  python3 tools/make_icons.py  after changing anything here."""
import math
SP="#14403C"; GD="#B8862B"
def cross(cx, top, h, w, t, arm_y):
    # single outline cross: vertical bar width t, height h; arm width w at y arm_y
    x0, x1 = cx - t/2, cx + t/2
    a0, a1 = cx - w/2, cx + w/2
    y0, y1 = arm_y, arm_y + t
    pts=[(x0,top),(x1,top),(x1,y0),(a1,y0),(a1,y1),(x1,y1),(x1,top+h),(x0,top+h),(x0,y1),(a0,y1),(a0,y0),(x0,y0)]
    return "M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)+" Z"
def mark(arch=SP, key=GD, crossc="#fff", gap="#fff", with_gaps=True):
    cx, cy, R, r = 80, 88, 70, 47          # arch centre, outer/inner radius
    legs = 134                              # bottom of legs
    # arch outer/inner path (semicircle + legs)
    d=(f"M{cx-R} {legs} V{cy} A{R} {R} 0 0 1 {cx+R} {cy} V{legs} H{cx+r} V{cy} A{r} {r} 0 0 0 {cx-r} {cy} V{legs} Z")
    # stone joints: radial lines at these angles (deg from left horizontal)
    joints=""
    if with_gaps:
        for ang in (0, 40, 140, 180):
            a=math.radians(180-ang)
            x0,y0=cx+math.cos(a)*(r-2), cy-math.sin(a)*(r-2)
            x1,y1=cx+math.cos(a)*(R+2), cy-math.sin(a)*(R+2)
            joints+=f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{gap}" stroke-width="4"/>'
    # keystone: wedge at top, wider at top, overlapping the arch
    kt, kb = 2, 54            # top / bottom y
    ktw, kbw = 27, 17         # half widths
    keystone=f'M{cx-ktw} {kt} H{cx+ktw} L{cx+kbw} {kb} H{cx-kbw} Z'
    # gap outline around keystone so it reads as a separate stone
    kgap=f'<path d="{keystone}" fill="none" stroke="{gap}" stroke-width="8" stroke-linejoin="round"/>' if with_gaps else ""
    c=cross(cx, 10, 37, 24, 7, 19)
    return (f'<path d="{d}" fill="{arch}"/>{joints}{kgap}'
            f'<path d="{keystone}" fill="{key}"/><path d="{c}" fill="{crossc}"/>')
def svg(inner, vb="0 0 160 136"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{inner}</svg>'
