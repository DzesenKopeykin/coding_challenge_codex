import unittest
import script
from canvas import Canvas


class TestScriptFile(unittest.TestCase):

    def test_drawing(self):
        input_file = open('./test_input.txt', 'w')
        output_file = open('./test_output.txt', 'w')
        input_file.write('C 4 3\nL 1 1 2 1\nR 2 2 3 3\nB 4 3 v')
        output_file.close()
        input_file.close()
        script.drawing('./test_input.txt', './test_output.txt')
        with open('./test_output.txt', 'r') as f:
            self.assertEqual(f.read(), '------\n'
                                       '|    |\n'
                                       '|    |\n'
                                       '|    |\n'
                                       '------\n'
                                       '------\n'
                                       '|xx  |\n'
                                       '|    |\n'
                                       '|    |\n'
                                       '------\n'
                                       '------\n'
                                       '|xx  |\n'
                                       '| xx |\n'
                                       '| xx |\n'
                                       '------\n'
                                       '------\n'
                                       '|xxvv|\n'
                                       '| xxv|\n'
                                       '| xxv|\n'
                                       '------\n')

    def test_drawing_error(self):
        self.assertRaises(script.DrawError, script.execute_command, 'L 1 1 2 1', None)
        self.assertRaises(script.DrawError, script.execute_command, 'L 1 1 2 1 3', Canvas(5, 5))


if __name__ == '__main__':
    unittest.main()
