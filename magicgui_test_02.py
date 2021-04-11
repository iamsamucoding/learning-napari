import math
from enum import Enum
from magicgui import magicgui

# dropdown boxes are best made by creating an enum
class Medium(Enum):
    Glass = 1.520
    Oil = 1.515
    Water = 1.333
    Air = 1.0003

# decorate your function with the ``@magicgui`` decorator
@magicgui(call_button="calculate")
def snells_law(aoi=30.0, n1=Medium.Glass, n2=Medium.Water, degrees=True):
    aoi = math.radians(aoi) if degrees else aoi
    try:
        result = math.asin(n1.value * math.sin(aoi) / n2.value)
        return math.degrees(result) if degrees else result
    except ValueError:
        # beyond the critical angle
        return "Total internal reflection!"


def my_callback(event):
    # The callback receives an `Event` object that has the result
    # of the function call in the `value` attribute
    print("Your function was called! The result is", event.value)

snells_law.called.connect(my_callback)

snells_law.show(run=True)

# it will be executed after closing the GUI
result = snells_law()
print(f'result: {result}')

