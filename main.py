import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1,1,1)
ctx.paint()

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

# Left Wall structure
ctx.move_to(120, 178)
ctx.line_to(120, 105)

ctx.move_to(70, 80)
ctx.line_to(70, 165)


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

# Draw the back roof (angled for 3D effect)
ctx.move_to(60, 85)
ctx.line_to(145, 45)
ctx.line_to(175, 35)
ctx.line_to(90, 75)
ctx.close_path()

# Draw the front roof (angled for 3D effect)
ctx.move_to(120, 105)
ctx.line_to(200, 60)
ctx.line_to(175, 35)
ctx.line_to(90, 75)
ctx.close_path()


# Chimney
#front part
ctx.move_to(160, 45)
ctx.line_to(160, 60)
ctx.line_to(165, 62)
ctx.line_to(165, 48)
ctx.close_path()


#lateral part
ctx.move_to(165, 62)
ctx.line_to(175, 55)
ctx.line_to(175, 43)
ctx.line_to(165, 48)


#top part
ctx.move_to(160, 45)
ctx.line_to(170, 40)
ctx.line_to(175, 43)


ctx.set_line_width(0.8)
ctx.set_source_rgb(0,0,0)
ctx.stroke()

# Right Wall
ctx.move_to(120, 180)
ctx.line_to(120, 105)
ctx.move_to(190, 65)
ctx.line_to(190, 145)
# ctx.line_to(147, 186)
# ctx.close_path()

ctx.move_to(155, 150)
ctx.line_to(175, 140)
ctx.line_to(185, 145)
ctx.line_to(165, 155)
ctx.close_path()

ctx.move_to(155, 150)
ctx.line_to(155, 165)
ctx.line_to(180, 170)
ctx.line_to(200, 160)
ctx.line_to(200, 155)
ctx.line_to(185, 150)
ctx.line_to(165, 160)
ctx.line_to(180, 165)
ctx.line_to(180, 170)

ctx.move_to(180, 165)
ctx.line_to(200, 155)
ctx.move_to(165, 160)
ctx.line_to(165, 155)

ctx.move_to(185, 150)
ctx.line_to(185, 145)

ctx.move_to(120, 180)
ctx.line_to(155, 160)

ctx.move_to(190, 145)
ctx.line_to(185, 147)

# Door
ctx.move_to(155, 150)
ctx.line_to(155, 110)
ctx.line_to(175, 100)
ctx.line_to(175, 140)

# Door window
ctx.move_to(157, 110)
ctx.line_to(157, 145)
ctx.line_to(165, 141)
ctx.line_to(165, 106)

# R-wall windows
ctx.move_to(150, 115)
ctx.line_to(150, 93)
ctx.line_to(140, 100)
ctx.line_to(140, 121)
ctx.close_path()

ctx.move_to(136, 102)
ctx.line_to(125, 108)
ctx.line_to(125, 128)
ctx.line_to(136, 123)
ctx.close_path()

ctx.set_source_rgb(0,0,0)
ctx.set_line_width(0.8)
ctx.stroke()

surface.write_to_png('house.png')