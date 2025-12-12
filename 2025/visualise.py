#!/usr/bin/env python3

import sys
import time
from pprint import pprint

# use non-interactive backend
import matplotlib
matplotlib.use("Agg")

# use plotting libraries
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.animation import PillowWriter

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"
outfile_png = infile.rpartition('.')[0] + ".png"
outfile_gif = infile.rpartition('.')[0] + ".gif"
outfile_mp4 = infile.rpartition('.')[0] + ".mp4"

total = 0
with open(infile, 'r') as file:
    # read coordinates
    data = [tuple(map(int, line.strip().split(","))) for line in file]

x_vals = [x for x, y in data]
y_vals = [y for x, y in data]
x_max, y_max = max(x_vals), max(y_vals)

def apply_axes():
    plt.xlim(0, x_max+1)
    plt.ylim(0, y_max+1)
    plt.gca().invert_yaxis()
    plt.axis('off')

# Create static plot
print(f"Creating static plot")
apply_axes()
plt.scatter(x_vals, y_vals, s=1, c="black")
print(f"Saving to {outfile_png}")
plt.savefig(outfile_png, dpi=150)
plt.close()

# Create animated plot
print(f"Creating animated plot")
apply_axes()
scatter = plt.scatter([], [], s=1, c="black")

def update(frame):
    scatter.set_offsets(data[:frame+1])
    return (scatter,)

animation = ani.FuncAnimation(
    plt.gcf(),          # current figure
    update,             # update function
    frames=len(data),   # number of frames
    interval=10,        # ms between frames
    blit=True
)
print(f"Saving to {outfile_mp4}")
animation.save(outfile_mp4, writer="ffmpeg", dpi=150)
print(f"Saving to {outfile_gif}")
#slow! animation.save(outfile_gif, writer="imagemagick", dpi=150)
animation.save(outfile_gif, writer=PillowWriter(fps=30), dpi=150)

t1 = time.perf_counter()
print(f"Execution time: {t1 - t0:.6f} seconds")
