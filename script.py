from canvas import Canvas


def start_drawing(input_path='./input.txt', output_path='./output.txt'):
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        canvas = execute_command(input_file.readline().strip())
        output_file.write(str(canvas) + '\n')
        for command in input_file.read().split('\n'):
            execute_command(command, canvas)
            output_file.write(str(canvas) + '\n')


def execute_command(command, canvas=None):
    params = command.split(' ')
    if params[0] == 'C':
        return Canvas(int(params[1]), int(params[2]))
    if params[0] == 'L':
        canvas.draw_line(*map(int, params[1:]))
    if params[0] == 'R':
        canvas.draw_rectangle(*map(int, params[1:]))
    if params[0] == 'B':
        canvas.bucket_fill(int(params[1]), int(params[2]), params[3])


if __name__ == '__main__':
    start_drawing()
