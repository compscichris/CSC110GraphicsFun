### Chris Chen
### 10/1/2018
### This program creates an image of a mountain scenery, and allows the users to
### interact with it using a mouse, changing the angle of the view. 

# importing classes
import sys
import os
import random
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def main():
    ''' 
    main is the main function that calls the rest of the functions used to draw 
    the graphics. The main while loop calls many functions, initializes the mountain
    colors calling the store_mountains function, initializes the list bird_index with
    the original.
    '''
    gui = graphics(800,800,'Motion Parallax')
    back_color = gui.get_color_string(183, 247, 255)
    grass_color = gui.get_color_string(117, 239, 137)
    
    # List, since we just learned that and you said I could. :)
    bird_index = [-40, -120, -200, -280, -360]
    mountain1, mountain2, mountain3 = store_mountains(gui)
    
    # Infinite while-loop to make sure program runs forever until exiting. It does
    # not conflict with other functions in this program.
    while True:
        gui.clear()
        x_pos = (gui.mouse_x - 400)/7
        y_pos = (gui.mouse_y - 400)/7
        gui.rectangle(0, 0, 800, 800, back_color)
        draw_mountains(mountain1, mountain2, mountain3, x_pos, y_pos, gui)
        draw_sun(x_pos, y_pos, gui)
        draw_grass(x_pos, y_pos, gui, grass_color)
        draw_tree(x_pos, y_pos, gui)
        draw_flock(bird_index, gui)
        gui.update_frame(30)

def draw_flock(bird_index, gui):
    ''' 
    draw_flock takes in a list of integers (which represent the starting index
    values of each bird). The function utilizes a while loop to call each 
    individual index value of the birds so that it can call draw_birds, taking
    parameters of the starting x index and y index.
    bird_index is list of starting bird x positions.
    gui is the graphics object.
    '''
    index = 0
    while(index < 5):
        if(bird_index[index] > 920):
            bird_index[index] = -40
        draw_bird(bird_index[index], 160 + 20 * (4 - index),gui)
        bird_index[index]= bird_index[index] + 5
        index += 1

def draw_bird(x, y, gui):
    ''' 
    draw_bird draws birds of length 40, height 10.
    x and y are integers based on starting position of the birds x,y.
    gui is the graphics object.
    '''
    gui.line(x, y, x + 20, y + 10, 'black')
    gui.line(x + 20, y + 10, x + 40, y, 'black')

def random_color(gui):
    ''' 
    random_color generates a random color from the values received from 
    random_generator.
    gui is the graphics object.
    '''
    return gui.get_color_string(random_generator(), random_generator(), random_generator())

def random_generator():
    '''
    random_generator generates a random number between 0 and 255 for a r, g, or b 
    value.
    '''
    random_value = random.randint(0, 255)
    return random_value
    
def draw_grass(x_pos, y_pos, gui, grass_color):
    '''
    draw_grass draws the grass and ground.
    x_pos and y_pos are integers based on mouse position x,y.
    gui is the graphics object.
    grass_color is the color of the grass.
    '''
    gui.rectangle(0, 700 + y_pos, 800, 210, grass_color)
    index = -400
    while (index) < (1200):
        gui.line(index + x_pos, 680 + y_pos, index + x_pos, 710 + y_pos, grass_color)
        index += 5
     
def draw_tree(x_pos, y_pos, gui):
    ''' 
    draw_tree draws the tree.
    x_pos and y_pos are integers based on mouse position x,y.
    gui is the graphics object.
    '''   
    gui.rectangle(480 + x_pos, 670 + y_pos, 14, 60, 'brown')
    gui.ellipse(487 + x_pos, 650 + y_pos, 60, 80, 'green')

def draw_sun(x_pos, y_pos, gui):
    '''
    draw_sun draws the sun.
    x_pos and y_pos are integers based on mouse position x,y.
    gui is the graphics object.
    '''
    gui.ellipse(640 + x_pos/55, 120 + y_pos/55, 80, 80, 'yellow')
    
def store_mountains(gui):
    ''' 
    store_mountains stores the color values of the mountains.
    gui is the graphics object.
    '''
    return random_color(gui), random_color(gui), random_color(gui)
    
def draw_mountains(mountain1, mountain2, mountain3, x_pos, y_pos, gui):
    '''
    draw_mountains draws mountains based of off the random colors found by 
    store_mountains.
    mountain1, mountain2, mountain3 are colors.
    x_pos and y_pos are integers based on mouse position x,y.
    gui is the graphics object.
    '''
    # These are short variable that are representing x,y coordinates:
    # a,b for closer 2 mountains.
    apos = x_pos/2
    bpos = y_pos/2
    # c,d for farther mountain.
    cpos = x_pos/7
    dpos = y_pos/7
    gui.triangle(140 + cpos, 740 + dpos, 420 + cpos, 230 + dpos, 760 + cpos, 740 + dpos, mountain1)
    gui.triangle(-140 + apos, 740 + bpos, 180 + apos, 320 + bpos, 600 + apos, 740 + bpos, mountain2)
    gui.triangle(320 + apos, 740 + bpos, 630 + apos, 320 + bpos, 970 + apos, 740 + bpos, mountain3)

# Calling main.
main()