import tkinter as tk  # py3

from src.staff.pick_colors import pick_colors

# Check that link for more information https://stackoverflow.com/a/26182241/9714136

class GradientFrame(tk.Canvas):
    """A gradient frame which uses a canvas to draw the background"""

    def __init__(self, parent, **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)

        colors = pick_colors()
        self._color1 = colors[0]
        self._color2 = colors[1]
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        """Draw the gradient"""
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, 2000, tags=("gradient",), fill=color)
        self.lower("gradient")
