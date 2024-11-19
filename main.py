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
ctx.move_to(70,158)
ctx.line_to(40, 170)
ctx.line_to(140, 200)
ctx.line_to(240, 150)
ctx.line_to(190,135)

ctx.move_to(40,170)
ctx.line_to(40,180)
ctx.line_to(140,210)
ctx.line_to(240,160)
ctx.line_to(240,150)

ctx.move_to(140,200)
ctx.line_to(140,210)

ctx.set_source_rgb(0,0,0)
ctx.set_line_width(0.8)
ctx.stroke()

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

surface.write_to_png('house.png')