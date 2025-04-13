from window import Window
from point import Point
from line import Line

win = Window(800, 600)
point1 = Point(100, 100)
point2 = Point(200, 200)
line = Line(point1, point2)
win.draw_line(line, "red")

win.wait_for_close()