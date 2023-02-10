import vsketch
from shapely.geometry import Point
import math

class MiscDebuggingSketch(vsketch.SketchClass):
    # Sketch parameters:
    debug = vsketch.Param(False)
    width = vsketch.Param(5., decimals=2, unit="in")
    height = vsketch.Param(3., decimals=2, unit="in")
    pen_width = vsketch.Param(0.7, decimals=3, unit="mm")
    radius = vsketch.Param(-1, decimals=3, unit="in")
    num_layers = vsketch.Param(1)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size(f"{self.height}x{self.width}", landscape=True, center=True)
        vsk.penWidth(f"{self.pen_width}")

        # implement your sketch here
        layers = [1 + i for i in range(self.num_layers)]
        layer = layers[math.floor(vsk.random(0, len(layers)))]
        vsk.stroke(layer)
        vsk.fill(layer)
        vsk.circle(0, 0, self.radius*2)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    MiscDebuggingSketch.display()
