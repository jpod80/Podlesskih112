# Задание 1. Написать функцию, принимающую некоторую информацию о геометрической фигуре.

from math import pi
def area_geom_fig(figure_type, **kwargs):
    #print(figure_type, kwargs)
    if figure_type == "rombus":
        return kwargs["d1"] * kwargs["d2"] / 2
    elif figure_type == "square":
        return kwargs["a"] * 4
    elif figure_type == "trapezoid":
        return 0.5 * (kwargs["a"] + kwargs["b"]) * kwargs["h"]
    elif figure_type == "circle":
        return pi * kwargs["r"]**2
    elif figure_type == "unknown":
        return "invalid data"

# figure_type = "rombus", d1=10, d2=8
# figure_type = "square", a=5
# figure_type = "trapezoid", a=12, b=3, h=6
# figure_type = "circle", r=18
# figure_type = "unknown", a=1, b=2, c=3

print(area_geom_fig(figure_type="rombus", d1=10, d2=8))
