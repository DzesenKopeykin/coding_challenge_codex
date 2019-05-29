import unittest
from canvas import Canvas, DrawError


class TestCanvas(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(4, 3)

    def test_init_canvas(self):
        self.assertEqual(self.canvas.width, 4)
        self.assertEqual(self.canvas.height, 3)
        self.assertEqual(self.canvas.canvas, [[' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' '],
                                              [' ', ' ', ' ', ' ']])

    def test_draw_line(self):
        self.canvas.draw_line(2, 1, 2, 3)
        self.assertEqual(self.canvas.canvas, [[' ', 'x', ' ', ' '],
                                              [' ', 'x', ' ', ' '],
                                              [' ', 'x', ' ', ' ']])

    def test_draw_rectangle(self):
        self.canvas.draw_rectangle(2, 1, 4, 3)
        self.assertEqual(self.canvas.canvas, [[' ', 'x', 'x', 'x'],
                                              [' ', 'x', ' ', 'x'],
                                              [' ', 'x', 'x', 'x']])

    def test_bucket_fill(self):
        self.canvas.draw_rectangle(2, 1, 4, 3)
        self.canvas.bucket_fill(1, 1, 'o')
        self.assertEqual(self.canvas.canvas, [['o', 'x', 'x', 'x'],
                                              ['o', 'x', ' ', 'x'],
                                              ['o', 'x', 'x', 'x']])

    def test_canvas_to_str(self):
        self.canvas.draw_rectangle(2, 1, 4, 3)
        self.canvas.bucket_fill(1, 1, 'o')
        self.assertEqual(str(self.canvas), '------\n|oxxx|\n|ox x|\n|oxxx|\n------')

    def test_draw_line_error(self):
        self.assertRaises(DrawError, self.canvas.draw_line, 20, 1, 3, 3)
        self.assertRaises(DrawError, self.canvas.draw_line, 2, 1, 3, 3)

    def test_draw_rectangle_error(self):
        self.assertRaises(DrawError, self.canvas.draw_rectangle, 20, 1, 3, 3)
        self.assertRaises(DrawError, self.canvas.draw_rectangle, 3, 3, 1, 1)

    def test_draw_bucket_fill_error(self):
        self.assertRaises(DrawError, self.canvas.bucket_fill, -2, 1, 'q')
        self.assertRaises(TypeError, self.canvas.bucket_fill, 3, 3, 2)


if __name__ == '__main__':
    unittest.main()
