import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,1,1)
ctx.paint()

# Draw the back roof (angled for 3D effect)
ctx.move_to(60, 85)
ctx.line_to(145, 45)
ctx.line_to(175, 35)
ctx.line_to(90, 75)
ctx.close_path()
ctx.close_path()

# Draw the front roof (angled for 3D effect)
ctx.move_to(175, 35)
ctx.line_to(200, 52.5)
ctx.line_to(115, 95)
ctx.line_to(90, 75)
ctx.line_to(175, 35)
ctx.close_path()

# Chimney
#front part
ctx.move_to(160, 45)
ctx.line_to(160, 60)
ctx.line_to(165, 60)
ctx.line_to(165, 47.5)
ctx.close_path()


#lateral part
ctx.move_to(165, 47.5)
ctx.line_to(165, 60)
ctx.line_to(172.5, 55)
ctx.line_to(172.5, 45)
ctx.close_path()


#top part
ctx.move_to(160, 45)
ctx.line_to(165, 47.5)
ctx.line_to(172.5, 55)
ctx.line_to(170, 37.5)
ctx.line_to(160, 45)
ctx.close_path()


ctx.set_line_width(0.8)
ctx.set_source_rgb(0,0,0)
ctx.stroke()

surface.write_to_png('roof.png')
