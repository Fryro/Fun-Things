colours_list = ["red", "blue", "green", "purple", "orange"]

def pentagon(colour):
    pendown()
    begin_fill()
    color(colour)
    left(72)
    for i in range(5):
        forward(50)
        right(72)
    end_fill()
        
        
penup()
left(90)
forward(50)
for i in range(5):
    penup()
    pentagon(colours_list[i])
    penup()
    forward(50)
