from io import StringIO

import numpy as np
import svgwrite


def create_beam_svg(L, B, H, a, e, qu, tipo):
    a = a * 100
    L = L * 100

    # THE CROSS SECTION
    dwg_cross_sec = svgwrite.Drawing(size=(10 + a + B + 10, 30 + e + H + 10))

    # Draw the beam

    # Dibujar la viga
    dwg_cross_sec.add(dwg_cross_sec.rect((10 + a/2 - B/2, 10), (B, H), fill='lightgray', stroke='black', stroke_width=1))
    # Beam Dimensions
    x = 10 + a/2
    y = 10 + H + 10
    dwg_cross_sec.add(dwg_cross_sec.text(f'{B} cm', insert=(x, y), text_anchor='middle', font_size=10))
    # Beam Dimensions
    x = 10 + a/2 + B/2 + 10
    y = 10 + H / 2
    dwg_cross_sec.add(dwg_cross_sec.text(f'{H} cm', insert=(x, y), text_anchor='middle', font_size=10, font_family="Serif",transform=f"rotate(-90 {x} {y})"))

    # Dibujar la losa
    dwg_cross_sec.add(dwg_cross_sec.rect((10, 10), (a, e), fill='lightgray', stroke='black', stroke_width=1, opacity=0.5))
    # Slab dimensions
    x = 10 + a / 2
    y = 8
    dwg_cross_sec.add(dwg_cross_sec.text(f'Tributary width = {a} cm', insert=(x, y), text_anchor='middle', font_size=10))

    x = 10 + a + 10
    y = 10 + e / 2
    dwg_cross_sec.add(dwg_cross_sec.text(f'{e} cm', insert=(x, y), text_anchor='middle', font_size=10, font_family="Serif",transform=f"rotate(-90 {x} {y})"))

    # Write the SVG content to a buffer
    buffer_cross_sec = StringIO()
    dwg_cross_sec.write(buffer_cross_sec)

    ## ELEVATION

    top_margin = 25

    dwg = svgwrite.Drawing(size=(10 + L + 10, 30 + e + H * 2 + 10))

    # the beam
    dwg.add(dwg.rect((10, top_margin + 15), (L, H), 
                     fill='lightgray', stroke='black', stroke_width=1, opacity=1.0))   
    
    # the slab
    dwg.add(dwg.rect((10, top_margin + 15), (L, e), 
                     fill='lightgray', stroke='black', stroke_width=1, opacity=0.5))

    # The lenght
    x = 10 + L / 2
    y = top_margin + H + 30
    dwg.add(dwg_cross_sec.text(f'{L=} cm', insert=(x, y), text_anchor='middle', font_size=16))

    # Displaying the load

    # create a new marker object
    marker = dwg.marker(insert=(5,5), size=(10,10))

    # red point as marker
    arrow = dwg.polygon([(0, 0), (10, 0), (5, 10)], stroke='black', fill='blue')
    marker.add(arrow)

    # add marker to defs section of the drawing
    dwg.defs.add(marker)

    x = 10 + L / 2
    y = top_margin - 5
    dwg.add(dwg_cross_sec.text(f'qu = {round(qu, 3)} [ton / m]', insert=(x, y), text_anchor='middle', font_size=16))

    for x_pos in np.linspace(10 + 5, L, 10):
        line = dwg.add(dwg.polyline([(x_pos, top_margin), (x_pos, top_margin + 10),], 
                                    stroke='black', fill='black'))

        # set individually markers, to just set the end marker set other markers to None or False:
        line.set_markers((None, None, marker))

    # los apoyos

    # create a new marker object
    marker1 = dwg.marker(insert=(0,0), size=(30,30))
    marker2 = dwg.marker(insert=(0,0), size=(30,30))

    # add marker to defs section of the drawing
    dwg.defs.add(marker1)
    dwg.defs.add(marker2)
    
    if tipo == "Pined-Pined":
        
        arrow1 = dwg.polygon([(0, 20), (20, 20), (10, 0)], stroke='black', fill='orange')
        marker1.add(arrow1)
        marker2.add(arrow1)
    
    elif tipo == "Pined-Fixed":
        arrow1 = dwg.polygon([(0, 20), (20, 20), (10, 0)], stroke='black', fill='orange')
        arrow2 = dwg.polygon([(0, 20), (20, 20), (20, 0), (0, 0)], stroke='black', fill='orange')
        marker1.add(arrow1)
        marker2.add(arrow2)

    elif tipo == "Fixed-Fixed":
        arrow1 = dwg.polygon([(0, 20), (20, 20), (10, 0)], stroke='black', fill='orange')
        arrow2 = dwg.polygon([(0, 20), (20, 20), (20, 0), (0, 0)], stroke='black', fill='orange')
        marker1.add(arrow2)
        marker2.add(arrow2)
    
    else:
        arrow1 = dwg.polygon([(0, 20), (20, 20), (10, 0)], stroke='black', fill='orange')
        arrow2 = dwg.polygon([(0, 20), (20, 20), (20, 0), (0, 0)], stroke='black', fill='orange')
        marker1.add(arrow2)
        # marker2.add(arrow2)

    xi = 0
    yi = top_margin + H + 15
    pin1 = dwg.add(dwg.line((xi, yi), (xi, yi), stroke='black', fill='black'))
    pin1.set_markers((False, False, marker1))

    xi = L
    yi = top_margin + H + 15
    pin2 = dwg.add(dwg.line((xi, yi), (xi, yi), stroke='black', fill='black'))
    pin2.set_markers((False, False, marker2))

    # Write the SVG content to a buffer
    buffer_elevation = StringIO()
    dwg.write(buffer_elevation)

    return buffer_cross_sec.getvalue(), buffer_elevation.getvalue()