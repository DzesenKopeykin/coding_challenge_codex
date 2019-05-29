from canvas import Canvas, DrawError


def drawing(input_path='./input.txt', output_path='./output.txt'):
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        canvas = None
        for command in input_file.read().split('\n'):
            try:
                canvas = execute_command(command, canvas)
            except DrawError as de:
                print('incorrect input file: ' + str(de))
                return
            output_file.write(str(canvas) + '\n')


def execute_command(command, canvas):
    params = command.split(' ')
    if params[0] == 'C' and len(params) == 3:
        return Canvas(int(params[1]), int(params[2]))
    elif not canvas:
        raise DrawError('canvas not created')
    elif params[0] == 'L' and len(params) == 5:
        canvas.draw_line(*map(int, params[1:]))
    elif params[0] == 'R' and len(params) == 5:
        canvas.draw_rectangle(*map(int, params[1:]))
    elif params[0] == 'B' and len(params) == 4:
        canvas.bucket_fill(int(params[1]), int(params[2]), params[3])
    else:
        raise DrawError('unknown command')
    return canvas


if __name__ == '__main__':
    drawing()
