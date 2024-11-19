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

# Ground structure
context.move_to(70,158)
context.line_to(40, 170)
context.line_to(140, 200)
context.line_to(240, 150)
context.line_to(190,135)

context.move_to(40,170)
context.line_to(40,180)
context.line_to(140,210)
context.line_to(240,160)
context.line_to(240,150)

context.move_to(140,200)
context.line_to(140,210)

context.set_source_rgb(0,0,0)
context.set_line_width(0.8)
context.stroke()
