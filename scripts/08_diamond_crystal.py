"""
Icon 8: Diamond / Crystal Facet
Geometric gem shape — represents crystallography through a polished crystal form.
Faceted diamond with light refraction effect.
"""
import cairo
import math

SIZE = 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SIZE, SIZE)
ctx = cairo.Context(surface)

# Background - dark navy gradient
gradient = cairo.LinearGradient(0, 0, 0, SIZE)
gradient.add_color_stop_rgb(0, 0.075, 0.145, 0.267)  # darker navy top
gradient.add_color_stop_rgb(1, 0.047, 0.098, 0.200)  # even darker bottom
ctx.set_source(gradient)
ctx.rectangle(0, 0, SIZE, SIZE)
ctx.fill()

cx, cy = SIZE / 2, SIZE / 2

# Diamond outline points
top = (cx, cy - 55)
left = (cx - 50, cy - 10)
right = (cx + 50, cy - 10)
bottom = (cx, cy + 60)

# Crown facets (top trapezoid)
crown_left = (cx - 30, cy - 10)
crown_right = (cx + 30, cy - 10)
crown_top_left = (cx - 18, cy - 55)
crown_top_right = (cx + 18, cy - 55)

# Facet colors - blues and teals with varying lightness
facets = [
    # Left crown facet
    ([top, crown_top_left, left], (0.15, 0.35, 0.55)),
    # Center crown facet
    ([crown_top_left, top, crown_top_right], (0.20, 0.45, 0.65)),
    # Right crown facet
    ([top, crown_top_right, right], (0.12, 0.32, 0.52)),
    # Left pavilion
    ([left, crown_left, bottom], (0.10, 0.28, 0.48)),
    # Center-left pavilion
    ([crown_left, (cx, cy - 10), bottom], (0.18, 0.42, 0.62)),
    # Center-right pavilion
    ([(cx, cy - 10), crown_right, bottom], (0.22, 0.50, 0.70)),
    # Right pavilion
    ([crown_right, right, bottom], (0.13, 0.33, 0.53)),
    # Girdle left
    ([left, crown_left, crown_top_left], (0.16, 0.38, 0.58)),
    # Girdle right
    ([crown_top_right, crown_right, right], (0.14, 0.36, 0.56)),
    # Girdle center
    ([crown_top_left, crown_top_right, crown_right, crown_left], (0.20, 0.48, 0.68)),
]

for pts, color in facets:
    ctx.move_to(*pts[0])
    for pt in pts[1:]:
        ctx.line_to(*pt)
    ctx.close_path()
    ctx.set_source_rgba(color[0], color[1], color[2], 0.85)
    ctx.fill_preserve()
    ctx.set_source_rgba(0.6, 0.8, 1.0, 0.3)
    ctx.set_line_width(0.8)
    ctx.stroke()

# Diamond outline
outline = [top, right, bottom, left]
ctx.move_to(*outline[0])
for pt in outline[1:]:
    ctx.line_to(*pt)
ctx.close_path()
ctx.set_source_rgba(0.431, 0.749, 0.890, 0.8)  # light blue outline
ctx.set_line_width(2)
ctx.stroke()

# Sparkle at top
ctx.set_source_rgba(1, 1, 1, 0.8)
ctx.arc(cx, cy - 52, 3, 0, 2 * math.pi)
ctx.fill()

# Light refraction lines inside
ctx.set_source_rgba(0.961, 0.620, 0.043, 0.15)  # subtle amber refraction
ctx.set_line_width(1)
ctx.move_to(cx - 15, cy - 40)
ctx.line_to(cx + 25, cy + 20)
ctx.stroke()
ctx.move_to(cx + 10, cy - 45)
ctx.line_to(cx - 20, cy + 15)
ctx.stroke()

surface.write_to_png("08_diamond_crystal.png")
print("Generated: 08_diamond_crystal.png")
