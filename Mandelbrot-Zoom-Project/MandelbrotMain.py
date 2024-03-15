import random
import numpy as np
import matplotlib
import time
from PIL import Image
import colorsys


def make_image(center_num, width, n):
    image = Image.new("RGB", (n, n), (255, 255, 255))
    pixels = image.load()
    pixels[n/2, n/2] = dist_to_color(calc(center_num), 10**8)
    for x in range(n):
        for y in range(n):
            coordinate = (center_num[0] + ((x-(n/2)) * (width / n)), center_num[1] + ((y-(n/2)) * (width / n)))
            pixels[x, y] = dist_to_color(calc(coordinate), 10**8)
    image.show()
    return image


# max_distance is set to 10^8.
def dist_to_color(distance, max_distance):
    if distance >= max_distance:
        return 0, 0, 0
    temp_num = 0
    if distance != 0:
        temp_num = np.abs(31*np.log10(distance)) / 256
    r, g, b = colorsys.hsv_to_rgb(temp_num, 1.0, 1.0)
    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    return r, g, b


# coordinate takes (a, b) pair referring to the a and b in (a + bi).
# coordinate[0] returns the "a" and coordinate[1] returns the b
def calc(coordinate):
    z_500 = recurse_calc(500, coordinate, coordinate)
    distance = np.sqrt((coordinate[0]-z_500[0])**2 + (coordinate[1]-z_500[1])**2)
    return distance


def recurse_calc(counter, zn, z0):
    if counter == 0:
        return zn
    if zn[0] > 10**10 or zn[1] > 10**10:
        return 10**10, 10**10
    zn_sqr = (zn[0]**2 - zn[1]**2, 2*zn[0]*zn[1])
    next_coord = zn_sqr[0] + z0[0], zn_sqr[1] + z0[1]
    return recurse_calc(counter-1, next_coord, z0)
