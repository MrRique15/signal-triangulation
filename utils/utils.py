#!/usr/bin/env python

import matplotlib.pyplot as plt 
from matplotlib.patches import Circle

def prepare_data(receptors, case):
    coordinates = [r.coordinates for r in receptors]
    radii = [r.calculate_dk(case[r.name]) for r in receptors]
    colors = [r.color for r in receptors]
    return coordinates, radii, colors

def create_plot(receptors, case, emissor, caseName=""):
    fig, ax = plt.subplots()
    
    coordinates, radii, colors = prepare_data(receptors=receptors, case=case)
    ax.set_aspect('equal')
    
    for a, r, c in zip(coordinates, radii, colors):
        circle = Circle((a[0], a[1]), r, color=c, fill=False, linewidth=1, facecolor='none')
        ax.add_patch(circle)

    ax.add_patch(Circle((emissor[0], emissor[1]), 0.3, color="black", fill=True))
    
    plt.title(f"Plotagem {caseName}")
    plt.scatter(*zip(*coordinates))
    plt.show()