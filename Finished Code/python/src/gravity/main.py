"""
CLI entry point for the gravity simulation.

Usage:
    python main.py <scenario_name> <num_gens> <time_step> <canvas_width> <drawing_frequency>

Example:
    python main.py jupiterMoons 2000 0.01 800 5

This will read:   data/jupiterMoons.txt
and write video:  output/jupiterMoons.mp4
"""

import sys
import os
import time
import pygame
import imageio
from custom_io import read_universe
from gravity import simulate_gravity
from drawing import animate_system, pygame_surface_to_numpy, draw_to_canvas, save_video_from_surfaces

def main():
    canvas_width = 800   # num pixels wide and tall for our surface 
    u = read_universe("data/butterfly.txt")

    print((u.bodies[0]).name)

    # surface = draw_to_canvas(universe, canvas_width)
    # pygame.image.save(surface, "output/butterfly.png")


    u = read_universe("data/jupiterMoons.txt")
    print(u.gravitational_constant)
    
    # surface = draw_to_canvas(universe, canvas_width)
    # pygame.image.save(surface, "output/jupiterMoon.png")




    """
    Run the full pipeline:
      1) read universe from file
      2) simulate gravity for N generations
      3) render selected frames to pygame surfaces
      4) encode frames to an MP4 video
    """
    print("Let's simulate gravity!")

if __name__ == "__main__":
    main()