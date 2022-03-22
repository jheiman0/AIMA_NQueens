import tkinter as tk

class NQueensGUI:
    def __init__(self, sol, N=8, size=320, colors=('white', 'black', 'red')):
        self.sol = sol
        self.size = size
        self.square_size = size / N
        self.N = N
        self.colors = colors
        self.__draw()

    def __draw(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, height=self.size, width=self.size)
        canvas.pack()

        color = self.colors[0]
        for y in range(self.N):
            for x in range(self.N):
                color = self.colors[2] if (x, y) in self.sol else color
                canvas.create_rectangle((
                    x*self.square_size,
                    y*self.square_size,
                    x*self.square_size + self.square_size,
                    y*self.square_size + self.square_size), fill=color)
                color = self.colors[0] if (y + x) % 2 == 1 else self.colors[1]
            color = self.colors[0] if (y + x) % 2 == (self.N % 2) else self.colors[1]

        root.mainloop()

