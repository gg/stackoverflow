#!/usr/bin/env python
# coding: utf-8

"""Suppose I am given number of lines segments in Cartesian coordinate system.
Each line segement is given as ((x0,y0), (x1,y1)), assuming x0 < x1. Write an
algorithm that finds a vertical line that crosses the maximum number of line
segments."""
def max_intersections(line_segments):
    """Returns the x value of a vertical line that crosses the maximum number of
    line segments. O(n lg n) complexity."""
    points = []
    for ((x0,y0), (x1,y1)) in line_segments:
        if x1 < x0:
            x0, x1 = x1, x0
        points.append((x0, True))
        points.append((x1, False))

    points = sorted(points)

    intersections = 0
    mx = 0
    x_vertical = None

    for (x, is_start) in points:
        if is_start:
            intersections += 1

            if intersections > mx:
                mx = intersections
                x_vertical = x
        else:
            intersections -= 1

    return x_vertical

if __name__ == "__main__":
    line_segments = [((1,3), (4, 2)), ((3, 3), (7, 6)), ((3, 5), (8, 8)),
                     ((6, 3), (10, 2)), ((6, 8), (11, 7))]
    x_vertical = max_intersections(line_segments)
    assert(x_vertical == 6)
