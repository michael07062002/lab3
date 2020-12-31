from struct import pack
from math import sin,pi
def form_information_header(long, height):
    header_size = 40
    planes = 1
    bits_per_pixel = 8
    compression = 0
    image_size = 0
    x_pixels_per_meter = 0
    y_pixels_per_meter = 0
    total_colors = 2
    important_colors = 0
    return pack(
        "<3L2H6L",
        header_size,
        long,
        height,
        planes,
        bits_per_pixel,
        compression,
        image_size,
        x_pixels_per_meter,
        y_pixels_per_meter,
        total_colors,
        important_colors,
    )






def form_bmp_header(long, height):
    filetype = 19778
    reserved_1 = 0
    reserved_2 = 0
    offset = 62
    filesize = offset + 1 * long * height
    return pack("<HL2HL", filetype, filesize, reserved_1, reserved_2, offset)
def form_pixels(begin, end, step):
    pixels = []
    x_min = y_min = float("inf")
    t = begin
    while t <= end:
        x = round(sin(5*t -pi/2), 2)
        if x < x_min:
            x_min = x
        y = round( sin(6*t) , 2)
        if y < y_min:
            y_min = y
        pixels.append((x, y))
        t += step
    pixels.reverse()
    return pixels, x_min, y_min


def form_colors():
    color_1 = (0, 0, 255, 0)
    color_2 = (255, 255, 255, 0)
    return pack("<8B", *color_1, *color_2)


def write_file(begin, end, step, long, height, filename):
    with open("{}.bmp".format(filename), "wb") as f:
        f.write(form_bmp_header(long, height))
        f.write(form_information_header(long, height))
        f.write(form_colors())
        pixels, x_min, y_min = form_pixels(begin, end, step)

        y_pix = y_min
        for i in range(height):
            x_pix = x_min
            for j in range(long):
                if (x_pix, y_pix) in pixels:
                    f.write(pack("<B", 0))
                else:
                    f.write(pack("<B", 1))
                x_pix = round(x_pix + step, 2)
            y_pix = round(y_pix + step, 2)
write_file(0, 10 * pi, 0.01, 200, 200, "resualt")
