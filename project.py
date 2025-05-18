from graphics import Canvas
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_rectangles(canvas, 0, 0)
    
def draw_rectangles(canvas, start_x, start_y):
    color = random_color()
    canvas.create_rectangle(start_x, start_y, CANVAS_WIDTH, CANVAS_HEIGHT, color)
    color = random_color()
    canvas.create_rectangle(start_x+20, start_y+20, CANVAS_WIDTH-20, CANVAS_HEIGHT-20, color)
    color = random_color()
    canvas.create_rectangle(start_x+40, start_y+40, CANVAS_WIDTH-40, CANVAS_HEIGHT-40, color)
    color = random_color()
    canvas.create_rectangle(start_x+60, start_y+60, CANVAS_WIDTH-60, CANVAS_HEIGHT-60, color)
    color = random_color()
    canvas.create_rectangle(start_x+80, start_y+80, CANVAS_WIDTH-80, CANVAS_HEIGHT-80, color)
    color = random_color()
    canvas.create_rectangle(start_x+100, start_y+100, CANVAS_WIDTH-100, CANVAS_HEIGHT-100, color)
    color = random_color()
    canvas.create_rectangle(start_x+120, start_y+120, CANVAS_WIDTH-120, CANVAS_HEIGHT-120, color)
    color = random_color()
    canvas.create_rectangle(start_x+120, start_y+120, CANVAS_WIDTH-120, CANVAS_HEIGHT-120, color)
    color = random_color()
    canvas.create_rectangle(start_x+140, start_y+140, CANVAS_WIDTH-140, CANVAS_HEIGHT-140, color)
    color = random_color()
    canvas.create_rectangle(start_x+160, start_y+160, CANVAS_WIDTH-160, CANVAS_HEIGHT-160, color)
    color = random_color()
    canvas.create_rectangle(start_x+180, start_y+180, CANVAS_WIDTH-180, CANVAS_HEIGHT-180, color)

def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen', "firebrick", "indianred", "lightcoral", "salmon", "lightpink", "pink"]
    return random.choice(colors)

if __name__ == '__main__':
    main()
