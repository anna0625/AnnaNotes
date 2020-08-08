import turtle
import tkinter

WIDTH = 15
BRANCH_LENGTH = 120
ROTATION_LENGTH = 27

# below has some bugs.

class Tree_Fractal(turtle.Turtle):
    def __init__(self, level):
        super(Tree_Fractal, self).__init__()
        turtle.hideturtle() #MUCH faster drawing and better view
        self.level = level
        self.hideturtle()
        self.speed('fastest')
        self.left(90)
        self.width(WIDTH)
        self.penup()
        self.back(BRANCH_LENGTH * 1.5)
        self.pendown()
        self.forward(BRANCH_LENGTH)
        self.draw_tree(BRANCH_LENGTH, level)

    def draw_tree(self, branch_length, level):
        turtle.hideturtle() #MUCH faster drawing and better view
        width = self.width()
        self.width(width * 3. / 4.)
        branch_length *= 3. / 4.
        self.left(ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.right(2 * ROTATION_LENGTH)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.left(ROTATION_LENGTH)

        self.width(width)


if __name__ == '__main__':
    tree_level = 11  # choose
    tree = Tree_Fractal(tree_level)
    turtle.done()


'''
import turtle
for i in range(2048): #how many branches(2 ** depth)
    turtle.goto(0,0) #beginning of tree
    turtle.setheading(90) #direction(try 270 for root effect)
    turtle.hideturtle() #MUCH faster drawing and better view
    a = str(bin(i)).replace('0b','') #binary is for two branches('0b' ignored)
    a = list(str('0' * (11 - len(list(a)))) + a) #cake filling
    turtle.speed(0) #no animation
    turtle.pendown() #you probably wanna draw it
    for f in range(len(a)): #depth
        b = 200 #primary branch length
        for l in range(f + 1): #more depth less length
            b /= 1.5 #the difference of branch length(b = b / float)
        turtle.width(b / 10) #branch width(for better effect)
        turtle.forward(b) #drawing a branch
        turtle.right((int(a[f]) - 0.5) * 60) #change 60 to any angle
    turtle.penup() #also try without this line
'''