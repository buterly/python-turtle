import turtle as t

p = t.Turtle()

p.getscreen().bgcolor('black')

#p.color('yellow')

p.speed(10)

for j in range(100):
    p.color('yellow')
    for i in range(5):
        p.forward(100+j)
        p.left(216)

    p.color('red')
    p.left(216)
    p.forward(100+j*10)

t.done()
