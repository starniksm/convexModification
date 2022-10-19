#!/usr/bin/env -S python3 -B
from convex import Void, Point, Segment, Polygon
from r2point import R2Point
from tk_drawer import TkDrawer
from deq import Deq


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())
        for r in range(2, self.points.size() - 1):
            if self.points.first().dist(self.points.medium(r)) == self.min_d():
                tk.draw_line(self.points.first(), self.points.medium(r))


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)

tk = TkDrawer()
f = Void()
tk.clean()

try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, M = {f.min_d()}\n")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
