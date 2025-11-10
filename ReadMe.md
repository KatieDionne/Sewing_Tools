This repository is for little python tools to do math for me for assorted sewing projects.

## Fabric yardage optimizer
yardage.py

### Background
Fabric is sold by the yard, cut from bolts of varying width. Determining how much to buy is a major annoyance but provides a simple packing problem.

### Solution
Function to determine yardage required to cut a given assortment of rectangles from fabric of a given width.

### Details
Vertical and horizontal dimensions of each rectangle is specified in a dataframe.

All rectangles keep the same orientation, yardage is returned for vertical facing the width of the fabric or facing along the length.

Yardage is only returned if the fabric is wide enough for all rectangles to be cut in that direction.

Visualization is returned using matplotlib.

### Future changes
Piecing options: when large pieces are needed, supply options for smaller peieces. For example, a 110" rectangle is cut in one piece from 120" fabric, but from a 50" and two 30" pieces from 60" fabric.

Automatically run through all options instead of one call per options

Include sizes on the matplotlib visualization.
