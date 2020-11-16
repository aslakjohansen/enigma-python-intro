import cairo

mm = lambda value: float(value)/25.4*72
width, height = mm(60), mm(100)

surface = cairo.PDFSurface('cairoexample.pdf', width, height)
c = cairo.Context(surface)

c.move_to(0, 0)
c.line_to(width, height)
c.set_line_width(7.8)
c.set_source_rgb(0.8, 0.8, 1)
c.stroke()

c.move_to(0,0)
c.line_to(width,0)
c.line_to(0,height)
c.close_path()
c.set_source_rgba(0, 1, 0, 0.5)
c.fill()
