from colour import Color

import canvas
import camera
import helpers
import shapes
import transform

def main():
    # Size
    w, h = helpers.DEF_WIDTH, helpers.DEF_HEIGHT
    
    # Tests
    c = camera.Camera(width=w, height=h, loop_behavior="reverse")
    t = transform.Transform.IDENTITY().shift(w / 8, h / 8).rotate_about(
    		w / 2, h / 2, 180)
    pt = transform.Transform.RESIZE_ABOUT(w / 2, h / 2, 1., .5)
    s = shapes.TestShapeChildren(stroke_color="red", stroke_width=2.,
                          		 fill_color=Color("green"), transform=t,
                          		 parent_transform=pt)
    b1 = shapes.BezierCurve((0, 0), (0, h), (w, h), (w, 0),
                            stroke_color="#FF00FF", stroke_width=8.)
    b2 = shapes.BezierCurve((0, 0), (0, h), (w, h), (w, 0),
                            stroke_color="aqua", stroke_width=5.,
                            slice_pos=.5, close_path=True)
    b3 = shapes.BezierCurve((0, 0), (0, h), (w, h), (w, 0),
                            stroke_color=(1., 0., 0.), stroke_width=2.,
                            slice_pos=.25)
    s.add(b1, b2, b3)
    p = shapes.Polyline((w / 4, h / 4), (w / 2, 3 * h / 4), (3 * w / 4, h / 4),
                        smooth=True, closed=True, stroke_color="white")
    for shape in s.flatten():
        print shape
    parts = helpers.DEF_FPS
    for i in range(0, parts + 1):
        f = 1. * i / parts
        f2 = 1. * (i + 1) / (parts + 1)
        b2.slice(1. * f)
        s.update_transform(transform.Transform.RESIZE_ABOUT(w / 2, h / 2,
                                                            2. * f2,
                                                            1. * f2))
        p.points[0, :] = [w / 2 * f2, h / 2 * f2]
        p.update_symbol()
        c.capture_frame(s, p)
    c.show()

if __name__ == "__main__":
    main()
