import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,1,1)
ctx.paint()

# Wall structure
ctx.move_to(120, 180)
ctx.line_to(120, 95)
ctx.line_to(70, 80)
ctx.line_to(70, 165)
ctx.close_path()

ctx.move_to(120, 175)
ctx.line_to(70, 160)
ctx.line_to(70, 165)
ctx.line_to(120, 180)
ctx.close_path()

ctx.set_source_rgb(0,0,0)
ctx.set_line_width(0.8)
ctx.stroke()

surface.write_to_png('left_wall.png')
