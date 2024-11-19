import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 300)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()
