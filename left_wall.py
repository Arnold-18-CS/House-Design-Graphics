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

# Adding Windows
ctx.move_to(110,160)
ctx.line_to(110,140)
ctx.line_to(97, 135)
ctx.line_to(97, 155)
ctx.close_path()

ctx.move_to(93, 155)
ctx.line_to(93, 135)
ctx.line_to(80, 130)
ctx.line_to(80, 150)
ctx.close_path()

ctx.move_to(110, 128)
ctx.line_to(110, 110)
ctx.line_to(97, 105)
ctx.line_to(97, 123)
ctx.close_path()

ctx.move_to(93, 105)
ctx.line_to(80, 100)
ctx.line_to(80, 119)
ctx.line_to(93, 123)
ctx.close_path()

ctx.stroke()



surface.write_to_png('left_wall.png')
