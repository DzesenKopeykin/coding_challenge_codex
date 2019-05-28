class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[' ' for j in range(width)] for i in range(height)]

    def __str__(self):
        result_str = '-' * self.width
        for line in self.canvas:
            result_str += '\n|'
            for char in line:
                result_str += char
            result_str += '|'
        result_str += '\n' + '-' * self.width
        return result_str

    def draw_line(self, x1, y1, x2, y2):
        assert all([x1 <= self.width, x2 <= self.width, y1 <= self.height, y2 <= self.height]), \
               "coordinates outside the canvas: L {x1} {y1} {x2} {y2}".format(x1=x1, y1=y1, x2=x2, y2=y2)
        assert x1 == x2 or y1 == y2, "line isn't vertical or horizontal"
        if x1 > x2 or y1 > y2:
            x1, x2, y1, y2 = x2, x1, y2, y1
        for line in range(y1 - 1, y2):
            for column in range(x1 - 1, x2):
                self.canvas[line][column] = 'x'

    def draw_rectangle(self, x1, y1, x2, y2):
        assert all([x1 <= self.width, x2 <= self.width, y1 <= self.height, y2 <= self.height]), \
               "coordinates outside the canvas: R {x1} {y1} {x2} {y2}".format(x1=x1, y1=y1, x2=x2, y2=y2)
        assert x1 < x2 or y1 > y2, "invalid parameters"
        for line in range(y1 - 1, y2):
            for column in range(x1 - 1, x2):
                if any([line == y1 - 1, line == y2 - 1, column == x1 - 1, column == x2 - 1]):
                    self.canvas[line][column] = 'x'

    def bucket_fill(self, x, y, char):
        assert all([x <= self.width, y <= self.height]), "coordinates outside the canvas: B {x} {y}".format(x=x, y=y)
        if self.canvas[y - 1][x - 1] == 'x':
            return
        Canvas._fill_cells_near(self.canvas, x - 1, y - 1, char)

    @staticmethod
    def _fill_cells_near(canvas, x, y, char):
        canvas[y][x] = char
        for line in range(y - 1 if y > 0 else 0, y + 2):
            for column in range(x - 1 if x > 0 else 0, x + 2):
                try:
                    if (line == y and column == x) or canvas[line][column] == 'x' or canvas[line][column] == char:
                        continue
                except IndexError:
                    continue
                Canvas._fill_cells_near(canvas, column, line, char)
